# Getting Started with CYPHER

## Installation

Install CYPHER from PyPI:

```bash
pip install cypher-lang
```

## Your First Program

Create a file `hello.cy`:

```cypher
A(greeting)
G(greeting;text:Hello, CYPHER!)
F(greeting;fixed)
L(greeting;life)
```

Run it:

```bash
cypher run hello.cy
```

## Basic Syntax

CYPHER uses 8 primitives:

- **A(entity)** - Create/Allocate
- **C(entity;target)** - Connect/Link
- **G(entity;key:value)** - Generate/Store data
- **T(entity;operation)** - Transform/Compute
- **F(entity;constraints)** - Fix state with evolution boundaries
- **L(entity)** - Execute/Live
- **I(entity;condition)** - Conditional
- **J(entity;label)** - Jump/Loop

## Multi-Context Execution

One CYPHER file can generate code for multiple contexts:

```bash
cypher run app.cy --contexts frontend,backend,database
```

This will output HTML, backend code, and SQL from the same source.

## Next Steps

- Read the [Primitives Reference](./primitives_reference.md)
- Explore [Examples](../../examples/)
- Check the [API Reference](./api_reference.md)
