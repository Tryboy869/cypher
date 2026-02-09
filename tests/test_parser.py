import pytest
from cypher import CypherParser, Opcode

def test_parse_basic():
    parser = CypherParser()
    gene = parser.parse("""
    A(user)
    G(user;name:Alice)
    F(user;fixed)
    L(user;life)
    """)
    assert len(gene.operations) == 4
    assert gene.operations[0].opcode == Opcode.A_CREATE
    assert gene.operations[0].entity == "user"

def test_parse_with_params():
    parser = CypherParser()
    gene = parser.parse("G(user;name:Alice;age:25;active:true)")
    op = gene.operations[0]
    assert op.params['name'] == 'Alice'
    assert op.params['age'] == 25
    assert op.params['active'] == True

def test_parse_comments():
    parser = CypherParser()
    gene = parser.parse("""
    # This is a comment
    A(user)  # inline comment
    G(user;data:test)
    """)
    assert len(gene.operations) == 2

def test_parse_evolution_constraints():
    parser = CypherParser()
    gene = parser.parse("F(temp;min:0;max:100;auto_evolve:true)")
    assert 'temp' in gene.constraints
    constraints = gene.constraints['temp']
    assert constraints.min_value == 0
    assert constraints.max_value == 100
    assert constraints.auto_evolve == True

def test_invalid_syntax():
    parser = CypherParser()
    with pytest.raises(SyntaxError):
        parser.parse("INVALID(syntax")
