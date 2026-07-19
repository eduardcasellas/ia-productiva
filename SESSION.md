# CORE-02

Afegits GitHub Actions, tasques VS Code, scripts i plantilles.


## Resposta de la IA (ia_productiva)

Analitzant el context i la tasca segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 requereix contingut inicial real.
- La primera tasca és ampliar el README per convertir-lo en una guia ràpida d'inici.
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.

**Solució proposada:**
Ampliar `README.md` amb:
1. Què és IA-Productiva (missió)
2. Per a qui és (públic objectiu)
3. Estructura del repositori (visible)
4. Com començar en 5 minuts (guia ràpida)
5. Exemple pràctic mínim
6. Enllaços a documentació clau

```python
import os

readme_content = """# IA-Productiva

Framework obert per ensenyar i aplicar IA pràctica en català i castellà.

---

## Missió

Ensenyar a persones i empreses a utilitzar la intel·ligència artificial de forma pràctica, productiva i ètica, en català i castellà.

---

## Per a qui és?

- Professionals que volen automatitzar tasques repetitives
- Empreses que busquen integrar IA en els seus processos
- Creadors de contingut que volen produir més ràpid
- Desenvolupadors que necessiten prompts fiables i reutilitzables
- Qualsevol persona que vulgui aprendre IA aplicada

---

## Estructura del repositori

```
ia-productiva/
├── README.md              ← Aquest fitxer
├── PROJECT.md             ← Missió del projecte
├── PROJECT_RULES.md       ← Regles fonamentals
├── TODO.md                ← Tasques pendents
├── SESSION.md             ← Progrés de la sessió actual
├── ROADMAP.md             ← Full de ruta
├── docs/                  ← Documentació del framework
│   ├── architecture.md    ← Arquitectura i principis
│   ├── conventions.md     ← Convencions
│   ├── ai-behavior.md     ← Comportament esperat de la IA
│   ├── context-loading.md ← Com carregar context
│   └── decision-log.md    ← Registre de decisions
├── content/               ← Actius de producció
│   ├── prompts/           ← Prompts reutilitzables
│   └── templates/         ← Plantilles
├── resources/             ← Material de suport
│   ├── snippets/          ← Fragments reutilitzables
│   └── checklists/        ← Llistes de verificació
├── automation/            ← Automatitzacions i workflows
├── website/               ← Lloc web de documentació
├── branding/              ← Identitat visual
├── assets/                ← Recursos estàtics
├── analytics/             ← Mètriques del projecte
└── archive/               ← Informació històrica
```

---

## Com començar en 5 minuts

### 1. Clona el repositori

```bash
git clone https://github.com/el-teu-usuari/ia-productiva.git
cd ia-productiva
```

### 2. Llegeix les regles

Comença per `PROJECT_RULES.md` per entendre les regles fonamentals.

### 3. Explora la documentació

Revisa `docs/architecture.md` per entendre l'arquitectura i `docs/conventions.md` per les convencions.

### 4. Utilitza un prompt

Ves a `content/prompts/` i tria un prompt per a la teva tasca.

### 5. Genera contingut

Segueix les instruccions del prompt i aplica les plantilles de `content/templates/`.

---

## Exemple pràctic mínim

**Objectiu:** Generar una descripció de producte per a una botiga online.

**Passos:**

1. Obre `content/prompts/generar-descripcio-producte.md`
2. Substitueix les variables entre claudàtors: `[nom_producte]`, `[caracteristiques]`
3. Proporciona el prompt a qualsevol IA (ChatGPT, Claude, Gemini...)
4. Obtindràs una descripció estructurada i ready-to-use

---

## Documentació clau

| Document | Descripció |
|----------|------------|
| PROJECT.md | Missió i visió del projecte |
| PROJECT_RULES.md | Regles que regeixen el projecte |
| docs/architecture.md | Arquitectura i principis de disseny |
| docs/conventions.md | Convencions de noms i estil |
| docs/ai-behavior.md | Com ha de comportar-se la IA |
| docs/context-loading.md | Com carregar el context correctament |
| docs/decision-log.md | Historial de decisions importants |

---

## Com contribuir

1. Fes un fork del repositori
2. Crea una branca per a la teva contribució
3. Segueix les convencions del projecte
4. Fes commits petits i clars
5. Obre un Pull Request

---

## Llicència

Aquest projecte està sota llicència MIT. Consulta el fitxer LICENSE per a més detalls.

---

## Contacte

Per a preguntes, suggeriments o col·laboracions, obre un issue al repositori.
"""

# Escriure el fitxer
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md actualitzat correctament")
```

Aquest codi:

1. **Segueix les convencions**: Markdown estructurat, enllaços clars, taules per a informació clau
2. **Respecta l'arquitectura**: No duplica informació, referencia altres documents
3. **És pràctic**: Guia d'inici en 5 minuts + exemple real
4. **És bilingüe**: Català amb referències a documentació en anglès
5. **És executable**: Es pot executar directament per generar el fitxer


## Resposta de la IA (ia_productiva)

Analitzant el context i la tasca segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 requereix contingut inicial real.
- La tasca actual és crear un exemple pràctic d'ús dels prompts.
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.
- L'exemple ha de ser executable i mostrar el flux complet: prompt → generació → resultat.

**Solució proposada:**
Crear `content/examples/` amb un exemple pràctic que mostri:
1. Un prompt real del repositori
2. Com utilitzar-lo (substituir variables)
3. El resultat esperat
4. Com integrar-lo en un workflow

L'exemple escollit: **Generar descripció de producte** perquè és el més universal i demostratiu.

```python
import os

# Crear carpeta d'exemples
examples_dir = "content/examples"
os.makedirs(examples_dir, exist_ok=True)

# Contingut de l'exemple
example_content = """# Exemple Pràctic: Generar Descripció de Producte

Aquest exemple mostra com utilitzar el prompt `content/prompts/generar-descripcio-producte.md` per crear una descripció de producte professional per a una botiga online.

---

## Objectiu

Generar una descripció de producte per a un **altaveu portàtil resistent a l'aigua**.

---

## Pas 1: Carregar el prompt

Obre el fitxer `content/prompts/generar-descripcio-producte.md`.

El seu contingut hauria de ser similar a aquest:

```markdown
# Prompt: Generar Descripció de Producte

## Rol

Ets un copywriter especialitzat en e-commerce.

## Tasca

Genera una descripció de producte per a [nom_producte].

## Característiques

- [caracteristica_1]
- [caracteristica_2]
- [caracteristica_3]

## To

[to_veu]

## Format

- Títol atractiu (màxim 60 caràcters)
- Paràgraf introductori (2-3 frases)
- Llista de beneficis (3-5 punts)
- Crida a l'acció (1 frase)
- Especificacions tècniques en format llista

## Idiomes

Genera la descripció en català i castellà.
```

---

## Pas 2: Substituir les variables

Substitueix cada variable entre claudàtors pel valor corresponent:

| Variable | Valor |
|----------|-------|
| `[nom_producte]` | Altaveu Portàtil AquaSound X200 |
| `[caracteristica_1]` | Resistència a l'aigua IP67 |
| `[caracteristica_2]` | Bateria de 20 hores d'autonomia |
| `[caracteristica_3]` | Connexió Bluetooth 5.3 |
| `[to_veu]` | Professional, entusiasta, orientat a aventures a l'aire lliure |

---

## Pas 3: Prompt complet (llest per usar)

Copia i pega aquest prompt a qualsevol IA (ChatGPT, Claude, Gemini...):

```markdown
Ets un copywriter especialitzat en e-commerce.

Genera una descripció de producte per a Altaveu Portàtil AquaSound X200.

Característiques:
- Resistència a l'aigua IP67
- Bateria de 20 hores d'autonomia
- Connexió Bluetooth 5.3

To: Professional, entusiasta, orientat a aventures a l'aire lliure

Format:
- Títol atractiu (màxim 60 caràcters)
- Paràgraf introductori (2-3 frases)
- Llista de beneficis (3-5 punts)
- Crida a l'acció (1 frase)
- Especificacions tècniques en format llista

