#!/usr/bin/env python3
import time
from cypher import execute_cypher

def benchmark_execution(iterations=100):
    code = """
    A(user)
    G(user;name:Alice;email:test@example.com)
    C(user;database)
    T(user;validate:email)
    F(user;fixed)
    L(user;life)
    """
    
    start = time.time()
    for _ in range(iterations):
        execute_cypher(code, contexts=['backend'])
    elapsed = time.time() - start
    
    print(f"Iterations: {iterations}")
    print(f"Total time: {elapsed:.2f}s")
    print(f"Avg time: {(elapsed/iterations)*1000:.2f}ms")
    print(f"Ops/sec: {iterations/elapsed:.0f}")

if __name__ == '__main__':
    benchmark_execution()
