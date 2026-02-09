# Référence des Primitives CYPHER

## A - Créer/Allouer

Crée une nouvelle entité.

**Syntaxe:** `A(nom_entite)`

**Exemple:**
```cypher
A(utilisateur)
A(base_donnees)
A(serveur_api)
```

## C - Connecter/Lier

Connecte des entités ensemble.

**Syntaxe:** `C(entite;cible:valeur)`

**Exemple:**
```cypher
C(utilisateur;base_donnees)
C(api;endpoint:/utilisateurs)
```

## G - Générer/Stocker

Génère ou stocke des données dans une entité.

**Syntaxe:** `G(entite;cle:valeur;cle2:valeur2)`

**Exemple:**
```cypher
G(utilisateur;nom:Alice;age:25)
G(config;hote:localhost;port:8080)
```

## T - Transformer/Calculer

Applique des transformations ou calculs.

**Syntaxe:** `T(entite;operation:params)`

**Exemple:**
```cypher
T(donnees;valider:email)
T(nombres;trier:croissant)
T(texte;format:majuscules)
```

## F - Fixer avec Contraintes d'Évolution

Fixe l'état tout en définissant des limites d'évolution et règles d'auto-adaptation.

**Syntaxe:** `F(entite;min:valeur;max:valeur;auto_evolve:bool)`

**Paramètres:**
- `min` - Valeur minimale autorisée
- `max` - Valeur maximale autorisée
- `allowed` - Liste des états autorisés
- `forbidden` - Liste des états interdits
- `auto_evolve` - Activer l'auto-évolution (défaut: true)
- `adapt_rate` - Vitesse d'évolution 0-1 (défaut: 0.1)

**Exemple:**
```cypher
# Contraintes numériques
F(temperature;min:15;max:30;auto_evolve:true)

# Contraintes d'états
F(statut;allowed:[en_attente,actif,termine];auto_evolve:true)

# Système adaptatif
F(charge;min:0;max:100;adapt_rate:0.2;auto_evolve:true)
```

La primitive F permet aux systèmes de:
- Définir des limites de sécurité
- S'auto-adapter dans les contraintes
- Prévenir les états invalides
- Activer l'évolution contrôlée

## L - Exécuter/Vivre

Exécute le gène/programme.

**Syntaxe:** `L(entite)`

**Exemple:**
```cypher
L(application)
L(vie)
```

## I - Conditionnel

Branchement conditionnel.

**Syntaxe:** `I(entite;condition)`

**Exemple:**
```cypher
I(utilisateur;age >= 18)
G(utilisateur;statut:adulte)
J(utilisateur;fin)
```

## J - Saut/Boucle

Contrôle de saut ou boucle.

**Syntaxe:** `J(label)`

**Exemple:**
```cypher
J(fin)
J(debut_boucle)
```

## Exemple Complet

```cypher
# Système d'inscription utilisateur
A(utilisateur)
G(utilisateur;nom:Alice;email:alice@example.com;age:25)
T(utilisateur;valider:email)
I(utilisateur;age >= 18)
G(utilisateur;statut:approuve)
C(utilisateur;base_donnees)
F(utilisateur;fixe)
J(utilisateur;fin)
G(utilisateur;statut:rejete)
F(utilisateur;fixe)
L(utilisateur;vie)
```
