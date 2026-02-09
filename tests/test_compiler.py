import pytest
from cypher import compile_cypher

def test_compile_basic():
    bytecode = compile_cypher("""
    A(test)
    G(test;value:1)
    F(test)
    L(test)
    """)
    assert isinstance(bytecode, bytes)
    assert len(bytecode) > 32  # Header + operations
    assert bytecode.startswith(b'CYPHER')

def test_compile_empty():
    bytecode = compile_cypher("")
    assert isinstance(bytecode, bytes)
