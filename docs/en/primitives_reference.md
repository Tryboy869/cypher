# CYPHER Primitives Reference

## A - Create/Allocate

Creates a new entity.

**Syntax:** `A(entity_name)`

**Example:**
```cypher
A(user)
A(database)
A(api_server)
```

## C - Connect/Link

Connects entities together.

**Syntax:** `C(entity;target:value)`

**Example:**
```cypher
C(user;database)
C(api;endpoint:/users)
```

## G - Generate/Store

Generates or stores data in an entity.

**Syntax:** `G(entity;key:value;key2:value2)`

**Example:**
```cypher
G(user;name:Alice;age:25)
G(config;host:localhost;port:8080)
```

## T - Transform/Compute

Applies transformations or computations.

**Syntax:** `T(entity;operation:params)`

**Example:**
```cypher
T(data;validate:email)
T(numbers;sort:ascending)
T(text;format:uppercase)
```

## F - Fix with Evolution Constraints

Fixes state while defining evolution boundaries and auto-adaptation rules.

**Syntax:** `F(entity;min:value;max:value;auto_evolve:bool)`

**Parameters:**
- `min` - Minimum allowed value
- `max` - Maximum allowed value
- `allowed` - List of allowed states
- `forbidden` - List of forbidden states
- `auto_evolve` - Enable auto-evolution (default: true)
- `adapt_rate` - Evolution speed 0-1 (default: 0.1)

**Example:**
```cypher
# Numeric constraints
F(temperature;min:15;max:30;auto_evolve:true)

# State constraints
F(status;allowed:[pending,active,done];auto_evolve:true)

# Adaptive system
F(load;min:0;max:100;adapt_rate:0.2;auto_evolve:true)
```

The F primitive allows systems to:
- Define safety boundaries
- Auto-adapt within constraints
- Prevent invalid states
- Enable controlled evolution

## L - Execute/Live

Executes the gene/program.

**Syntax:** `L(entity)`

**Example:**
```cypher
L(application)
L(life)
```

## I - Conditional

Conditional branching.

**Syntax:** `I(entity;condition)`

**Example:**
```cypher
I(user;age >= 18)
G(user;status:adult)
J(user;end)
```

## J - Jump/Loop

Jump or loop control.

**Syntax:** `J(label)`

**Example:**
```cypher
J(end)
J(loop_start)
```

## Complete Example

```cypher
# User registration system
A(user)
G(user;name:Alice;email:alice@example.com;age:25)
T(user;validate:email)
I(user;age >= 18)
G(user;status:approved)
C(user;database)
F(user;fixed)
J(user;end)
G(user;status:rejected)
F(user;fixed)
L(user;life)
```