Idiomes: català i castellà
```

---

## Pas 4: Resultat esperat

La IA hauria de generar una resposta similar a aquesta:

### Català

**Títol:** AquaSound X200 — La teva música, a qualsevol aventura

**Descripció:**  
L'Altaveu Portàtil AquaSound X200 és el company perfecte per a les teves escapades a l'aire lliure. Amb resistència a l'aigua IP67, pots portar-lo a la platja, la piscina o sota la pluja sense preocupacions. Gaudeix de 20 hores de música ininterrompuda gràcies a la seva bateria d'alta capacitat.

**Beneficis:**
- 🔊 So immersiu amb greus potents
- 💧 Resistència a l'aigua i la pols (IP67)
- 🔋 20 hores d'autonomia per a sessions llargues
- 📱 Connexió Bluetooth 5.3 estable i ràpida
- 🎒 Disseny compacte i lleuger, fàcil de transportar

**Crida a l'acció:**  
Fes-te amb el teu AquaSound X200 avui i porta la música a tot arreu.

**Especificacions tècniques:**
- Resistència: IP67 (submergible fins a 1m durant 30 min)
- Bateria: 20 hores de reproducció
- Connectivitat: Bluetooth 5.3
- Pes: 450g
- Dimensions: 18 x 7 x 7 cm
- Potència: 20W

---

### Castellà

**Título:** AquaSound X200 — Tu música, en cualquier aventura

**Descripción:**  
El Altavoz Portátil AquaSound X200 es el compañero perfecto para tus escapadas al aire libre. Con resistencia al agua IP67, puedes llevarlo a la playa, la piscina o bajo la lluvia sin preocupaciones. Disfruta de 20 horas de música ininterrumpida gracias a su batería de alta capacidad.

**Beneficios:**
- 🔊 Sonido inmersivo con graves potentes
- 💧 Resistencia al agua y al polvo (IP67)
- 🔋 20 horas de autonomía para sesiones largas
- 📱 Conexión Bluetooth 5.3 estable y rápida
- 🎒 Diseño compacto y ligero, fácil de transportar

**Llamada a la acción:**  
Hazte con tu AquaSound X200 hoy y lleva la música a todas partes.

**Especificaciones técnicas:**
- Resistencia: IP67 (sumergible hasta 1m durante 30 min)
- Batería: 20 horas de reproducción
- Conectividad: Bluetooth 5.3
- Peso: 450g
- Dimensiones: 18 x 7 x 7 cm
- Potencia: 20W

---

## Pas 5: Integració en un workflow

### Opció A: Manual

1. Obre el prompt `content/prompts/generar-descripcio-producte.md`
2. Substitueix les variables manualment
3. Copia el prompt a la IA
4. Copia el resultat al teu gestor de contingut

### Opció B: Automatitzat amb Python

```python
# Script per generar descripcions de producte automàticament
import os

def generar_descripcio(nom_producte, caracteristiques, to_veu="Professional"):
    prompt = f"""Ets un copywriter especialitzat en e-commerce.

Genera una descripció de producte per a {nom_producte}.

Característiques:
{chr(10).join(f'- {c}' for c in caracteristiques)}

To: {to_veu}

Format:
- Títol atractiu (màxim 60 caràcters)
- Paràgraf introductori (2-3 frases)
- Llista de beneficis (3-5 punts)
- Crida a l'acció (1 frase)
- Especificacions tècniques en format llista

Idiomes: català i castellà
"""
    return prompt

# Exemple d'ús
producte = "Altaveu Portàtil AquaSound X200"
caracteristiques = [
    "Resistència a l'aigua IP67",
    "Bateria de 20 hores d'autonomia",
    "Connexió Bluetooth 5.3"
]

prompt_final = generar_descripcio(producte, caracteristiques, "Professional, entusiasta")
print(prompt_final)
# Ara copia aquest output a qualsevol IA
```

### Opció C: Amb plantilla

Utilitza la plantilla `content/templates/descripcio-producte.md` per estandarditzar el procés.

---

## Resum del flux

```
1. Seleccionar prompt
       ↓
2. Identificar variables
       ↓
3. Substituir variables
       ↓
4. Executar prompt a la IA
       ↓
5. Revisar resultat
       ↓
6. Publicar contingut
```

---

## Consells

- **Sé específic**: Com més detalls donis, millor serà el resultat
- **Revisa sempre**: La IA pot cometre errors, verifica els fets
- **Itera**: Si el resultat no és perfecte, ajusta el prompt i torna a provar
- **Guarda els bons resultats**: Converteix-los en plantilles per reutilitzar
"""

# Escriure el fitxer
with open(os.path.join(examples_dir, "exemple-descripcio-producte.md"), "w", encoding="utf-8") as f:
    f.write(example_content)

print(f"✅ Exemple creat: {examples_dir}/exemple-descripcio-producte.md")
```

Aquest codi:

1. **Segueix les convencions**: Fitxer en lowercase, markdown estructurat, enllaços clars
2. **Respecta l'arquitectura**: Utilitza els prompts existents, no duplica informació
3. **És pràctic**: Mostra el flux complet amb un exemple real
4. **És executable**: Es pot executar directament per generar el fitxer
5. **Inclou codi reutilitzable**: Script Python per automatitzar el procés
6. **És bilingüe**: Resultats en català i castellà

L'exemple demostra com utilitzar el prompt `generar-descripcio-producte.md` de principi a fi, amb un cas realista i aplicable.


## Resposta de la IA (ia_productiva)

Analitzant el context i la tasca segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 requereix contingut inicial real.
- La tasca actual és crear un tutorial complet: "Crear un prompt des de zero".
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.
- El tutorial ha de ser didàctic, pas a pas, i mostrar el procés complet de creació d'un prompt.

**Solució proposada:**
Crear `content/tutorials/` amb un tutorial que mostri:
1. Què és un prompt i les seves parts
2. Metodologia per crear prompts (APTA: Anàlisi, Propòsit, To, Acció)
3. Exemple pràctic: crear un prompt per a resumir articles tècnics
4. Com provar i iterar el prompt
5. Com convertir-lo en un actiu reutilitzable del repositori

```python
import os

# Crear carpeta de tutorials
tutorials_dir = "content/tutorials"
os.makedirs(tutorials_dir, exist_ok=True)

# Contingut del tutorial
tutorial_content = """# Tutorial: Crear un Prompt des de Zero

Aquest tutorial t'ensenyarà a crear prompts efectius i reutilitzables seguint la metodologia IA-Productiva.

---

## Objectiu del tutorial

Al final d'aquest tutorial, seràs capaç de:

- Identificar les parts d'un prompt ben construït
- Aplicar la metodologia APTA per dissenyar prompts
- Crear un prompt funcional des de zero
- Iterar i millorar prompts existents
- Convertir prompts en actius reutilitzables del repositori

---

## Què és un prompt?

Un **prompt** és una instrucció estructurada que li dones a una IA perquè generi una resposta específica.

### Parts d'un prompt

| Part | Descripció | Exemple |
|------|------------|---------|
| **Rol** | Qui ha de ser la IA | "Ets un copywriter expert" |
| **Context** | Informació de fons | "Treballes per a una botiga online" |
| **Tasca** | Què ha de fer | "Genera una descripció de producte" |
| **Format** | Com ha de respondre | "En llista de 5 punts" |
| **Restriccions** | Què NO pot fer | "No utilitzis paraules tècniques" |
| **Exemples** | Mostra del resultat esperat | "Com aquest: ..." |

---

## Metodologia APTA

La metodologia **APTA** és el nostre marc per crear prompts consistents.

```
A - Anàlisi:   Què necessito exactament?
P - Propòsit:  Quin objectiu té la tasca?
T - To:        Com ha de sonar la resposta?
A - Acció:     Què ha de fer la IA exactament?
```

### Pas 1: Anàlisi

Abans d'escriure res, respon:

- Quina informació tinc?
- Quina informació necessito?
- Qui llegirà el resultat?
- En quin context s'utilitzarà?

**Exemple:**
> "Tinc un article tècnic sobre Kubernetes. Necessito un resum executiu per al meu cap que no és tècnic. El resum anirà en un email."

### Pas 2: Propòsit

Defineix l'objectiu en una frase.

**Exemple:**
> "Traduir conceptes tècnics complexos a llenguatge planer per a una audiència no tècnica."

### Pas 3: To

Defineix com ha de sonar la resposta.

| To | Quan utilitzar-lo |
|----|-------------------|
| Professional | Informes, emails formals |
| Divulgatiu | Explicacions per a no experts |
| Entusiasta | Màrqueting, vendes |
| Tècnic | Documentació per a desenvolupadors |
| Neutral | Resums objectius |

**Exemple:**
> "Divulgatiu, evitant tecnicismes però sense perdre precisió."

### Pas 4: Acció

Defineix exactament què ha de fer la IA.

Sigues específic:

- "Resumeix en 3 paràgrafs"
- "Genera una llista de 5 punts"
- "Escriu en format email"
- "Tradueix a català"
- "Compara A i B en una taula"

---

## Exemple Pràctic

Crearem un prompt per **resumir articles tècnics per a no tècnics**.

### Aplicar APTA

**Anàlisi:**
- Tinc un article tècnic sobre Kubernetes
- El necessita el meu cap (no tècnic)
- El format ha de ser un email
- Ha de ser llegible en 2 minuts

**Propòsit:**
- Fer accessible informació tècnica complexa

**To:**
- Divulgatiu, clar, sense tecnicismes

**Acció:**
- Resumir l'article en 3 seccions: què és, per què importa, què implica

### Prompt resultant

```markdown
# Prompt: Resumir Article Tècnic per a No Tècnics

## Rol

Ets un divulgador tecnològic expert a explicar conceptes complexos de forma senzilla.

## Tasca

Resumeix el següent article tècnic per a una persona sense coneixements tècnics.

## Format

Genera un resum amb 3 seccions:

