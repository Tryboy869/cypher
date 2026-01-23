# 🧬 CYPHER Primitives Reference / Référence des Primitives

**Version:** 0.1.0  
**Last Updated / Dernière mise à jour:** January 2026 / Janvier 2026

---

## Table of Contents / Table des Matières

### English
1. [Overview](#overview-english)
2. [A - Create](#a---create-english)
3. [C - Connect](#c---connect-english)
4. [G - Generate](#g---generate-english)
5. [T - Transform](#t---transform-english)
6. [F - Fix](#f---fix-english)
7. [L - Life](#l---life-english)
8. [Composition Patterns](#composition-patterns-english)

### Français
1. [Vue d'ensemble](#vue-densemble-français)
2. [A - Créer](#a---créer-français)
3. [C - Connecter](#c---connecter-français)
4. [G - Générer](#g---générer-français)
5. [T - Transformer](#t---transformer-français)
6. [F - Fixer](#f---fixer-français)
7. [L - Vie](#l---vie-français)
8. [Patterns de Composition](#patterns-de-composition-français)

---

# Overview (English)

CYPHER is built on **6 fundamental primitives** that correspond to the basic operations needed for any computation. These primitives are inspired by DNA's four bases (A, C, G, T) plus two control operators (F, L).

## Turing Completeness

The 6 primitives map to the classical Turing machine operations:

| CYPHER | Turing Operation | Function |
|--------|------------------|----------|
| **A** | Print/Write | Create new entity |
| **C** | Right/Left | Navigate/link entities |
| **G** | Scan/Read | Input data |
| **T** | Erase/Modify | Transform state |
| **F** | Halt (Pause) | Fix state |
| **L** | Execute | Launch lifecycle |

## Base-4 Compilation

Each primitive compiles to a 2-bit opcode:

```
A = 00 (binary) = 0 (decimal)
C = 01 (binary) = 1 (decimal)
G = 10 (binary) = 2 (decimal)
T = 11 (binary) = 3 (decimal)
```

---

# Vue d'ensemble (Français)

CYPHER est construit sur **6 primitives fondamentales** qui correspondent aux opérations de base nécessaires pour tout calcul. Ces primitives sont inspirées des quatre bases de l'ADN (A, C, G, T) plus deux opérateurs de contrôle (F, L).

## Complétude de Turing

Les 6 primitives correspondent aux opérations classiques de machine de Turing:

| CYPHER | Opération Turing | Fonction |
|--------|------------------|----------|
| **A** | Print/Write | Créer nouvelle entité |
| **C** | Right/Left | Naviguer/lier entités |
| **G** | Scan/Read | Entrée données |
| **T** | Erase/Modify | Transformer état |
| **F** | Halt (Pause) | Fixer état |
| **L** | Execute | Lancer cycle de vie |

## Compilation Base-4

Chaque primitive compile vers un opcode 2-bit:

```
A = 00 (binaire) = 0 (décimal)
C = 01 (binaire) = 1 (décimal)
G = 10 (binaire) = 2 (décimal)
T = 11 (binaire) = 3 (décimal)
```

---

# A - Create (English)

## Syntax
```cypher
A(identifier)
```

## Purpose
Creates a new entity in the system. This is the fundamental building block.

## Parameters
- `identifier`: Name/ID of the entity to create

## Backend Behavior

### Web Backend
Infers HTML element type from identifier:
- `button` → `<button>`
- `header` → `<header>`
- `input` → `<input>`
- `container` / other → `<div>`

### Rust Backend
Generates a struct or function definition.

## Examples

```cypher
# Create a button / Créer un bouton
A(button):

# Create a container / Créer un conteneur
A(dashboard):

# Create an API endpoint / Créer un endpoint API
A(api_users):
```

## Output Examples

**Web:**
```html
<button id="button"></button>
<div id="dashboard"></div>
```

**Rust:**
```rust
struct Button {}
struct Dashboard {}
```

---

# A - Créer (Français)

## Syntaxe
```cypher
A(identificateur)
```

## Objectif
Crée une nouvelle entité dans le système. C'est le bloc de construction fondamental.

## Paramètres
- `identificateur`: Nom/ID de l'entité à créer

## Comportement Backend

### Backend Web
Déduit le type d'élément HTML depuis l'identificateur:
- `button` → `<button>`
- `header` → `<header>`
- `input` → `<input>`
- `container` / autre → `<div>`

### Backend Rust
Génère une définition de struct ou fonction.

## Exemples

```cypher
# Créer un bouton
A(button):

# Créer un conteneur
A(dashboard):

# Créer un endpoint API
A(api_users):
```

## Exemples de Sortie

**Web:**
```html
<button id="button"></button>
<div id="dashboard"></div>
```

**Rust:**
```rust
struct Button {}
struct Dashboard {}
```

---

# C - Connect (English)

## Syntax
```cypher
C(target)
```

## Purpose
Establishes connections between entities. Creates relationships and data flow.

## Parameters
- `target`: Entity or resource to connect to

## Use Cases
- Link UI components
- Connect to APIs
- Establish database queries
- Create event handlers

## Examples

```cypher
# Connect to API / Connecter à API
A(user_list);C(api_users):

# Connect to database / Connecter à base de données
A(query);C(db_connection):

# Link components / Lier composants
A(parent);C(child):
```

## Backend Behavior

### Web Backend
Creates event handlers or data bindings.

### Rust Backend
Generates function calls or module imports.

---

# C - Connecter (Français)

## Syntaxe
```cypher
C(cible)
```

## Objectif
Établit des connexions entre entités. Crée relations et flux de données.

## Paramètres
- `cible`: Entité ou ressource à connecter

## Cas d'Usage
- Lier composants UI
- Connecter aux APIs
- Établir requêtes base de données
- Créer gestionnaires d'événements

## Exemples

```cypher
# Connecter à API
A(user_list);C(api_users):

# Connecter à base de données
A(query);C(db_connection):

# Lier composants
A(parent);C(child):
```

## Comportement Backend

### Backend Web
Crée gestionnaires d'événements ou liaisons de données.

### Backend Rust
Génère appels de fonction ou imports de module.

---

# G - Generate (English)

## Syntax
```cypher
G("content")
G(parameter:value)
```

## Purpose
Generates content or inputs data into entities.

## Parameters
- `"text"`: Text content (quoted)
- `key:value`: Named parameters

## Examples

```cypher
# Add text content / Ajouter contenu texte
A(title);G("Welcome to CYPHER"):

# Add placeholder / Ajouter placeholder
A(input);G(placeholder:"Enter name"):

# Add endpoint / Ajouter endpoint
A(api);G(endpoint:/api/users):

# Add SQL query / Ajouter requête SQL
A(query);G(SELECT * FROM users):
```

## Backend Behavior

### Web Backend
```html
<h1>Welcome to CYPHER</h1>
<input placeholder="Enter name" />
```

### Rust Backend
```rust
let endpoint = "/api/users";
let query = "SELECT * FROM users";
```

---

# G - Générer (Français)

## Syntaxe
```cypher
G("contenu")
G(paramètre:valeur)
```

## Objectif
Génère du contenu ou injecte des données dans les entités.

## Paramètres
- `"texte"`: Contenu texte (entre guillemets)
- `clé:valeur`: Paramètres nommés

## Exemples

```cypher
# Ajouter contenu texte
A(title);G("Bienvenue à CYPHER"):

# Ajouter placeholder
A(input);G(placeholder:"Entrer nom"):

# Ajouter endpoint
A(api);G(endpoint:/api/users):

# Ajouter requête SQL
A(query);G(SELECT * FROM users):
```

## Comportement Backend

### Backend Web
```html
<h1>Bienvenue à CYPHER</h1>
<input placeholder="Entrer nom" />
```

### Backend Rust
```rust
let endpoint = "/api/users";
let query = "SELECT * FROM users";
```

---

# T - Transform (English)

## Syntax
```cypher
T(style)
T(style1;style2;style3)
```

## Purpose
Transforms appearance, behavior, or output format of entities.

## Parameters
- Single style: `T(primary)`
- Multiple styles: `T(flex;column;gap-2)`
- CSS properties: `T(color:#333)`

## Style Categories

### Layout Utilities
```cypher
T(flex)           # display: flex
T(grid)           # display: grid
T(column)         # flex-direction: column
```

### Color/Theme
```cypher
T(primary)        # Blue theme
T(secondary)      # Gray theme
T(danger)         # Red theme
```

### Typography
```cypher
T(text-xl)        # Large text
T(text-2xl)       # Extra large text
T(font-bold)      # Bold font
```

### Custom CSS
```cypher
T(color:#ff0000)
T(padding:1rem)
T(border-radius:0.5rem)
```

## Examples

```cypher
# Button with primary style / Bouton avec style primaire
A(button);G("Click");T(primary):

# Flex container / Conteneur flex
A(container);T(flex;column;gap-2):

# Custom styled card / Carte avec style personnalisé
A(card);T(padding:2rem;bg:#f0f0f0;border-radius:1rem):
```

## Backend Behavior

### Web Backend
Generates CSS classes and inline styles:

```html
<button class="primary">Click</button>
<div class="flex column gap-2"></div>
<div style="padding: 2rem; background: #f0f0f0; border-radius: 1rem;"></div>
```

### Rust Backend
Generates configuration or formatting directives.

---

# T - Transformer (Français)

## Syntaxe
```cypher
T(style)
T(style1;style2;style3)
```

## Objectif
Transforme l'apparence, comportement ou format de sortie des entités.

## Paramètres
- Style unique: `T(primary)`
- Plusieurs styles: `T(flex;column;gap-2)`
- Propriétés CSS: `T(color:#333)`

## Catégories de Style

### Utilitaires de Mise en Page
```cypher
T(flex)           # display: flex
T(grid)           # display: grid
T(column)         # flex-direction: column
```

### Couleur/Thème
```cypher
T(primary)        # Thème bleu
T(secondary)      # Thème gris
T(danger)         # Thème rouge
```

### Typographie
```cypher
T(text-xl)        # Texte large
T(text-2xl)       # Texte extra large
T(font-bold)      # Police grasse
```

### CSS Personnalisé
```cypher
T(color:#ff0000)
T(padding:1rem)
T(border-radius:0.5rem)
```

## Exemples

```cypher
# Bouton avec style primaire
A(button);G("Cliquer");T(primary):

# Conteneur flex
A(container);T(flex;column;gap-2):

# Carte avec style personnalisé
A(card);T(padding:2rem;bg:#f0f0f0;border-radius:1rem):
```

## Comportement Backend

### Backend Web
Génère classes CSS et styles inline:

```html
<button class="primary">Cliquer</button>
<div class="flex column gap-2"></div>
<div style="padding: 2rem; background: #f0f0f0; border-radius: 1rem;"></div>
```

### Backend Rust
Génère configuration ou directives de formatage.

---

# F - Fix (English)

## Syntax
```cypher
F(fixed)
```

## Purpose
Locks the system state. Prevents further modifications. Must be called before `L(life)`.

## Behavior
- Freezes all entities
- Prevents mutations
- Prepares system for execution

## Examples

```cypher
# Simple program / Programme simple
A(app);G("Hello"):
F(fixed):
L(life):

# Complex system / Système complexe
A(ui);T(flex):
A(api);C(backend):
F(fixed):  # Lock state / Verrouiller état
L(life):   # Then execute / Puis exécuter
```

## Error Handling

Without F(fixed), L(life) will throw error:
```
RuntimeError: System must be fixed before running
```

---

# F - Fixer (Français)

## Syntaxe
```cypher
F(fixed)
```

## Objectif
Verrouille l'état du système. Empêche modifications ultérieures. Doit être appelé avant `L(life)`.

## Comportement
- Gèle toutes les entités
- Empêche mutations
- Prépare système pour exécution

## Exemples

```cypher
# Programme simple
A(app);G("Bonjour"):
F(fixed):
L(life):

# Système complexe
A(ui);T(flex):
A(api);C(backend):
F(fixed):  # Verrouiller état
L(life):   # Puis exécuter
```

## Gestion d'Erreurs

Sans F(fixed), L(life) lance erreur:
```
RuntimeError: System must be fixed before running
```

---

# L - Life (English)

## Syntax
```cypher
L(life)
```

## Purpose
Launches system execution. Starts the "lifecycle" of the living system.

## Requirements
- Must come after `F(fixed)`
- Should be last instruction

## Behavior
Triggers:
1. Final compilation
2. Backend execution
3. Output generation
4. System startup

## Examples

```cypher
# Web app launch / Lancement app web
A(app);G("Dashboard"):
F(fixed):
L(life):

# API server launch / Lancement serveur API
A(server);G(port:8000):
C(routes):
F(fixed):
L(life):
```

## Lifecycle Phases

```
Parse → Compile → Fix → Life
   ↓        ↓       ↓      ↓
  AST → Bytecode → Lock → Execute
```

---

# L - Vie (Français)

## Syntaxe
```cypher
L(life)
```

## Objectif
Lance l'exécution du système. Démarre le "cycle de vie" du système vivant.

## Prérequis
- Doit venir après `F(fixed)`
- Devrait être dernière instruction

## Comportement
Déclenche:
1. Compilation finale
2. Exécution backend
3. Génération sortie
4. Démarrage système

## Exemples

```cypher
# Lancement app web
A(app);G("Tableau de bord"):
F(fixed):
L(life):

# Lancement serveur API
A(server);G(port:8000):
C(routes):
F(fixed):
L(life):
```

## Phases du Cycle de Vie

```
Parse → Compile → Fix → Life
   ↓        ↓       ↓      ↓
  AST → Bytecode → Lock → Exécuter
```

---

# Composition Patterns (English)

## Pattern 1: Simple UI Component

```cypher
A(button);G("Submit");T(primary):
```

Generates:
```html
<button class="primary">Submit</button>
```

---

## Pattern 2: Container with Children

```cypher
A(dashboard);T(grid):
  A(card1);G("Sales: $45k"):
  A(card2);G("Users: 1.2k"):
```

Generates:
```html
<div id="dashboard" class="grid">
  <div id="card1">Sales: $45k</div>
  <div id="card2">Users: 1.2k</div>
</div>
```

---

## Pattern 3: Full-Stack Flow

```cypher
# Frontend
A(ui);C(api_data):

# Backend
A(api_data);G(endpoint:/api/users):
  C(database):
  T(return_json):

F(fixed):
L(life):
```

---

# Patterns de Composition (Français)

## Pattern 1: Composant UI Simple

```cypher
A(button);G("Soumettre");T(primary):
```

Génère:
```html
<button class="primary">Soumettre</button>
```

---

## Pattern 2: Conteneur avec Enfants

```cypher
A(dashboard);T(grid):
  A(card1);G("Ventes: 45k€"):
  A(card2);G("Utilisateurs: 1.2k"):
```

Génère:
```html
<div id="dashboard" class="grid">
  <div id="card1">Ventes: 45k€</div>
  <div id="card2">Utilisateurs: 1.2k</div>
</div>
```

---

## Pattern 3: Flux Full-Stack

```cypher
# Frontend
A(ui);C(api_data):

# Backend
A(api_data);G(endpoint:/api/users):
  C(database):
  T(return_json):

F(fixed):
L(life):
```

---

## Advanced Compositions / Compositions Avancées

### Pattern 4: Form with Validation
```cypher
A(form);T(flex;column):
  A(input_email);G(type:email;required:true):
  A(input_password);G(type:password;min:8):
  A(submit);G("Login");T(primary):
  C(validate):
```

### Pattern 5: API with Error Handling
```cypher
A(api_endpoint);G(path:/api/create):
  C(validate_input):
  C(db_insert):
  T(on_success:return_201):
  T(on_error:return_400):
```

---

**CYPHER v0.1.0 - Primitives Reference**  
**Référence des Primitives CYPHER v0.1.0**

For more examples, see `/examples` directory.  
Pour plus d'exemples, voir répertoire `/examples`.