# 🧬 CYPHER v0.1.0

**Bio-inspired programming language for living systems**  
**Langage de programmation bio-inspiré pour systèmes vivants**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/tryboy869/cypher)

---

## 🌟 Overview / Vue d'ensemble

### English

CYPHER is a revolutionary programming language inspired by DNA's elegant simplicity. With only **6 core primitives** (A, C, G, T, F, L), you can build complete full-stack applications — from user interfaces to backend APIs.

**Key Features:**
- ✨ **6 primitives** for Turing-complete computation
- 🎨 **Multi-backend**: HTML/CSS/JS for UI, Rust for logic
- 📦 **Single-file runtime** (~1500 lines Python)
- 🚀 **Simple installation**: `pip install cypher-lang`
- 🔄 **Living systems**: Code with fixed state and lifecycle

### Français

CYPHER est un langage de programmation révolutionnaire inspiré de l'élégance simple de l'ADN. Avec seulement **6 primitives de base** (A, C, G, T, F, L), vous pouvez construire des applications full-stack complètes — des interfaces utilisateur aux APIs backend.

**Caractéristiques clés:**
- ✨ **6 primitives** pour calcul Turing-complet
- 🎨 **Multi-backend**: HTML/CSS/JS pour UI, Rust pour logique
- 📦 **Runtime fichier unique** (~1500 lignes Python)
- 🚀 **Installation simple**: `pip install cypher-lang`
- 🔄 **Systèmes vivants**: Code avec état fixé et cycle de vie

---

## 🚀 Quick Start / Démarrage Rapide

### Installation

```bash
# Install from PyPI / Installer depuis PyPI
pip install cypher-lang

# Or install from source / Ou installer depuis source
git clone https://github.com/tryboy869/cypher
cd cypher
pip install -e .
```

### Hello World

```cypher
# hello.cypher

# Create a button with content / Créer un bouton avec contenu
A(button);G("Hello CYPHER!");T(primary):

# Fix state and launch / Fixer état et lancer
F(fixed):
L(life):
```

Run it / Exécutez-le:
```bash
cypher run hello.cypher
```

Output / Sortie:
```html
<button id="button" class="primary">Hello CYPHER!</button>
```

---

## 📖 Language Guide / Guide du Langage

### The 6 Primitives / Les 6 Primitives

| Primitive | Name / Nom | Function / Fonction | Example / Exemple |
|-----------|------------|---------------------|-------------------|
| **A** | Create / Créer | Create entity / Créer entité | `A(button)` |
| **C** | Connect / Connecter | Link entities / Lier entités | `C(api_endpoint)` |
| **G** | Generate / Générer | Add content / Ajouter contenu | `G("Hello")` |
| **T** | Transform / Transformer | Style/behavior / Style/comportement | `T(primary)` |
| **F** | Fix / Fixer | Lock state / Verrouiller état | `F(fixed)` |
| **L** | Life / Vie | Launch execution / Lancer exécution | `L(life)` |

### Syntax Rules / Règles de Syntaxe

**English:**
- Each line is a **gene** (ends with `:`)
- Instructions separated by `;`
- Comments start with `#`
- Parameters in parentheses: `A(name)`
- Multiple params with `;`: `T(flex;column)`

**Français:**
- Chaque ligne est un **gène** (se termine par `:`)
- Instructions séparées par `;`
- Commentaires commencent par `#`
- Paramètres entre parenthèses: `A(nom)`
- Plusieurs paramètres avec `;`: `T(flex;column)`

---

## 💡 Examples / Exemples

### 1. Simple UI / UI Simple

```cypher
# Dashboard layout / Mise en page tableau de bord
A(dashboard);T(flex;column):
  A(header);G("My Dashboard");T(text-2xl):
  A(content);T(grid):
    A(card);G("Users: 1,234");T(primary):
    A(card);G("Sales: $45k");T(primary):

F(fixed):
L(life):
```

### 2. Full-Stack App / Application Full-Stack

```cypher
# Frontend
A(app);T(flex):
  A(title);G("Blog");T(text-xl):
  A(posts);C(fetch_api):

# Backend
A(api_posts);G(endpoint:/api/posts):
  C(db_query);T(SELECT * FROM posts):
  T(return_json):

F(fixed):
L(life):
```

### 3. Workflow Automation / Automatisation Workflow

```cypher
# Daily email report / Rapport email quotidien
A(cron);G("0 9 * * *"):
  C(collect_data):
  C(generate_report):
  C(send_email);G(to:admin@company.com):

F(fixed):
L(life):
```

---

## 🛠️ CLI Commands / Commandes CLI

### English

