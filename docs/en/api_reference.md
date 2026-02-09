# CYPHER API Reference

## Functions

### execute_cypher()

Execute CYPHER source code.

**Signature:**
```python
def execute_cypher(source: str, contexts: List[str] = None) -> Dict[str, Any]
```

**Parameters:**
- `source` (str): CYPHER source code
- `contexts` (List[str], optional): Execution contexts. Defaults to ['backend']

**Returns:**
- Dict with context outputs and statistics

**Example:**
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
print(result['_stats'])    # Execution stats
```

### compile_cypher()

Compile CYPHER source to bytecode.

**Signature:**
```python
def compile_cypher(source: str) -> bytes
```

**Parameters:**
- `source` (str): CYPHER source code

**Returns:**
- bytes: Compiled bytecode

**Example:**
```python
from cypher import compile_cypher

bytecode = compile_cypher("""
A(test)
G(test;value:1)
F(test)
L(test)
""")

with open('output.cyb', 'wb') as f:
    f.write(bytecode)
```

## Classes

### CypherRuntime

Main runtime class.

**Methods:**
- `execute(source, contexts)` - Execute source code
- `compile(source)` - Compile to bytecode

### EvolutionConstraints

Represents evolution constraints for F operations.

**Attributes:**
- `min_value` (float): Minimum allowed value
- `max_value` (float): Maximum allowed value
- `allowed_states` (Set[str]): Allowed states
- `forbidden_states` (Set[str]): Forbidden states
- `adaptation_rate` (float): Evolution speed (0-1)
- `auto_evolve` (bool): Enable auto-evolution

**Methods:**
- `can_evolve_to(current_state, new_state)` - Check if evolution is allowed

## CLI

### cypher run

Run a CYPHER file.

```bash
cypher run <file.cy> [--contexts <contexts>]
```

### cypher build

Compile to bytecode.

```bash
cypher build <file.cy> [--output <output.cyb>]
```

### cypher version

Show version information.

```bash
cypher version
```
