# Démarrage avec CYPHER

## Installation

Installez CYPHER depuis PyPI:

```bash
pip install cypher-lang
```

## Votre Premier Programme

Créez un fichier `hello.cy`:

```cypher
A(salutation)
G(salutation;texte:Bonjour, CYPHER!)
F(salutation;fixe)
L(salutation;vie)
```

Exécutez-le:

```bash
cypher run hello.cy
```

## Syntaxe de Base

CYPHER utilise 8 primitives:

- **A(entite)** - Créer/Allouer
- **C(entite;cible)** - Connecter/Lier
- **G(entite;cle:valeur)** - Générer/Stocker données
- **T(entite;operation)** - Transformer/Calculer
- **F(entite;contraintes)** - Fixer l'état avec limites d'évolution
- **L(entite)** - Exécuter/Vivre
- **I(entite;condition)** - Conditionnel
- **J(entite;label)** - Saut/Boucle

## Exécution Multi-Contexte

Un fichier CYPHER peut générer du code pour plusieurs contextes:

```bash
cypher run app.cy --contexts frontend,backend,database
```

Cela produira du HTML, du code backend et du SQL depuis la même source.

## Prochaines Étapes

- Lisez la [Référence des Primitives](./reference_primitives.md)
- Explorez les [Exemples](../../examples/)
- Consultez la [Référence API](./reference_api.md)
