"""
Setup configuration for CYPHER language
Configuration d'installation pour le langage CYPHER
"""

from setuptools import setup
from pathlib import Path

# Read README / Lire README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ""

setup(
    name="cypher-lang",
    version="0.1.0",
    
    # Single-file module / Module fichier unique
    py_modules=["cypher"],
    
    # Dependencies / Dépendances
    install_requires=[
        # No external dependencies for core runtime
        # Pas de dépendances externes pour runtime de base
    ],
    
    # Optional dependencies / Dépendances optionnelles
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=23.0.0',
            'mypy>=1.0.0',
        ],
    },
    
    # CLI entry point / Point d'entrée CLI
    entry_points={
        "console_scripts": [
            "cypher=cypher:main",
        ],
    },
    
    # Metadata / Métadonnées
    author="Daouda Abdoul Anzize",
    author_email="nexusstudio100@gmail.com",
    
    description="Bio-inspired programming language with 6 primitives",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    url="https://github.com/tryboy869/cypher",
    project_urls={
        "Bug Tracker": "https://github.com/tryboy869/cypher/issues",
        "Documentation": "https://github.com/tryboy869/cypher/docs",
        "Source Code": "https://github.com/tryboy869/cypher",
    },
    
    license="MIT",
    
    # Classifiers / Classificateurs
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Natural Language :: French",
    ],
    
    keywords=[
        "cypher",
        "bio-inspired",
        "programming-language",
        "compiler",
        "dna",
        "primitives",
        "langage-programmation",
        "bio-inspiré",
    ],
    
    python_requires=">=3.8",
    
    # Package data / Données du package
    include_package_data=True,
    package_data={
        "": ["README.md", "LICENSE", "examples/*.cypher", "docs/*.md"],
    },
    
    zip_safe=False,
)