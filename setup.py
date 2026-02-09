from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme = Path("README.md").read_text(encoding="utf-8") if Path("README.md").exists() else ""

setup(
    name="cypher-lang",
    version="0.1.0",
    author="Daouda Abdoul Anzize",
    author_email="nexusstudio100@gmail.com",
    description="Minimalist programming language with 8 primitives and unified hardware execution",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/tryboy869/cypher",
    project_urls={
        "Bug Tracker": "https://github.com/tryboy869/cypher/issues",
        "Documentation": "https://github.com/tryboy869/cypher/tree/main/docs",
        "Source Code": "https://github.com/tryboy869/cypher",
    },
    py_modules=["cypher"],
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
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "cypher=cypher:cli",
        ],
    },
    keywords="programming-language compiler interpreter minimalist bio-inspired",
    include_package_data=True,
    zip_safe=False,
)
