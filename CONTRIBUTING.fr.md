# Contribuer à CYPHER

Merci de votre intérêt pour contribuer à CYPHER!

## Comment Contribuer

1. **Forkez le dépôt**
2. **Créez une branche feature** (`git checkout -b feature/fonctionnalite-geniale`)
3. **Faites vos modifications**
4. **Lancez les tests** (`pytest tests/`)
5. **Committez vos changements** (`git commit -m 'Ajout fonctionnalité géniale'`)
6. **Poussez vers la branche** (`git push origin feature/fonctionnalite-geniale`)
7. **Ouvrez une Pull Request**

## Configuration Développement

```bash
git clone https://github.com/tryboy869/cypher.git
cd cypher
pip install -e ".[dev]"
```

## Lancer les Tests

```bash
pytest tests/ -v
```

## Style de Code

- Suivre PEP 8
- Utiliser des noms de variables significatifs
- Ajouter des docstrings aux fonctions
- Garder les fonctions focalisées et petites

## Signaler des Problèmes

Utilisez GitHub Issues pour signaler des bugs ou suggérer des fonctionnalités.

Inclure:
- Version CYPHER
- Version Python
- Système d'exploitation
- Exemple de code minimal
- Comportement attendu vs réel

## Licence

En contribuant, vous acceptez que vos contributions soient licenciées sous la Licence MIT.
