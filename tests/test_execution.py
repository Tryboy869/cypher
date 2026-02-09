import pytest
from cypher import execute_cypher

def test_execute_basic():
    result = execute_cypher("""
    A(test)
    G(test;value:hello)
    F(test;fixed)
    L(test;life)
    """, contexts=['backend'])
    assert 'backend' in result
    assert '_stats' in result

def test_execute_multicontext():
    result = execute_cypher("""
    A(user)
    G(user;name:Alice)
    F(user;fixed)
    L(user;life)
    """, contexts=['frontend', 'backend', 'database'])
    assert 'frontend' in result
    assert 'backend' in result
    assert 'database' in result

def test_cache_stats():
    code = "A(item);G(item;val:1);F(item);L(life)"
    # Run twice to test cache
    execute_cypher(code)
    result = execute_cypher(code)
    stats = result['_stats']
    assert 'cache_hit_rate' in stats
