# 🧬 CYPHER Programming Language

**Version:** 0.1.0  
**Author:** Daouda Abdoul Anzize  
**Organization:** Nexus Studio  
**License:** MIT

---

## 🌟 What is CYPHER?

CYPHER is a **minimalist programming language** inspired by biological information processing concepts, featuring:

- **8 core primitives** for all operations
- **Unified architecture** - one source file generates frontend, backend, and database code
- **Automatic hardware optimization** - transparent CPU/GPU/Worker management  
- **Single-file runtime** - entire language in ~1,800 lines
- **Zero-dependency deployment**

## 🚀 Quick Start

### Installation

```bash
pip install cypher-lang
```

### Your First Program

Create `hello.cy`:

```cypher
# Hello World in CYPHER
A(greeting)
G(greeting;text:Hello, CYPHER!)
T(greeting;render:console)
F(greeting;fixed)
L(greeting;life)
```

Run it:

```bash
cypher run hello.cy
```

## 📚 The 8 Primitives

| Primitive | Function | Example |
|-----------|----------|---------|
| **A** | Create/Allocate | `A(user)` |
| **C** | Connect/Link | `C(database)` |
| **G** | Generate/Store | `G(name:Alice)` |
| **T** | Transform/Compute | `T(validate:email)` |
| **F** | Fix with constraints | `F(min:0;max:100)` |
| **L** | Execute/Live | `L(life)` |
| **I** | Conditional | `I(condition)` |
| **J** | Jump/Loop | `J(label)` |

## 💡 Key Features

### Multi-Context Execution

One CYPHER file generates multiple outputs:

```cypher
A(user)
G(user;name:Alice;email:alice@example.com)
C(user;database)
T(user;validate:email)
F(user;fixed)
L(user;life)
```

Outputs:
- **Frontend**: HTML user interface
- **Backend**: Rust-like API code
- **Database**: SQL schema

### Automatic Hardware Management

CYPHER automatically selects the best hardware:

```cypher
A(processing)
T(processing;normalize:data)  # → Auto-routed to GPU if available
C(processing;database)         # → Auto-routed to async Workers
F(processing;fixed)
L(processing;life)
```

### Evolution Constraints (F Primitive)

Define state boundaries with auto-evolution:

```cypher
# Temperature controller with safety limits
A(temperature)
G(temperature;value:20)
F(temperature;min:15;max:30;auto_evolve:true;adapt_rate:0.1)
L(temperature;life)
```

## 📖 Documentation

- [English Documentation](./docs/en/)
- [Documentation Française](./docs/fr/)
- [Examples](./examples/)
- [API Reference](./docs/en/api_reference.md)

## 🧪 Examples

### Web Application

```cypher
A(dashboard)
G(dashboard;title:Analytics Dashboard)
T(dashboard;layout:grid)
C(dashboard;api)
F(dashboard;fixed)
L(dashboard;life)
```

### API Server

```cypher
A(get_users)
G(get_users;endpoint:/api/users;method:GET)
C(get_users;database)
T(get_users;format:json)
F(get_users;fixed)
L(get_users;life)
```

## 🔧 CLI Commands

```bash
# Run CYPHER file
cypher run app.cy

# Compile to bytecode  
cypher build app.cy

# Multi-context execution
cypher run app.cy --contexts frontend,backend,database

# Version info
cypher version
```

## 🐍 Python API

```python
from cypher import execute_cypher

result = execute_cypher("""
A(user)
G(user;name:Alice)
F(user;fixed)
L(user;life)
""", contexts=['frontend', 'backend'])

print(result['frontend'])  # HTML output
print(result['backend'])   # Backend code
```

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 License

MIT License - see [LICENSE](./LICENSE)

## 🔗 Links

- [GitHub](https://github.com/tryboy869/cypher)
- [PyPI](https://pypi.org/project/cypher-lang/)
- [Documentation](./docs/)

---

**Made with ❤️ by Nexus Studio**