```bash
# Run CYPHER file / Exécuter fichier CYPHER
cypher run app.cypher

# Compile to bytecode / Compiler en bytecode
cypher build app.cypher

# Generate web output / Générer sortie web
cypher run app.cypher web

# Generate Rust code / Générer code Rust
cypher run app.cypher rust

# Show version / Afficher version
cypher version
```

### Français

```bash
# Exécuter fichier CYPHER
cypher run app.cypher

# Compiler en bytecode
cypher build app.cypher

# Générer sortie web
cypher run app.cypher web

# Générer code Rust
cypher run app.cypher rust

# Afficher version
cypher version
```

---

## 🐳 Docker Usage / Utilisation Docker

```bash
# Build image / Construire image
docker build -t cypher:0.1.0 .

# Run CYPHER file / Exécuter fichier CYPHER
docker run -v $(pwd)/app.cypher:/app.cypher cypher:0.1.0 run /app.cypher

# Interactive mode / Mode interactif
docker run -it cypher:0.1.0
```

---

## 🏗️ Architecture

### English

CYPHER uses a **single-file runtime** approach:

```
cypher.py (~1500 lines)
├── Parser (ACGTFL → AST)
├── Compiler (AST → Bytecode base-4)
├── Backends
│   ├── Web (HTML/CSS/JS)
│   └── Rust (API/Logic)
├── Entity System (State management)
└── CLI (Commands)
```

### Français

CYPHER utilise une approche **runtime fichier unique**:

```
cypher.py (~1500 lignes)
├── Analyseur (ACGTFL → AST)
├── Compilateur (AST → Bytecode base-4)
├── Backends
│   ├── Web (HTML/CSS/JS)
│   └── Rust (API/Logique)
├── Système d'Entités (Gestion état)
└── CLI (Commandes)
```

---

## 🧪 Philosophy / Philosophie

### English

CYPHER embodies the principles of **living systems**:

1. **Minimal primitives** → Maximum composition
2. **Bio-inspired syntax** → Natural thinking
3. **Fixed state** → Stability guarantee
4. **Lifecycle execution** → Organic behavior
5. **Single source** → One language, many targets

### Français

CYPHER incarne les principes des **systèmes vivants**:

1. **Primitives minimales** → Composition maximale
2. **Syntaxe bio-inspirée** → Pensée naturelle
3. **État fixé** → Garantie de stabilité
4. **Exécution par cycle de vie** → Comportement organique
5. **Source unique** → Un langage, plusieurs cibles

---

## 📚 Documentation

- **[Primitives Reference](docs/primitives_functions.md)** - Complete primitive guide / Guide complet des primitives
- **[Examples](examples/)** - Sample CYPHER programs / Programmes CYPHER exemples
- **[API Reference](docs/api.md)** - Python API documentation / Documentation API Python

---

## 🤝 Contributing / Contribuer

### English

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Français

Nous accueillons les contributions ! Veuillez:

1. Fork le dépôt
2. Créer une branche de fonctionnalité
3. Écrire des tests pour nouvelles fonctionnalités
4. Soumettre une pull request

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour détails.

---

## 📜 License / Licence

MIT License - see [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Daouda Abdoul Anzize - Nexus Studio

---

## 👤 Author / Auteur

**Daouda Abdoul Anzize**
- 🏢 Nexus Studio
- 📧 nexusstudio100@gmail.com
- 🐙 GitHub: [@tryboy869](https://github.com/tryboy869)
- 🌐 Portfolio: [tryboy869.github.io/daa](https://tryboy869.github.io/daa)

---

## 🌟 Acknowledgments / Remerciements

### English

CYPHER builds on the shoulders of giants:
- **Forth** - For minimal runtime inspiration
- **Lisp** - For primitive-based composition
- **Lua** - For single-file simplicity
- **Nexus-Stellar** - For entity system foundation

### Français

CYPHER s'appuie sur les épaules de géants:
- **Forth** - Pour inspiration runtime minimal
- **Lisp** - Pour composition basée sur primitives
- **Lua** - Pour simplicité fichier unique
- **Nexus-Stellar** - Pour fondation système d'entités

---

## 🚀 Roadmap

### v0.1.0 (Current / Actuel)
- ✅ Core 6 primitives
- ✅ Web backend (HTML/CSS/JS)
- ✅ Rust backend (code generation)
- ✅ CLI tool
- ✅ Docker support

### v0.2.0 (Next / Prochain)
- 🔲 VS Code extension
- 🔲 Standard library (stdlib.cypher)
- 🔲 Package manager
- 🔲 Interactive REPL

### v1.0.0 (Future / Futur)
- 🔲 LSP (Language Server Protocol)
- 🔲 Debugger
- 🔲 AI agent integration
- 🔲 Native compilation

---

**CYPHER - Decrypt living systems** 🧬  
**CYPHER - Déchiffrez les systèmes vivants** 🧬