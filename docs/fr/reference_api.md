# Référence API CYPHER

## Fonctions

### execute_cypher()

Exécute du code source CYPHER.

**Signature:**
```python
def execute_cypher(source: str, contexts: List[str] = None) -> Dict[str, Any]
```

**Paramètres:**
- `source` (str): Code source CYPHER
- `contexts` (List[str], optionnel): Contextes d'exécution. Par défaut ['backend']

**Retourne:**
- Dict avec sorties par contexte et statistiques

**Exemple:**
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
print(resultat['_stats'])    # Stats d'exécution
```

### compile_cypher()

Compile le source CYPHER en bytecode.

**Signature:**
```python
def compile_cypher(source: str) -> bytes
```

**Paramètres:**
- `source` (str): Code source CYPHER

**Retourne:**
- bytes: Bytecode compilé

**Exemple:**
```python
from cypher import compile_cypher

bytecode = compile_cypher("""
A(test)
G(test;valeur:1)
F(test)
L(test)
""")

with open('output.cyb', 'wb') as f:
    f.write(bytecode)
```

## Classes

### CypherRuntime

Classe runtime principale.

**Méthodes:**
- `execute(source, contexts)` - Exécuter le code source
- `compile(source)` - Compiler en bytecode

### EvolutionConstraints

Représente les contraintes d'évolution pour les opérations F.

**Attributs:**
- `min_value` (float): Valeur minimale autorisée
- `max_value` (float): Valeur maximale autorisée
- `allowed_states` (Set[str]): États autorisés
- `forbidden_states` (Set[str]): États interdits
- `adaptation_rate` (float): Vitesse d'évolution (0-1)
- `auto_evolve` (bool): Activer l'auto-évolution

**Méthodes:**
- `can_evolve_to(etat_actuel, nouvel_etat)` - Vérifier si l'évolution est autorisée

## CLI

### cypher run

Exécuter un fichier CYPHER.

```bash
cypher run <fichier.cy> [--contexts <contextes>]
```

### cypher build

Compiler en bytecode.

```bash
cypher build <fichier.cy> [--output <sortie.cyb>]
```

### cypher version

Afficher les informations de version.

```bash
cypher version
```
