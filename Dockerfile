FROM python:3.11-slim as base

# Metadata / Métadonnées
LABEL maintainer="Daouda Abdoul Anzize <nexusstudio100@gmail.com>"
LABEL description="CYPHER v0.1.0 - Bio-inspired programming language runtime"
LABEL description.fr="CYPHER v0.1.0 - Runtime du langage de programmation bio-inspiré"
LABEL version="0.1.0"

# Install system dependencies / Installer dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    gcc \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Rust / Installer Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Install Node.js (for web backend if needed) / Installer Node.js (pour backend web si nécessaire)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

# Set working directory / Définir répertoire de travail
WORKDIR /cypher

# Copy CYPHER runtime / Copier runtime CYPHER
COPY cypher.py .
COPY setup.py .
COPY README.md .
COPY LICENSE .

# Copy examples / Copier exemples
COPY examples/ ./examples/

# Copy documentation / Copier documentation
COPY docs/ ./docs/

# Install CYPHER / Installer CYPHER
RUN pip install --no-cache-dir -e .

# Bootstrap backends (compile cache) / Démarrer backends (cache compilation)
RUN python -c "from cypher import CypherRuntime; CypherRuntime()" || true

# Create cache directory / Créer répertoire cache
RUN mkdir -p /root/.cypher_cache

# Expose port for web server (future) / Exposer port pour serveur web (futur)
EXPOSE 8000

# Entry point / Point d'entrée
ENTRYPOINT ["python", "cypher.py"]

# Default command shows help / Commande par défaut affiche aide
CMD ["help"]

# Usage examples / Exemples d'utilisation:
# docker build -t cypher:0.1.0 .
# docker run -v $(pwd)/app.cypher:/app.cypher cypher:0.1.0 run /app.cypher
# docker run -it cypher:0.1.0 version