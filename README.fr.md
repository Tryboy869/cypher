# 🧬 Langage de Programmation CYPHER

**Version:** 0.1.0  
**Auteur:** Daouda Abdoul Anzize  
**Organisation:** Nexus Studio  
**Licence:** MIT

---

## 🌟 Qu'est-ce que CYPHER ?

CYPHER est un **langage de programmation minimaliste** inspiré par les concepts de traitement de l'information biologique, avec :

- **8 primitives fondamentales** pour toutes les opérations
- **Architecture unifiée** - un fichier source génère le frontend, backend et la base de données
- **Optimisation matérielle automatique** - gestion transparente CPU/GPU/Workers
- **Runtime mono-fichier** - tout le langage en ~1,800 lignes
- **Déploiement sans dépendances**

## 🚀 Démarrage Rapide

### Installation

```bash
pip install cypher-lang
```

### Votre Premier Programme

Créez `hello.cy`:

```cypher
# Hello World en CYPHER
A(salutation)
G(salutation;texte:Bonjour, CYPHER!)
T(salutation;rendu:console)
F(salutation;fixe)
L(salutation;vie)
```

Exécutez-le:

```bash
cypher run hello.cy
```

## 📚 Les 8 Primitives

| Primitive | Fonction | Exemple |
|-----------|----------|---------|
| **A** | Créer/Allouer | `A(utilisateur)` |
| **C** | Connecter/Lier | `C(base_donnees)` |
| **G** | Générer/Stocker | `G(nom:Alice)` |
| **T** | Transformer/Calculer | `T(valider:email)` |
| **F** | Fixer avec contraintes | `F(min:0;max:100)` |
| **L** | Exécuter/Vivre | `L(vie)` |
| **I** | Conditionnel | `I(condition)` |
| **J** | Saut/Boucle | `J(label)` |

## 💡 Fonctionnalités Clés

### Exécution Multi-Contexte

Un fichier CYPHER génère plusieurs sorties:

```cypher
A(utilisateur)
G(utilisateur;nom:Alice;email:alice@example.com)
C(utilisateur;base_donnees)
T(utilisateur;valider:email)
F(utilisateur;fixe)
L(utilisateur;vie)
```

Sorties:
- **Frontend**: Interface utilisateur HTML
- **Backend**: Code API type Rust
- **Base de données**: Schéma SQL

### Gestion Matérielle Automatique

CYPHER sélectionne automatiquement le meilleur matériel:

```cypher
A(traitement)
T(traitement;normaliser:donnees)  # → Auto-routé vers GPU si disponible
C(traitement;base_donnees)         # → Auto-routé vers Workers async
F(traitement;fixe)
L(traitement;vie)
```

### Contraintes d'Évolution (Primitive F)

Définissez des limites d'état avec auto-évolution:

```cypher
# Contrôleur de température avec limites de sécurité
A(temperature)
G(temperature;valeur:20)
F(temperature;min:15;max:30;auto_evolve:true;adapt_rate:0.1)
L(temperature;vie)
```

## 📖 Documentation

- [Documentation Anglaise](./docs/en/)
- [Documentation Française](./docs/fr/)
- [Exemples](./examples/)
- [Référence API](./docs/fr/reference_api.md)

## 🔧 Commandes CLI

```bash
# Exécuter un fichier CYPHER
cypher run app.cy

# Compiler en bytecode
cypher build app.cy

# Exécution multi-contexte
cypher run app.cy --contexts frontend,backend,database

# Info version
cypher version
```

## 🐍 API Python

```python
from cypher import execute_cypher

resultat = execute_cypher("""
A(utilisateur)
G(utilisateur;nom:Alice)
F(utilisateur;fixe)
L(utilisateur;vie)
""", contexts=['frontend', 'backend'])

print(resultat['frontend'])  # Sortie HTML
print(resultat['backend'])   # Code backend
```

## 🤝 Contribution

Les contributions sont les bienvenues! Voir [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 Licence

Licence MIT - voir [LICENSE](./LICENSE)

## 🔗 Liens

- [GitHub](https://github.com/tryboy869/cypher)
- [PyPI](https://pypi.org/project/cypher-lang/)
- [Documentation](./docs/)

---

**Fait avec ❤️ par Nexus Studio**