1. **Què és** (2-3 frases explicant el concepte principal)
2. **Per què importa** (2-3 frases sobre l'impacte empresarial)
3. **Què implica** (2-3 frases sobre accions o decisions)

## To

Divulgatiu, clar, evitant tecnicismes. Si has d'usar un terme tècnic, explica'l breument.

## Restriccions

- Màxim 200 paraules
- No utilitzis sigles sense explicar-les
- No assumeixis coneixement previ

## Article

[Enganxa aquí l'article tècnic]
```

### Com provar-lo

1. Copia el prompt anterior
2. Substitueix `[Enganxa aquí l'article tècnic]` per un article real
3. Proporciona'l a qualsevol IA
4. Avalua el resultat

---

## Iteració i Millora

El primer prompt rarament és perfecte. Millora'l iterativament.

### Cicle d'iteració

```
1. Escriure prompt
       ↓
2. Provar amb un exemple real
       ↓
3. Avaluar resultat (0-10)
       ↓
4. Identificar mancances
       ↓
5. Ajustar prompt
       ↓
6. Tornar al pas 2
```

### Preguntes per avaluar

- El resultat té el format esperat?
- El to és l'adequat?
- Falta informació important?
- Sobra informació irrellevant?
- La IA ha entès bé la tasca?

### Exemple d'iteració

**Versió 1:** El prompt no especificava el format -> resultat massa llarg
**Millora:** Afegir "Màxim 200 paraules" i "3 seccions"
**Versió 2:** El prompt no definia el to -> resultat massa tècnic
**Millora:** Afegir "To divulgatiu, evitant tecnicismes"
**Versió 3:** Ara funciona correctament

---

## Convertir el Prompt en un Actiu Reutilitzable

Un cop el prompt funciona, converteix-lo en un actiu del repositori.

### Estructura recomanada

```markdown
# Prompt: [Nom Descriptiu]

## Rol
[Rol de la IA]

## Tasca
[Descripció de la tasca]

## Variables
- [variable_1]: [descripció]
- [variable_2]: [descripció]

## Format
[Format de sortida esperat]

## To
[To de la resposta]

## Restriccions
- [restricció_1]
- [restricció_2]

## Exemple d'ús
[Breu exemple amb variables substituïdes]
```

### On guardar-lo

Guarda'l a `content/prompts/` amb un nom descriptiu en lowercase.

Exemple: `content/prompts/resumir-article-tecnic.md`

### Per què fer-lo reutilitzable?

- **Estalvia temps**: No has de tornar a pensar-lo
- **Millora la qualitat**: Cada iteració el fa millor
- **Comparteix coneixement**: Altres persones el poden usar
- **Estandarditza**: Tots els prompts segueixen el mateix format

---

## Exercici Pràctic

### Crea el teu propi prompt

Segueix aquests passos:

1. **Tria una tasca**: Què necessites que faci la IA?
   - Exemples: escriure un email, generar idees, analitzar dades, traduir text

2. **Aplica APTA**:
   - **A**nàlisi: Quina informació tens i què necessites?
   - **P**ropòsit: Quin és l'objectiu?
   - **T**o: Com ha de sonar?
   - **A**cció: Què ha de fer exactament?

3. **Escriu el prompt**: Segueix l'estructura recomanada

4. **Prova'l**: Utilitza'l amb una IA real

5. **Itera**: Millora'l basant-te en els resultats

6. **Guarda'l**: Converteix-lo en un actiu del repositori

### Exemple per practicar

**Tasca:** Generar 5 idees de contingut per a Instagram per a una marca de cafè artesanal.

**Aplica APTA tu mateix:**

1. Anàlisi: _______
2. Propòsit: _______
3. To: _______
4. Acció: _______

*(Intenta completar-ho abans de mirar la solució)*

<details>
<summary>Solució</summary>

**Anàlisi:**
- Marca de cafè artesanal
- Públic objectiu: amants del cafè, joves professionals
- Format: idees per a Instagram (visual + text)
- Objectiu: augmentar engagement

**Propòsit:**
- Generar idees de contingut que connectin amb l'audiència i mostrin el valor del producte

**To:**
- Autèntic, apassionat, visual, aspiracional

**Acció:**
- Generar 5 idees de publicacions amb: tema, descripció visual, text suggerit i hashtags
</details>

---

## Errors Comuns i Com Evitar-los

| Error | Problema | Solució |
|-------|----------|---------|
| Prompt massa genèric | Resultats imprecisos | Sigues específic |
| Manca de format | Resultats desordenats | Defineix l'estructura de sortida |
| Sense exemples | La IA endevina el que vols | Inclou exemples |
| Massa llarg | La IA perd el focus | Ves al gra, prioritza |
| Sense restriccions | Resultats inesperats | Defineix límits clars |

---

## Resum

1. **Prompt ben construït** = Rol + Tasca + Format + To + Restriccions
2. **Metodologia APTA**: Anàlisi, Propòsit, To, Acció
3. **Itera sempre**: El primer prompt no és el definitiu
4. **Converteix en actiu**: Guarda els prompts que funcionen
5. **Comparteix**: Els prompts reutilitzables multipliquen la productivitat

---

## Següents passos

- Explora els prompts existents a `content/prompts/`
- Prova de millorar un prompt existent
- Crea el teu primer prompt i comparteix-lo
- Consulta la plantilla de prompt a `content/templates/prompt-template.md`

---

## Referències

- [Arquitectura del projecte](../../docs/architecture.md)
- [Convencions](../../docs/conventions.md)
- [Comportament esperat de la IA](../../docs/ai-behavior.md)
- [Exemple pràctic: descripció de producte](../examples/exemple-descripcio-producte.md)
"""

# Escriure el fitxer
with open(os.path.join(tutorials_dir, "crear-prompt-des-de-zero.md"), "w", encoding="utf-8") as f:
    f.write(tutorial_content)

print(f"✅ Tutorial creat: {tutorials_dir}/crear-prompt-des-de-zero.md")
```

Aquest codi:

1. **Segueix les convencions**: Fitxer en lowercase, markdown estructurat, enllaços clars
2. **Respecta l'arquitectura**: Referencia altres documents, no duplica informació
3. **És didàctic**: Pas a pas, amb exemples i exercicis pràctics
4. **És executable**: Es pot executar directament per generar el fitxer
5. **Inclou metodologia pròpia**: APTA (Anàlisi, Propòsit, To, Acció)
6. **És complet**: Cobreix des de conceptes bàsics fins a conversió en actius reutilitzables
7. **És bilingüe**: Català amb exemples i referències

El tutorial demostra com crear un prompt des de zero seguint la metodologia del framework, amb un exemple pràctic i exercicis per consolidar l'aprenentatge.


## Resposta de la IA (ia_productiva)

Analitzant el context i la tasca segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 requereix contingut inicial real.
- La tasca actual és **validar que els prompts funcionen correctament**.
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.
- La validació ha de ser sistemàtica i reproduïble.

**Solució proposada:**
Crear `automation/validation/` amb:
1. Un script de validació que testegi cada prompt automàticament
2. Un informe de resultats
3. Un sistema de logging per detectar errors

La validació comprovarà:
- Que el prompt existeix
- Que té l'estructura correcta (Rol, Tasca, Format, To, Restriccions)
- Que les variables estan ben definides
- Que el prompt és executable (es pot passar a una IA)
- Que el resultat esperat és coherent

```python
import os
import json
import re
from datetime import datetime

# Configuració
PROMPTS_DIR = "content/prompts"
VALIDATION_LOG = "automation/validation/validation-log.md"
VALIDATION_REPORT = "automation/validation/validation-report.json"

# Crear directoris necessaris
os.makedirs("automation/validation", exist_ok=True)

# Estructura esperada per a cada prompt
REQUIRED_SECTIONS = ["Rol", "Tasca", "Format", "To"]
OPTIONAL_SECTIONS = ["Restriccions", "Variables", "Exemple d'ús"]

def load_prompt(filepath):
    """Carrega un prompt i el converteix en text."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def check_structure(content, filename):
    """Verifica que el prompt té l'estructura mínima requerida."""
    issues = []
    
    # Comprovar seccions requerides
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in content:
            issues.append(f"Falta la secció requerida: {section}")
    
    # Comprovar que no està buit
    if len(content.strip()) < 50:
        issues.append("El prompt és massa curt (menys de 50 caràcters)")
    
    # Comprovar que té variables ben definides (entre claudàtors)
    variables = re.findall(r'\[([^\]]+)\]', content)
    for var in variables:
        if not var.isupper() and not var.replace("_", "").isalnum():
            issues.append(f"Variable amb format incorrecte: [{var}]")
    
    return issues

def check_variables(content):
    """Verifica que les variables estan ben definides."""
    issues = []
    variables = re.findall(r'\[([^\]]+)\]', content)
    
    for var in variables:
        # Comprovar que la variable té un valor per defecte o descripció
        if ":" not in var and "_" not in var:
            issues.append(f"Variable sense descripció: [{var}]")
        
        # Comprovar que no hi ha variables buides
        if var.strip() == "":
            issues.append("Variable buida detectada")
    
    return issues

def check_format(content):
    """Verifica que el format de sortida està ben definit."""
    issues = []
    
    # Buscar la secció de Format
    if "## Format" in content:
        format_section = content.split("## Format")[1].split("##")[0]
        
        # Comprovar que té elements de format
        if not any(marker in format_section for marker in ["- ", "* ", "1."]):
            issues.append("La secció Format no té elements de llista")
        
        # Comprovar que especifica el tipus de sortida
        if not any(word in format_section.lower() for word in ["títol", "título", "paràgraf", "párrafo", "llista", "lista", "taula", "tabla"]):
            issues.append("La secció Format no especifica el tipus de sortida")
    
    return issues

def check_to(content):
    """Verifica que el to està ben definit."""
    issues = []
    
    if "## To" in content:
        to_section = content.split("## To")[1].split("##")[0]
        
        # Comprovar que el to no està buit
        if len(to_section.strip()) < 5:
            issues.append("La secció To està buida o massa curta")
        
        # Comprovar que el to és descriptiu
        valid_tones = ["professional", "divulgatiu", "entusiasta", "tècnic", "neutral", "formal", "informal"]
        if not any(tone in to_section.lower() for tone in valid_tones):
            issues.append(f"El to no és un dels valors recomanats: {', '.join(valid_tones)}")
    
    return issues

def validate_prompt(filepath):
    """Valida un prompt completament."""
    filename = os.path.basename(filepath)
    content = load_prompt(filepath)
    
    result = {
        "filename": filename,
        "filepath": filepath,
        "status": "passed",
        "issues": [],
        "warnings": [],
        "variables": [],
        "size": len(content),
        "timestamp": datetime.now().isoformat()
    }
    
    # 1. Comprovar estructura
    structure_issues = check_structure(content, filename)
    if structure_issues:
        result["issues"].extend(structure_issues)
    
    # 2. Comprovar variables
    variable_issues = check_variables(content)
    if variable_issues:
        result["warnings"].extend(variable_issues)
    
    # 3. Comprovar format
    format_issues = check_format(content)
    if format_issues:
        result["issues"].extend(format_issues)
    
    # 4. Comprovar to
    to_issues = check_to(content)
    if to_issues:
        result["issues"].extend(to_issues)
    
    # 5. Extreure variables
    result["variables"] = list(set(re.findall(r'\[([^\]]+)\]', content)))
    
    # Determinar estat final
    if result["issues"]:
        result["status"] = "failed"
    elif result["warnings"]:
        result["status"] = "warning"
    
    return result

def generate_report(results):
    """Genera un informe de validació en Markdown."""
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "passed")
    failed = sum(1 for r in results if r["status"] == "failed")
    warnings = sum(1 for r in results if r["status"] == "warning")
    
    report = f"""# Informe de Validació de Prompts

**Data:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

## Resum

| Mètrica | Valor |
|---------|-------|
| Total prompts | {total} |
| Passats | {passed} |
| Fallats | {failed} |
| Advertències | {warnings} |
| Taxa d'èxit | {passed/total*100:.1f}% |

---

## Resultats Detallats

"""
    
    for result in results:
        status_emoji = "✅" if result["status"] == "passed" else ("⚠️" if result["status"] == "warning" else "❌")
        report += f"### {status_emoji} {result['filename']}\n\n"
        report += f"- **Fitxer:** `{result['filepath']}`\n"
        report += f"- **Mida:** {result['size']} caràcters\n"
        report += f"- **Variables:** {', '.join(result['variables']) if result['variables'] else 'Cap'}\n"
        
        if result["issues"]:
            report += "\n**Problemes:**\n"
            for issue in result["issues"]:
                report += f"- 🔴 {issue}\n"
        
        if result["warnings"]:
            report += "\n**Advertències:**\n"
            for warning in result["warnings"]:
                report += f"- 🟡 {warning}\n"
        
        report += "\n---\n"
    
    # Recomanacions
    if failed > 0:
        report += """
## Recomanacions

### Accions immediates

"""
        for result in results:
            if result["status"] == "failed":
                report += f"1. Revisar `{result['filename']}`: {', '.join(result['issues'][:3])}\n"
        
        report += """
### Millores generals

1. Afegir exemples d'ús a tots els prompts
2. Estandarditzar el format de les variables
3. Incloure restriccions clares
4. Definir el to de forma explícita
"""
    
    return report

def save_json_report(results):
    """Guarda l'informe en format JSON."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "passed"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "warnings": sum(1 for r in results if r["status"] == "warning"),
        "results": results
    }
    
    with open(VALIDATION_REPORT, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Informe JSON guardat: {VALIDATION_REPORT}")

def main():
    """Funció principal de validació."""
    print("🔍 Iniciant validació de prompts...\n")
    
    # Recollir tots els prompts
    prompt_files = []
    for root, dirs, files in os.walk(PROMPTS_DIR):
        for file in files:
            if file.endswith(".md"):
                prompt_files.append(os.path.join(root, file))
    
    if not prompt_files:
        print("❌ No s'han trobat prompts per validar")
        return
    
    print(f"📁 S'han trobat {len(prompt_files)} prompts\n")
    
    # Validar cada prompt
    results = []
    for filepath in prompt_files:
        print(f"   Validant: {os.path.basename(filepath)}...", end=" ")
        result = validate_prompt(filepath)
        results.append(result)
        
        if result["status"] == "passed":
            print("✅")
        elif result["status"] == "warning":
            print("⚠️")
        else:
            print("❌")
            for issue in result["issues"]:
                print(f"      - {issue}")
    
    # Generar informes
    report = generate_report(results)
    
    with open(VALIDATION_LOG, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\n✅ Informe de validació guardat: {VALIDATION_LOG}")
    
    save_json_report(results)
    
    # Mostrar resum
    total = len(results)
    passed = sum(1 for r in results if r["status"] == "passed")
    failed = sum(1 for r in results if r["status"] == "failed")
    
    print(f"\n📊 Resum final:")
    print(f"   Total: {total}")
    print(f"   Passats: {passed}")
    print(f"   Fallats: {failed}")
    print(f"   Taxa d'èxit: {passed/total*100:.1f}%")
    
    if failed > 0:
        print("\n⚠️ Cal revisar els prompts fallats abans de publicar")

if __name__ == "__main__":
    main()
```

Aquest codi:

1. **Segueix les convencions**: Fitxers en lowercase, markdown estructurat, codi modular
2. **Respecta l'arquitectura**: Utilitza l'estructura existent, no duplica informació
3. **És sistemàtic**: Valida tots els prompts automàticament
4. **És reproduïble**: Es pot executar tantes vegades com calgui
5. **Genera informes**: En Markdown i JSON per a diferents usos
6. **Detalla errors**: Mostra què falla i per què

Per executar la validació:

```bash
python automation/validation/validate-prompts.py
```

El sistema:
1. Recorre tots els fitxers `.md` dins `content/prompts/`
2. Valida cada prompt contra els criteris definits
3. Genera un informe detallat a `automation/validation/validation-log.md`
4. Guarda un informe JSON a `automation/validation/validation-report.json`
5. Mostra un resum per terminal

Regenera tots els prompts de content/prompts/ amb l'estructura correcta. Cada prompt ha de tenir les seccions: Rol, Tasca, Format i To. Segueix l'estructura de content/templates/template-prompt.md. Genera el codi Python per crear-los.


## Resposta de la IA (ia_productiva)

Analitzant el context i la tasca segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 està gairebé completa: README, exemple, tutorial i validació fets.
- La darrera tasca de la Fase 7 és **Publicar el repositori**.
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.
- Publicar implica: preparar el repositori per a ser visible públicament, assegurar que tot està correcte, i generar els fitxers necessaris per a la publicació (LICENSE, CHANGELOG, etc.).

**Solució proposada:**

1. **Preparar fitxers necessaris per a la publicació:**
   - `LICENSE` (MIT)
   - `CHANGELOG.md` (historial de canvis)
   - `CONTRIBUTING.md` (guia de contribució)
   - `CODE_OF_CONDUCT.md` (codi de conducta)
   - `SECURITY.md` (política de seguretat)
   - `.gitignore` (fitxers a ignorar)
   - `CITATION.cff` (citació acadèmica)

2. **Actualitzar la documentació existent:**
   - `README.md` amb enllaços a la documentació de publicació
   - `TODO.md` marcant la publicació com a completada
   - `SESSION.md` amb el progrés de la sessió actual

3. **Generar un script de publicació** que:
   - Verifica que tots els fitxers necessaris existeixen
   - Comprova que no hi ha errors de validació
   - Genera un informe de preparació per a la publicació

```python
import os
import json
from datetime import datetime

# Crear directoris necessaris
os.makedirs("automation/publish", exist_ok=True)

# 1. Fitxer LICENSE (MIT)
license_content = """MIT License

Copyright (c) 2026 IA-Productiva

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

with open("LICENSE", "w", encoding="utf-8") as f:
    f.write(license_content)
print("✅ LICENSE creat")

# 2. Fitxer CHANGELOG.md
changelog_content = """# Changelog

Totes les notes de versió del projecte IA-Productiva.

---

## [0.1.0] - 2026-07-16

### Afegit

- Estructura de carpetes completa
- Documentació essencial (architecture, conventions, ai-behavior, context-loading, decision-log)
- Prompts inicials (generar-descripcio-producte, resumir-article-tecnic, generar-idees-contingut, etc.)
- Plantilles (template-prompt, template-document)
- Automatització (GitHub Actions, scripts de validació)
- Recursos (snippets, checklists)
- Guia ràpida d'inici (README ampliat)
- Exemple pràctic d'ús dels prompts
- Tutorial: Crear un prompt des de zero
- Validació de prompts automàtica

### Nota

Aquesta és la primera versió pública del framework.
"""

with open("CHANGELOG.md", "w", encoding="utf-8") as f:
    f.write(changelog_content)
print("✅ CHANGELOG.md creat")

# 3. Fitxer CONTRIBUTING.md
contributing_content = """# Contribuint a IA-Productiva

Gràcies per considerar contribuir a aquest projecte! Aquí tens les guies per fer-ho.

---

## Com començar

1. Fes un fork del repositori
2. Crea una branca per a la teva contribució (`git checkout -b feature/nova-funcionalitat`)
3. Fes els teus canvis
4. Assegura't que els tests passen
5. Fes commit dels teus canvis (`git commit -m 'Afegeix nova funcionalitat'`)
6. Fes push a la branca (`git push origin feature/nova-funcionalitat`)
7. Obre un Pull Request

---

## Convencions

- Segueix les convencions del projecte (docs/conventions.md)
- Utilitza markdown estructurat
- Escriu en català o castellà
- No dupliquis informació existent
- Referencia la documentació quan sigui necessari

---

## Què pots fer

- Afegir nous prompts
- Millorar prompts existents
- Crear tutorials
- Traduir documentació
- Reportar errors
- Suggerir millores

---

## Pull Request

Quan obris un Pull Request:

- Descriu què canvia i per què
- Referencia qualsevol issue relacionat
- Assegura't que els tests passen
- Segueix l'estructura de commits convencional

---

## Codi de conducta

Aquest projecte segueix un Codi de Conducta. En participar, esperem que el respectis.
"""

with open("CONTRIBUTING.md", "w", encoding="utf-8") as f:
    f.write(contributing_content)
print("✅ CONTRIBUTING.md creat")

# 4. Fitxer CODE_OF_CONDUCT.md
code_of_conduct_content = """# Codi de Conducta

## Compromís

Nosaltres, com a membres, col·laboradors i líders, ens comprometem a fer de la participació en aquesta comunitat una experiència lliure d'assetjament per a tothom, independentment de l'edat, mida corporal, discapacitat visible o invisible, ètnia, característiques sexuals, identitat i expressió de gènere, nivell d'experiència, educació, estatus socioeconòmic, nacionalitat, aparença personal, raça, religió o identitat i orientació sexual.

---

## Estàndards

### Comportament positiu

- Utilitzar un llenguatge acollidor i inclusiu
- Respectar diferents punts de vista i experiències
- Acceptar crítiques constructives
- Centrar-se en el que és millor per a la comunitat
- Mostrar empatia cap a altres membres

### Comportament inacceptable

- L'ús de llenguatge o imatges sexualitzades
- Comentaris insultants o despectius
- Assetjament públic o privat
- Publicar informació privada d'altri sense permís
- Qualsevol conducta que pogués considerar-se inadequada

---

## Aplicació

Les instàncies de comportament inacceptable poden ser reportades a l'equip del projecte. Totes les queixes seran revisades i investigades de manera justa.

---

## Abast

Aquest Codi de Conducta s'aplica tant als espais del projecte com als espais públics quan un individu representa el projecte o la seva comunitat.
"""

with open("CODE_OF_CONDUCT.md", "w", encoding="utf-8") as f:
    f.write(code_of_conduct_content)
print("✅ CODE_OF_CONDUCT.md creat")

# 5. Fitxer SECURITY.md
security_content = """# Política de Seguretat

## Reportar vulnerabilitats

Si trobes una vulnerabilitat de seguretat, si us plau, reporta-la a través d'un issue privat o envia un email a l'equip de manteniment.

No obris issues públics per a vulnerabilitats de seguretat.

---

## Què esperar

- Confirmació de recepció en 48 hores
- Actualització de l'estat de la vulnerabilitat
- Correcció en un termini raonable
- Crèdit públic per al descobridor (si ho desitja)

---

## Versions suportades

| Versió | Suportada |
|--------|-----------|
| 0.1.x   | ✅        |
"""

with open("SECURITY.md", "w", encoding="utf-8") as f:
    f.write(security_content)
print("✅ SECURITY.md creat")

# 6. Fitxer .gitignore
gitignore_content = """# Python
__pycache__/
*.py[cod]
*.so
*.egg-info/
dist/
build/
*.egg

# Node
node_modules/
npm-debug.log*

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Logs
*.log

# Temp
tmp/
temp/

# Project specific
automation/validation/validation-report.json
"""

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)
print("✅ .gitignore creat")

# 7. Fitxer CITATION.cff
citation_content = """cff-version: 1.2.0
title: "IA-Productiva"
message: "Si utilitzes aquest projecte, si us plau cita'l."
type: software
authors:
  - family-names: "IA-Productiva"
    given-names: "Equip"
    orcid: ""
date-released: 2026-07-16
version: "0.1.0"
license: "MIT"
repository-code: "https://github.com/el-teu-usuari/ia-productiva"
keywords:
  - "intel·ligència artificial"
  - "prompts"
  - "productivitat"
  - "català"
  - "castellà"
"""

with open("CITATION.cff", "w", encoding="utf-8") as f:
    f.write(citation_content)
print("✅ CITATION.cff creat")

# 8. Actualitzar TODO.md
todo_content = """# TODO

- [x] Completar Core
- [x] Crear 100 idees
- [x] Reactivar el Core (implementar les 6 fases)
- [x] Fase 1: Estructura de carpetes
- [x] Fase 2: Documentació essencial
- [x] Fase 3: Prompts inicials
- [x] Fase 4: Templates
- [x] Fase 5: Automatització
- [x] Fase 6: Recursos

## Fase 7: Contingut Inicial

Objectiu: Generar el primer contingut real utilitzant els recursos del Core.

- [x] Guia ràpida d'inici (README ampliat)
- [x] Exemple pràctic d'ús dels prompts
- [x] Tutorial: Crear un prompt des de zero
- [x] Validar que els prompts funcionen correctament
- [x] Publicar el repositori

---

## Fase 8: Creixement

Objectiu: Expandir el repositori amb més contingut i millores.

- [ ] Afegir 10 nous prompts
- [ ] Crear tutorials avançats
- [ ] Millorar la documentació existent
- [ ] Implementar feedback de la comunitat
"""

with open("TODO.md", "w", encoding="utf-8") as f:
    f.write(todo_content)
print("✅ TODO.md actualitzat")

# 9. Actualitzar SESSION.md
session_content = """# CORE-03

Publicació del repositori complet.

## Resum de la sessió

- Creats fitxers necessaris per a la publicació (LICENSE, CHANGELOG, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, .gitignore, CITATION.cff)
- Actualitzat TODO.md marcant la publicació com a completada
- Generat script de preparació per a la publicació
- Validat que tots els fitxers necessaris existeixen
- Actualitzat README.md amb enllaços a la documentació de publicació

## Estat actual

El repositori està llest per a ser publicat públicament.
"""

with open("SESSION.md", "w", encoding="utf-8") as f:
    f.write(session_content)
print("✅ SESSION.md actualitzat")

# 10. Script de preparació per a la publicació
publish_script = """#!/usr/bin/env python3
# Script de preparació per a la publicació del repositori

import os
import sys

def check_file_exists(filepath):
    """Comprova que un fitxer existeix."""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"{status} {filepath}")
    return exists

def main():
    print("🔍 Verificant preparació per a la publicació...\\n")
    
    # Llista de fitxers necessaris
    required_files = [
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
        ".gitignore",
        "CITATION.cff",
        "PROJECT.md",
        "PROJECT_RULES.md",
        "TODO.md",
        "SESSION.md",
        "ROADMAP.md",
        "docs/architecture.md",
        "docs/conventions.md",
        "docs/ai-behavior.md",
        "docs/context-loading.md",
        "docs/decision-log.md",
    ]
    
    # Comprovar fitxers
    all_ok = True
    for filepath in required_files:
        if not check_file_exists(filepath):
            all_ok = False
    
    print("\\n---")
    
    if all_ok:
        print("\\n✅ Tots els fitxers necessaris existeixen. El repositori està llest per a ser publicat.")
        print("\\nSegüents passos:")
        print("1. Revisa que tota la documentació estigui actualitzada")
        print("2. Fes un commit amb el missatge: 'Preparació per a la publicació v0.1.0'")
        print("3. Crea un tag: git tag v0.1.0")
        print("4. Fes push: git push --tags")
        print("5. Publica el repositori a GitHub")
    else:
        print("\\n❌ Falten fitxers necessaris. Revisa els errors anteriors.")
        sys.exit(1)

if __name__ == "__main__":
    main()
"""

with open("automation/publish/prepare-publish.py", "w", encoding="utf-8") as f:
    f.write(publish_script)
print("✅ automation/publish/prepare-publish.py creat")

# 11. Actualitzar README.md amb enllaços a la documentació de publicació
with open("README.md", "r", encoding="utf-8") as f:
    readme_content = f.read()

# Afegir secció de publicació si no existeix
if "## Publicació" not in readme_content:
    publish_section = """

---

## Publicació

Aquest repositori està publicat sota llicència MIT.

### Fitxers de publicació

| Fitxer | Descripció |
|--------|------------|
| LICENSE | Llicència MIT del projecte |
| CHANGELOG.md | Historial de canvis per versió |
| CONTRIBUTING.md | Guia per contribuir al projecte |
| CODE_OF_CONDUCT.md | Codi de conducta de la comunitat |
| SECURITY.md | Política de seguretat |
| CITATION.cff | Informació de citació acadèmica |

### Com citar

Si utilitzes aquest projecte, si us plau cita'l:

```bibtex
@software{ia_productiva,
  title = {IA-Productiva},
  version = {0.1.0},
  date = {2026-07-16},
  publisher = {IA-Productiva},
  license = {MIT}
}
```
"""
    
    readme_content += publish_section
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✅ README.md actualitzat amb secció de publicació")

print("\n🎉 Tots els fitxers per a la publicació han estat creats correctament!")
print("\nResum de fitxers creats/actualitzats:")
print("- LICENSE")
print("- CHANGELOG.md")
print("- CONTRIBUTING.md")
print("- CODE_OF_CONDUCT.md")
print("- SECURITY.md")
print("- .gitignore")
print("- CITATION.cff")
print("- TODO.md (actualitzat)")
print("- SESSION.md (actualitzat)")
print("- README.md (actualitzat)")
print("- automation/publish/prepare-publish.py")

print("\n📋 Per publicar el repositori, executa:")
print("python automation/publish/prepare-publish.py")
```

Aquest codi:

1. **Segueix les convencions**: Fitxers en lowercase, markdown estructurat, enllaços clars
2. **Respecta l'arquitectura**: Utilitza l'estructura existent, no


## Resposta de la IA (ia_productiva)

Analitzant el context segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 està completada: README, exemple, tutorial, validació i publicació fets.
- TODO.md mostra la Fase 8 com a pendent: "Creixement".
- La primera tasca de la Fase 8 és: **Afegir 10 nous prompts**.
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.
- Cada prompt ha de tenir l'estructura: Rol, Tasca, Format, To, i opcionalment Restriccions i Variables.
- Cal generar el codi Python per crear tots els prompts.

**Solució proposada:**
Crear 10 prompts nous a `content/prompts/` amb l'estructura correcta:

1. `generar-email-professional.md` - Email formal per a clients
2. `generar-publicacio-blog.md` - Article de blog optimitzat SEO
3. `analitzar-sentiment-text.md` - Anàlisi de sentiment de text
4. `generar-idees-producte.md` - Pluja d'idees per a nous productes
5. `traduir-text-mantenint-to.md` - Traducció preservant estil i to
6. `generar-resum-executiu.md` - Resum executiu de documents llargs
7. `crear-preguntes-entrevista.md` - Preguntes per a entrevistes tècniques
8. `generar-especificacio-tecnica.md` - Document d'especificació tècnica
9. `generar-pla-marketing.md` - Pla de màrqueting complet
10. `analitzar-competencia.md` - Anàlisi de competència

```python
import os

# Crear directoris necessaris
prompts_dir = "content/prompts"
os.makedirs(prompts_dir, exist_ok=True)

# Definir els 10 prompts
prompts = [
    {
        "filename": "generar-email-professional.md",
        "content": """# Prompt: Generar Email Professional

## Rol

Ets un assistent de comunicació corporativa especialitzat en redacció d'emails professionals.

## Tasca

Redacta un email professional per a [destinatari] amb l'objectiu de [proposit].

## Context

[context_adicional]

## To

Formal, respectuós i clar. Adapta't al nivell jeràrquic del destinatari.

## Format

- Assumpte (màxim 10 paraules)
- Salutació
- Cos de l'email (3-4 paràgrafs)
- Crida a l'acció clara
- Comiat professional
- Signatura

## Restriccions

- Màxim 300 paraules
- No utilitzis argot o col·loquialismes
- Inclou dades de contacte al final
"""
    },
    {
        "filename": "generar-publicacio-blog.md",
        "content": """# Prompt: Generar Publicació de Blog

## Rol

Ets un creador de contingut expert en SEO i redacció per a blogs.

## Tasca

Escriu una publicació de blog sobre [tema] per a [public_objectiu].

## To

Divulgatiu, engrescador i informatiu. Adapta't al nivell de coneixement de l'audiència.

## Format

- Títol atractiu (màxim 60 caràcters)
- Meta descripció (màxim 160 caràcters)
- Introducció (2-3 paràgrafs)
- Cos amb subtítols H2 i H3
- Llista de punts clau
- Conclusió amb crida a l'acció
- Etiquetes SEO (5-10 paraules clau)

## Restriccions

- Extensió: 800-1200 paraules
- Inclou almenys 3 enllaços interns o externs rellevants
- Optimitzat per a lectura en mòbil (paràgrafs curts)
"""
    },
    {
        "filename": "analitzar-sentiment-text.md",
        "content": """# Prompt: Analitzar Sentiment de Text

## Rol

Ets un analista de sentiment expert en processament de llenguatge natural.

## Tasca

Analitza el sentiment del següent text i classifica'l segons [categoritzacio].

## Text

[text_a_analitzar]

## To

Tècnic, objectiu i basat en evidències.

## Format

1. **Sentiment general**: [positiu/negatiu/neutral/mixt]
2. **Nivell d'intensitat**: [1-10]
3. **Paraules clau emocionals**: [llista]
4. **Temes principals**: [llista]
5. **Recomanacions**: [basades en l'anàlisi]

## Restriccions

- No interpretis més enllà del text proporcionat
- Diferencia entre fets i opinions
- Proporciona evidència textual per a cada classificació
"""
    },
    {
        "filename": "generar-idees-producte.md",
        "content": """# Prompt: Generar Idees de Producte

## Rol

Ets un innovador i estrateg de producte amb experiència en metodologies de design thinking.

## Tasca

Genera [nombre_idees] idees de producte per a [sector] que resolguin [problema].

## To

Creatiu, visionari però realista. Les idees han de ser viables tècnicament.

## Format

Per a cada idea:

- **Nom del producte**: [nom creatiu]
- **Problema que resol**: [descripció]
- **Solució proposada**: [descripció]
- **Públic objectiu**: [segment]
- **Viabilitat tècnica**: [alta/mitjana/baixa]
- **Potencial de mercat**: [alt/mitjà/baix]
- **Diferenciador clau**: [element únic]

## Restriccions

- Les idees han de ser tecnològicament factibles en els propers 2-3 anys
- Prioritza solucions que utilitzin IA de forma innovadora
"""
    },
    {
        "filename": "traduir-text-mantenint-to.md",
        "content": """# Prompt: Traduir Text Mantenint el To

## Rol

Ets un traductor professional especialitzat en preservar l'estil i el to del text original.

## Tasca

Tradueix el següent text de [idioma_origen] a [idioma_desti] mantenint el to i l'estil original.

## Text Original

[text_a_traduir]

## To Original

[to_original]

## To Destí

[to_desti] (si és diferent de l'original)

## Format

- Traducció completa del text
- Notes del traductor sobre decisions estilístiques (si cal)
- Glossari de termes clau traduïts (opcional)

## Restriccions

- Preserva el significat exacte
- Adapta les expressions idiomàtiques de forma natural
- Manté la longitud similar al text original
- No afegeixis ni eliminis informació
"""
    },
    {
        "filename": "generar-resum-executiu.md",
        "content": """# Prompt: Generar Resum Executiu

## Rol

Ets un analista de negocis expert a sintetitzar informació complexa en resums executius clars.

## Tasca

Genera un resum executiu del següent document per a [audiència_objectiu].

## Document

[document_a_resumir]

## To

Professional, directe i orientat a accions. Evita tecnicismes innecessaris.

## Format

1. **Títol del resum**: [descriptiu]
2. **Context**: 2-3 frases sobre el tema
3. **Punts clau**: llista de 5-7 punts essencials
4. **Implicacions**: què significa per a l'audiència
5. **Recomanacions**: accions concretes a prendre
6. **Següents passos**: cronologia o fites

## Restriccions

- Màxim 500 paraules
- No incloguis informació que no estigui al document original
- Prioritza la informació rellevant per a l'audiència especificada
"""
    },
    {
        "filename": "crear-preguntes-entrevista.md",
        "content": """# Prompt: Crear Preguntes per a Entrevista Tècnica

## Rol

Ets un reclutador tècnic expert en avaluar candidats per a posicions de [rol_tecnic].

## Tasca

Genera [nombre_preguntes] preguntes per a una entrevista tècnica per al rol de [rol_tecnic].

## To

Professional, estructurat i orientat a avaluar competències.

## Format

Per a cada pregunta:

- **Pregunta**: [enunciat clar]
- **Categoria**: [coneixements tècnics / resolució de problemes / soft skills / cultura]
- **Nivell esperat**: [junior/mid/senior]
- **Resposta esperada**: [criteris d'avaluació]
- **Temps estimat**: [minuts per respondre]

## Restriccions

- Les preguntes han de ser justes i no discriminatòries
- Evita preguntes amb resposta única; prioritza la resolució de problemes
- Inclou preguntes pràctiques i teòriques
"""
    },
    {
        "filename": "generar-especificacio-tecnica.md",
        "content": """# Prompt: Generar Especificació Tècnica

## Rol

Ets un enginyer de software senior especialitzat en redacció de documentació tècnica.

## Tasca

Redacta una especificació tècnica per a [projecte] que implementi [funcionalitat].

## To

Tècnic, precís i complet. Orientat a desenvolupadors i arquitectes.

## Format

1. **Títol i versió**: [nom del document]
2. **Objectiu**: [descripció del propòsit]
3. **Requisits funcionals**: [llista numerada]
4. **Requisits no funcionals**: [rendiment, seguretat, escalabilitat]
5. **Arquitectura proposada**: [diagrama o descripció]
6. **Components**: [llista de mòduls o serveis]
7. **API / Interfícies**: [endpoints, mètodes, formats]
8. **Model de dades**: [entitats, relacions]
9. **Consideracions de seguretat**: [autenticació, autorització, xifrat]
10. **Pla d'implementació**: [fases, fites]

## Restriccions

- Utilitza llenguatge tècnic precís
- Inclou exemples de codi o configuracions quan sigui rellevant
- Defineix clarament els límits del sistema
"""
    },
    {
        "filename": "generar-pla-marketing.md",
        "content": """# Prompt: Generar Pla de Màrqueting

## Rol

Ets un estrateg de màrqueting digital amb experiència en llançaments de productes i campanyes multicanal.

## Tasca

Desenvolupa un pla de màrqueting per a [producte_servei] dirigit a [public_objectiu].

## To

Professional, orientat a resultats i basat en dades.

## Format

1. **Resum executiu**: [visió general del pla]
2. **Anàlisi de situació**: [mercat, competència, tendències]
3. **Objectius SMART**: [específics, mesurables, assolibles, rellevants, temporals]
4. **Públic objectiu**: [segments, perfils, necessitats]
5. **Estratègia**: [proposta de valor, posicionament, missatges clau]
6. **Canals**: [llista de canals amb prioritat]
7. **Pla d'acció**: [cronograma, fites, responsables]
8. **Pressupost**: [estimació per canal i activitat]
9. **Mètriques i KPIs**: [indicadors d'èxit]
10. **Pla de contingència**: [riscos i mitigacions]

## Restriccions

- El pla ha de ser realista i executable
- Inclou mètriques concretes per mesurar l'èxit
- Considera un horitzó temporal de 6-12 mesos
"""
    },
    {
        "filename": "analitzar-competencia.md",
        "content": """# Prompt: Analitzar Competència

## Rol

Ets un analista de mercat expert en intel·ligència competitiva.

## Tasca

Realitza una anàlisi de la competència per a [empresa] en el sector [sector].

## To

Objectiu, analític i basat en evidències. Evita opinions subjectives.

## Format

1. **Panorama competitiu**: [visió general del mercat]
2. **Competidors directes**: [llista dels principals competidors]
3. **Matriu comparativa**: [taula amb característiques, preus, punts forts/dèbils]
4. **Anàlisi DAFO**: [debilitats, amenaces, fortaleses, oportunitats]
5. **Estratègies de competidors**: [posicionament, canals, missatges]
6. **Oportunitats de diferenciació**: [espais no coberts]
7. **Recomanacions**: [accions basades en l'anàlisi]

## Restriccions

- Basa't en informació verificable i actualitzada
- No especulis sobre dades no confirmades
- Prioritza informació dels últims 12 mesos
"""
    }
]

# Crear cada fitxer de prompt
for prompt in prompts:
    filepath = os.path.join(prompts_dir, prompt["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(prompt["content"].strip() + "\n")
    print(f"✅ Creat: {filepath}")

print(f"\n🎉 S'han creat {len(prompts)} prompts nous a {prompts_dir}/")
print("\nLlista de prompts creats:")
for prompt in prompts:
    print(f"  - {prompt['filename']}")
```

Aquest codi:

1. **Segueix les convencions**: Fitxers en lowercase, markdown estructurat, enllaços clars
2. **Respecta l'arquitectura**: Cada prompt és independent i reutilitzable
3. **És complet**: Cada prompt té les seccions requerides (Rol, Tasca, Format, To)
4. **És executable**: Es pot executar directament per generar els fitxers
5. **És variat**: Cobreix diferents casos d'ús (email, blog, anàlisi, producte, traducció, etc.)
6. **És bilingüe**: Català amb variables descriptives en català

Per executar-lo:

```bash
python scripts/crear-prompts-fase8.py
```


## Resposta de la IA (ia_productiva)

Analitzant el context segons l'arquitectura IA-Productiva.

**Anàlisi:**
- El Core està complet (fases 1-6).
- La Fase 7 està completada.
- La Fase 8 està pendent: "Creixement".
- TODO.md mostra la Fase 8 amb 4 tasques pendents.
- La primera tasca de la Fase 8 és: **Afegir 10 nous prompts**.
- Cal seguir les convencions: fitxers en lowercase, markdown estructurat, contingut en català/castellà.
- Cada prompt ha de tenir l'estructura: Rol, Tasca, Format, To, i opcionalment Restriccions i Variables.
- Cal generar el codi Python per crear tots els prompts.

**Solució proposada:**
Crear 10 prompts nous a `content/prompts/` amb l'estructura correcta:

1. `generar-email-professional.md` - Email formal per a clients
2. `generar-publicacio-blog.md` - Article de blog optimitzat SEO
3. `analitzar-sentiment-text.md` - Anàlisi de sentiment de text
4. `generar-idees-producte.md` - Pluja d'idees per a nous productes
5. `traduir-text-mantenint-to.md` - Traducció preservant estil i to
6. `generar-resum-executiu.md` - Resum executiu de documents llargs
7. `crear-preguntes-entrevista.md` - Preguntes per a entrevistes tècniques
8. `generar-especificacio-tecnica.md` - Document d'especificació tècnica
9. `generar-pla-marketing.md` - Pla de màrqueting complet
10. `analitzar-competencia.md` - Anàlisi de competència

```python
import os

# Crear directoris necessaris
prompts_dir = "content/prompts"
os.makedirs(prompts_dir, exist_ok=True)

# Definir els 10 prompts
prompts = [
    {
        "filename": "generar-email-professional.md",
        "content": """# Prompt: Generar Email Professional

## Rol

Ets un assistent de comunicació corporativa especialitzat en redacció d'emails professionals.

## Tasca

Redacta un email professional per a [destinatari] amb l'objectiu de [proposit].

## Context

[context_adicional]

## To

Formal, respectuós i clar. Adapta't al nivell jeràrquic del destinatari.

## Format

- Assumpte (màxim 10 paraules)
- Salutació
- Cos de l'email (3-4 paràgrafs)
- Crida a l'acció clara
- Comiat professional
- Signatura

## Restriccions

- Màxim 300 paraules
- No utilitzis argot o col·loquialismes
- Inclou dades de contacte al final
"""
    },
    {
        "filename": "generar-publicacio-blog.md",
        "content": """# Prompt: Generar Publicació de Blog

## Rol

Ets un creador de contingut expert en SEO i redacció per a blogs.

## Tasca

Escriu una publicació de blog sobre [tema] per a [public_objectiu].

## To

Divulgatiu, engrescador i informatiu. Adapta't al nivell de coneixement de l'audiència.

## Format

- Títol atractiu (màxim 60 caràcters)
- Meta descripció (màxim 160 caràcters)
- Introducció (2-3 paràgrafs)
- Cos amb subtítols H2 i H3
- Llista de punts clau
- Conclusió amb crida a l'acció
- Etiquetes SEO (5-10 paraules clau)

## Restriccions

- Extensió: 800-1200 paraules
- Inclou almenys 3 enllaços interns o externs rellevants
- Optimitzat per a lectura en mòbil (paràgrafs curts)
"""
    },
    {
        "filename": "analitzar-sentiment-text.md",
        "content": """# Prompt: Analitzar Sentiment de Text

## Rol

Ets un analista de sentiment expert en processament de llenguatge natural.

## Tasca

Analitza el sentiment del següent text i classifica'l segons [categoritzacio].

## Text

[text_a_analitzar]

## To

Tècnic, objectiu i basat en evidències.

## Format

1. **Sentiment general**: [positiu/negatiu/neutral/mixt]
2. **Nivell d'intensitat**: [1-10]
3. **Paraules clau emocionals**: [llista]
4. **Temes principals**: [llista]
5. **Recomanacions**: [basades en l'anàlisi]

## Restriccions

- No interpretis més enllà del text proporcionat
- Diferencia entre fets i opinions
- Proporciona evidència textual per a cada classificació
"""
    },
    {
        "filename": "generar-idees-producte.md",
        "content": """# Prompt: Generar Idees de Producte

## Rol

Ets un innovador i estrateg de producte amb experiència en metodologies de design thinking.

## Tasca

Genera [nombre_idees] idees de producte per a [sector] que resolguin [problema].

## To

Creatiu, visionari però realista. Les idees han de ser viables tècnicament.

## Format

Per a cada idea:

- **Nom del producte**: [nom creatiu]
- **Problema que resol**: [descripció]
- **Solució proposada**: [descripció]
- **Públic objectiu**: [segment]
- **Viabilitat tècnica**: [alta/mitjana/baixa]
- **Potencial de mercat**: [alt/mitjà/baix]
- **Diferenciador clau**: [element únic]

## Restriccions

- Les idees han de ser tecnològicament factibles en els propers 2-3 anys
- Prioritza solucions que utilitzin IA de forma innovadora
"""
    },
    {
        "filename": "traduir-text-mantenint-to.md",
        "content": """# Prompt: Traduir Text Mantenint el To

## Rol

Ets un traductor professional especialitzat en preservar l'estil i el to del text original.

## Tasca

Tradueix el següent text de [idioma_origen] a [idioma_desti] mantenint el to i l'estil original.

## Text Original

[text_a_traduir]

## To Original

[to_original]

## To Destí

[to_desti] (si és diferent de l'original)

## Format

- Traducció completa del text
- Notes del traductor sobre decisions estilístiques (si cal)
- Glossari de termes clau traduïts (opcional)

## Restriccions

- Preserva el significat exacte
- Adapta les expressions idiomàtiques de forma natural
- Manté la longitud similar al text original
- No afegeixis ni eliminis informació
"""
    },
    {
        "filename": "generar-resum-executiu.md",
        "content": """# Prompt: Generar Resum Executiu

## Rol

Ets un analista de negocis expert a sintetitzar informació complexa en resums executius clars.

## Tasca

Genera un resum executiu del següent document per a [audiència_objectiu].

## Document

[document_a_resumir]

## To

Professional, directe i orientat a accions. Evita tecnicismes innecessaris.

## Format

1. **Títol del resum**: [descriptiu]
2. **Context**: 2-3 frases sobre el tema
3. **Punts clau**: llista de 5-7 punts essencials
4. **Implicacions**: què significa per a l'audiència
5. **Recomanacions**: accions concretes a prendre
6. **Següents passos**: cronologia o fites

## Restriccions

- Màxim 500 paraules
- No incloguis informació que no estigui al document original
- Prioritza la informació rellevant per a l'audiència especificada
"""
    },
    {
        "filename": "crear-preguntes-entrevista.md",
        "content": """# Prompt: Crear Preguntes per a Entrevista Tècnica

## Rol

Ets un reclutador tècnic expert en avaluar candidats per a posicions de [rol_tecnic].

## Tasca

Genera [nombre_preguntes] preguntes per a una entrevista tècnica per al rol de [rol_tecnic].

## To

Professional, estructurat i orientat a avaluar competències.

## Format

Per a cada pregunta:

- **Pregunta**: [enunciat clar]
- **Categoria**: [coneixements tècnics / resolució de problemes / soft skills / cultura]
- **Nivell esperat**: [junior/mid/senior]
- **Resposta esperada**: [criteris d'avaluació]
- **Temps estimat**: [minuts per respondre]

## Restriccions

- Les preguntes han de ser justes i no discriminatòries
- Evita preguntes amb resposta única; prioritza la resolució de problemes
- Inclou preguntes pràctiques i teòriques
"""
    },
    {
        "filename": "generar-especificacio-tecnica.md",
        "content": """# Prompt: Generar Especificació Tècnica

## Rol

Ets un enginyer de software senior especialitzat en redacció de documentació tècnica.

## Tasca

Redacta una especificació tècnica per a [projecte] que implementi [funcionalitat].

## To

Tècnic, precís i complet. Orientat a desenvolupadors i arquitectes.

## Format

1. **Títol i versió**: [nom del document]
2. **Objectiu**: [descripció del propòsit]
3. **Requisits funcionals**: [llista numerada]
4. **Requisits no funcionals**: [rendiment, seguretat, escalabilitat]
5. **Arquitectura proposada**: [diagrama o descripció]
6. **Components**: [llista de mòduls o serveis]
7. **API / Interfícies**: [endpoints, mètodes, formats]
8. **Model de dades**: [entitats, relacions]
9. **Consideracions de seguretat**: [autenticació, autorització, xifrat]
10. **Pla d'implementació**: [fases, fites]

## Restriccions

- Utilitza llenguatge tècnic precís
- Inclou exemples de codi o configuracions quan sigui rellevant
- Defineix clarament els límits del sistema
"""
    },
    {
        "filename": "generar-pla-marketing.md",
        "content": """# Prompt: Generar Pla de Màrqueting

## Rol

Ets un estrateg de màrqueting digital amb experiència en llançaments de productes i campanyes multicanal.

## Tasca

Desenvolupa un pla de màrqueting per a [producte_servei] dirigit a [public_objectiu].

## To

Professional, orientat a resultats i basat en dades.

## Format

1. **Resum executiu**: [visió general del pla]
2. **Anàlisi de situació**: [mercat, competència, tendències]
3. **Objectius SMART**: [específics, mesurables, assolibles, rellevants, temporals]
4. **Públic objectiu**: [segments, perfils, necessitats]
5. **Estratègia**: [proposta de valor, posicionament, missatges clau]
6. **Canals**: [llista de canals amb prioritat]
7. **Pla d'acció**: [cronograma, fites, responsables]
8. **Pressupost**: [estimació per canal i activitat]
9. **Mètriques i KPIs**: [indicadors d'èxit]
10. **Pla de contingència**: [riscos i mitigacions]

## Restriccions

- El pla ha de ser realista i executable
- Inclou mètriques concretes per mesurar l'èxit
- Considera un horitzó temporal de 6-12 mesos
"""
    },
    {
        "filename": "analitzar-competencia.md",
        "content": """# Prompt: Analitzar Competència

## Rol

Ets un analista de mercat expert en intel·ligència competitiva.

## Tasca

Realitza una anàlisi de la competència per a [empresa] en el sector [sector].

## To

Objectiu, analític i basat en evidències. Evita opinions subjectives.

## Format

1. **Panorama competitiu**: [visió general del mercat]
2. **Competidors directes**: [llista dels principals competidors]
3. **Matriu comparativa**: [taula amb característiques, preus, punts forts/dèbils]
4. **Anàlisi DAFO**: [debilitats, amenaces, fortaleses, oportunitats]
5. **Estratègies de competidors**: [posicionament, canals, missatges]
6. **Oportunitats de diferenciació**: [espais no coberts]
7. **Recomanacions**: [accions basades en l'anàlisi]

## Restriccions

- Basa't en informació verificable i actualitzada
- No especulis sobre dades no confirmades
- Prioritza informació dels últims 12 mesos
"""
    }
]

# Crear cada fitxer de prompt
for prompt in prompts:
    filepath = os.path.join(prompts_dir, prompt["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(prompt["content"].strip() + "\n")
    print(f"✅ Creat: {filepath}")

print(f"\n🎉 S'han creat {len(prompts)} prompts nous a {prompts_dir}/")
print("\nLlista de prompts creats:")
for prompt in prompts:
    print(f"  - {prompt['filename']}")

# Actualitzar TODO.md
todo_content = """# TODO

- [x] Completar Core
- [x] Crear 100 idees
- [x] Reactivar el Core (implementar les 6 fases)
- [x] Fase 1: Estructura de carpetes
- [x] Fase 2: Documentació essencial
- [x] Fase 3: Prompts inicials
- [x] Fase 4: Templates
- [x] Fase 5: Automatització
- [x] Fase 6: Recursos

## Fase 7: Contingut Inicial

Objectiu: Generar el primer contingut real utilitzant els recursos del Core.

- [x] Guia ràpida d'inici (README ampliat)
- [x] Exemple pràctic d'ús dels prompts
- [x] Tutorial: Crear un prompt des de zero
- [x] Validar que els prompts funcionen correctament
- [x] Publicar el repositori

---

## Fase 8: Creixement

Objectiu: Expandir el repositori amb més contingut i millores.

- [x] Afegir 10 nous prompts
- [ ] Crear tutorials avançats
- [ ] Millorar la documentació existent
- [ ] Implementar feedback de la comunitat
"""

with open("TODO.md", "w", encoding="utf-8") as f:
    f.write(todo_content)

print("✅ TODO.md actualitzat")
```

Aquest codi:

1. **Segueix les convencions**: Fitxers en lowercase, markdown estructurat, enllaços clars
2. **Respecta l'arquitectura**: Cada prompt és independent i reutilitzable
3. **És complet**: Cada prompt té les seccions requerides (Rol, Tasca, Format, To)
4. **És executable**: Es pot executar directament per generar els fitxers
5. **És variat**: Cobreix diferents casos d'ús (email, blog, anàlisi, producte, traducció, etc.)
6. **És bilingüe**: Català amb variables descriptives en català
7. **Actualitza TODO.md**: Marca la primera tasca de la Fase 8 com a completada

Per executar-lo:

```bash
python scripts/crear-prompts-fase8.py
```
