import argparse
import re
import subprocess
import tempfile
from pathlib import Path
from .context import load_project_context, detect_next_task
from .prompt import build_prompt
from .ia_adapter import IAAdapter
from .task import process_response, marcar_tasca_completada

# Mapatge de llenguatges a extensions i carpeta de destí (corregit)
LANGUAGE_MAP = {
    'python': ('py', 'scripts'),
    'html': ('html', 'content/html'),
    'css': ('css', 'content/css'),
    'javascript': ('js', 'content/js'),
    'markdown': ('md', 'content/markdown'),
    'json': ('json', 'content/json'),
    'yaml': ('yml', 'content/yaml'),
    'sql': ('sql', 'content/sql'),
    'bash': ('sh', 'scripts'),
    'shell': ('sh', 'scripts'),
}

def extreure_nom_fitxer(contingut, prefix=None):
    """
    Extreu un nom descriptiu del contingut.
    - Busca la primera línia que comenci per #, ##, ###, o <title>...
    - Si no, retorna 'document' o el prefix.
    """
    lines = contingut.split('\n')
    for line in lines[:10]:
        # Per Markdown: # Títol, ## Títol, etc.
        match_md = re.match(r'^#+\s+(.+)$', line.strip())
        if match_md:
            nom = match_md.group(1).strip()
            # Netejar el nom: treure caràcters no vàlids
            nom = re.sub(r'[^a-zA-Z0-9àèìòóúïü·\-_\s]', '', nom)
            nom = nom.replace(' ', '_').lower()
            return nom[:50]  # limitar longitud
        
        # Per HTML: <title>...</title>
        match_title = re.search(r'<title>(.+?)</title>', line, re.IGNORECASE)
        if match_title:
            nom = match_title.group(1).strip()
            nom = re.sub(r'[^a-zA-Z0-9àèìòóúïü·\-_\s]', '', nom)
            nom = nom.replace(' ', '_').lower()
            return nom[:50]
    
    # Si no es troba cap títol, usar el prefix o 'document'
    if prefix:
        return prefix.lower().replace(' ', '_')
    return 'document'

def guardar_fitxer(contingut, extensio, carpeta_base, nom_base=None):
    """Guarda el contingut en un fitxer amb l'extensió i carpeta adequades."""
    carpeta = Path.cwd() / carpeta_base
    carpeta.mkdir(parents=True, exist_ok=True)
    
    # Generar un nom de fitxer si no es proporciona
    if nom_base is None:
        nom_base = extreure_nom_fitxer(contingut)
    
    # Netejar el nom final
    nom_net = re.sub(r'[^a-zA-Z0-9àèìòóúïü·\-_]', '', nom_base)
    fitxer = carpeta / f"{nom_net}.{extensio}"
    
    # Si el fitxer ja existeix, afegir un número
    counter = 1
    while fitxer.exists():
        fitxer = carpeta / f"{nom_net}_{counter}.{extensio}"
        counter += 1
    
    with open(fitxer, 'w', encoding='utf-8') as f:
        f.write(contingut)
    print(f"✅ Creat: {fitxer}")
    return True

def extreure_i_guardar_codi(resposta):
    """
    Extreu blocs de codi de la resposta i els guarda com a fitxers.
    També detecta HTML directe si no hi ha blocs.
    """
    # 1. Buscar blocs de codi: ```llenguatge \n ... \n ```
    patron = r'```(\w+)\n(.*?)\n```'
    blocs = re.findall(patron, resposta, re.DOTALL)
    
    fitxers_creats = 0
    
    if blocs:
        print(f"\n🔧 S'han trobat {len(blocs)} blocs de codi. Processant...")
        for i, (llenguatge, contingut) in enumerate(blocs, 1):
            llenguatge = llenguatge.lower().strip()
            print(f"\n📝 Processant bloc {i} (llenguatge: {llenguatge})...")
            
            # Intentar extreure un nom del contingut
            nom = extreure_nom_fitxer(contingut, prefix=f"bloc_{i}")
            
            if llenguatge not in LANGUAGE_MAP:
                print(f"⚠️ Llenguatge '{llenguatge}' no suportat. Es guardarà com a text.")
                extensio = 'txt'
                carpeta = 'content/raw'
            else:
                extensio, carpeta = LANGUAGE_MAP[llenguatge]
            
            try:
                guardar_fitxer(contingut, extensio, carpeta, nom)
                fitxers_creats += 1
            except Exception as e:
                print(f"❌ Error guardant el bloc {i}: {e}")
        
        if fitxers_creats > 0:
            print(f"✅ S'han creat {fitxers_creats} fitxers.")
            return True
        else:
            print("❌ No s'ha creat cap fitxer.")
            return False
    
    # 2. Si no hi ha blocs, buscar HTML directe
    html_match = re.search(r'(<!DOCTYPE html>|<html).*?</html>', resposta, re.DOTALL | re.IGNORECASE)
    if html_match:
        contingut_html = html_match.group(0)
        print("\n🔧 S'ha detectat HTML directe. Guardant...")
        nom = extreure_nom_fitxer(contingut_html, prefix="pagina")
        try:
            guardar_fitxer(contingut_html, 'html', 'content/html', nom)
            print("✅ HTML guardat.")
            return True
        except Exception as e:
            print(f"❌ Error guardant HTML directe: {e}")
            return False
    
    # 3. Si no hi ha res, retornar False
    print("ℹ️ No s'ha trobat cap bloc de codi ni HTML directe a la resposta.")
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["run", "init"])
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--model", default="deepseek")
    args = parser.parse_args()

    if args.command == "run":
        project_root = Path.cwd()
        context = load_project_context(project_root)
        task = detect_next_task(project_root)
        prompt = build_prompt(context, task)

        print("\n📋 PROMPT GENERAT:")
        print("=" * 60)
        print(prompt)
        print("=" * 60)

        executar = args.auto
        if not args.auto:
            resposta = input("\n❓ Vols executar aquesta tasca? (s/n): ").strip().lower()
            if resposta in ['s', 'si', 'y', 'yes']:
                executar = True
            else:
                print("⏹️ Execució cancel·lada.")
                return

        if executar:
            adapter = IAAdapter(model=args.model)
            response = adapter.query(prompt, context)
            if response:
                print("\n✅ RESPOSTA DE LA IA:")
                print(response)
                process_response(project_root, response)

                if extreure_i_guardar_codi(response):
                    marcar_tasca_completada(project_root, task)
                    print("✅ Tasca marcada com a completada a TODO.md")
                else:
                    print("⚠️ La tasca NO s'ha marcat com a completada perquè no s'ha generat cap fitxer.")
            else:
                print("❌ No s'ha rebut resposta de la IA.")
        else:
            print("⏹️ Execució cancel·lada.")

if __name__ == "__main__":
    main()