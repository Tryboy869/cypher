#!/usr/bin/env python3
"""
CYPHER Programming Language v0.1.0
===================================
Minimalist programming language with unified hardware execution

Author: Daouda Abdoul Anzize
Organization: Nexus Studio
Email: nexusstudio100@gmail.com
License: MIT
Repository: https://github.com/tryboy869/cypher

Description:
A bio-inspired minimalist language with 8 primitives that auto-manages
hardware (CPU/GPU/Workers) and generates multi-context outputs (frontend,
backend, database) from a single source file.
"""

import re
import sys
import time
import json
import hashlib
from enum import IntEnum
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict
from pathlib import Path

__version__ = "0.1.0"
__author__ = "Daouda Abdoul Anzize"
__license__ = "MIT"

# ============================================================================
# SECTION 1: OPCODES AND DATA STRUCTURES
# ============================================================================

class Opcode(IntEnum):
    """The 8 core primitives of CYPHER"""
    A_CREATE = 0      # Allocate/Create entities
    C_CONNECT = 1     # Connect/Link entities
    G_GENERATE = 2    # Generate/Store data
    T_TRANSFORM = 3   # Transform/Compute
    F_FIX = 4         # Fix state with evolution constraints
    L_LIFE = 5        # Execute/Live
    I_IF = 6          # Conditional
    J_JUMP = 7        # Jump/Loop


@dataclass
class Operation:
    """Represents a single CYPHER operation"""
    opcode: Opcode
    entity: str
    params: Dict[str, Any]
    line: int
    
    def __hash__(self):
        return hash((self.opcode, self.entity, frozenset(self.params.items())))
    
    def to_bytecode(self) -> bytes:
        """Encode operation to 32-bit bytecode"""
        # [3-bit opcode][5-bit reserved][24-bit operand]
        opcode_bits = self.opcode.value << 29
        entity_hash = hash(self.entity) & 0xFFFFFF
        return (opcode_bits | entity_hash).to_bytes(4, 'big')


@dataclass
class EvolutionConstraints:
    """Evolution constraints for F (Fix) operation"""
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    allowed_states: Optional[Set[str]] = None
    forbidden_states: Optional[Set[str]] = None
    adaptation_rate: float = 0.1  # How fast state can evolve (0-1)
    auto_evolve: bool = True
    
    def can_evolve_to(self, current_state: Any, new_state: Any) -> bool:
        """Check if evolution from current to new state is allowed"""
        if not self.auto_evolve:
            return current_state == new_state
        
        # Check forbidden states
        if self.forbidden_states and new_state in self.forbidden_states:
            return False
        
        # Check allowed states
        if self.allowed_states and new_state not in self.allowed_states:
            return False
        
        # Check numeric constraints
        if self.min_value is not None and isinstance(new_state, (int, float)):
            if new_state < self.min_value:
                return False
        
        if self.max_value is not None and isinstance(new_state, (int, float)):
            if new_state > self.max_value:
                return False
        
        return True


@dataclass
class Gene:
    """A complete CYPHER gene (program)"""
    operations: List[Operation] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    constraints: Dict[str, EvolutionConstraints] = field(default_factory=dict)


# ============================================================================
# SECTION 2: PARSER
# ============================================================================

class CypherParser:
    """Parse CYPHER source code to AST"""
    
    OPCODE_MAP = {
        'A': Opcode.A_CREATE,
        'C': Opcode.C_CONNECT,
        'G': Opcode.G_GENERATE,
        'T': Opcode.T_TRANSFORM,
        'F': Opcode.F_FIX,
        'L': Opcode.L_LIFE,
        'I': Opcode.I_IF,
        'J': Opcode.J_JUMP,
    }
    
    def __init__(self):
        self.errors: List[str] = []
    
    def parse(self, source: str) -> Gene:
        """Parse source code to Gene"""
        gene = Gene()
        lines = source.strip().split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Remove inline comments
            if '#' in line:
                line = line[:line.index('#')].strip()
            
            try:
                operation = self._parse_line(line, line_num)
                if operation:
                    gene.operations.append(operation)
                    
                    # Extract constraints for F operations
                    if operation.opcode == Opcode.F_FIX:
                        constraints = self._extract_constraints(operation.params)
                        if constraints:
                            gene.constraints[operation.entity] = constraints
            
            except Exception as e:
                self.errors.append(f"Line {line_num}: {str(e)}")
        
        if self.errors:
            raise SyntaxError('\n'.join(self.errors))
        
        return gene
    
    def _parse_line(self, line: str, line_num: int) -> Optional[Operation]:
        """Parse a single line"""
        # Match pattern: OPCODE(entity;param1:value1;param2:value2)
        match = re.match(r'([ACGTFLIJ])\(([^)]+)\)', line)
        if not match:
            return None
        
        op_char, content = match.groups()
        opcode = self.OPCODE_MAP[op_char]
        
        entity, params = self._parse_params(content)
        
        return Operation(
            opcode=opcode,
            entity=entity,
            params=params,
            line=line_num
        )
    
    def _parse_params(self, content: str) -> Tuple[str, Dict[str, Any]]:
        """Parse entity and parameters"""
        parts = content.split(';')
        entity = parts[0].strip()
        params = {}
        
        for part in parts[1:]:
            if ':' in part:
                key, value = part.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"\'')
                
                # Type inference
                params[key] = self._infer_type(value)
        
        return entity, params
    
    def _infer_type(self, value: str) -> Any:
        """Infer type from string value"""
        # Boolean
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        
        # Integer
        if value.lstrip('-').isdigit():
            return int(value)
        
        # Float
        try:
            if '.' in value:
                return float(value)
        except ValueError:
            pass
        
        # List
        if value.startswith('[') and value.endswith(']'):
            items = value[1:-1].split(',')
            return [self._infer_type(item.strip()) for item in items if item.strip()]
        
        # String
        return value
    
    def _extract_constraints(self, params: Dict[str, Any]) -> Optional[EvolutionConstraints]:
        """Extract evolution constraints from F operation parameters"""
        if not any(k in params for k in ['min', 'max', 'allowed', 'forbidden', 'adapt_rate', 'auto_evolve']):
            return None
        
        constraints = EvolutionConstraints()
        
        if 'min' in params:
            constraints.min_value = float(params['min'])
        
        if 'max' in params:
            constraints.max_value = float(params['max'])
        
        if 'allowed' in params:
            allowed = params['allowed']
            constraints.allowed_states = set(allowed if isinstance(allowed, list) else [allowed])
        
        if 'forbidden' in params:
            forbidden = params['forbidden']
            constraints.forbidden_states = set(forbidden if isinstance(forbidden, list) else [forbidden])
        
        if 'adapt_rate' in params:
            constraints.adaptation_rate = float(params['adapt_rate'])
        
        if 'auto_evolve' in params:
            constraints.auto_evolve = bool(params['auto_evolve'])
        
        return constraints


# ============================================================================
# SECTION 3: HARDWARE MANAGER
# ============================================================================

class HardwareType(IntEnum):
    """Available hardware types"""
    CPU = 0
    GPU = 1
    WORKER = 2


class L1Cache:
    """L1 cache for hot execution paths"""
    def __init__(self, max_size: int = 1024):
        self.cache: Dict[int, HardwareType] = {}
        self.max_size = max_size
        self.hits = 0
        self.misses = 0
    
    def get(self, key: int) -> Optional[HardwareType]:
        """Get cached hardware decision"""
        if key in self.cache:
            self.hits += 1
            return self.cache[key]
        self.misses += 1
        return None
    
    def set(self, key: int, hardware: HardwareType):
        """Cache hardware decision"""
        if len(self.cache) >= self.max_size:
            # Evict oldest entry
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = hardware


class L2Cache:
    """L2 cache for warm execution paths"""
    def __init__(self, max_size: int = 8192):
        self.cache: Dict[int, HardwareType] = {}
        self.max_size = max_size
    
    def get(self, key: int) -> Optional[HardwareType]:
        """Get cached hardware decision"""
        return self.cache.get(key)
    
    def set(self, key: int, hardware: HardwareType):
        """Cache hardware decision"""
        if len(self.cache) >= self.max_size:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = hardware


class HardwareManager:
    """Unified hardware manager with auto-dispatch"""
    
    def __init__(self):
        self.l1_cache = L1Cache()
        self.l2_cache = L2Cache()
        self.stats = defaultdict(lambda: {'count': 0, 'time': 0.0})
        self.gpu_available = self._detect_gpu()
    
    def _detect_gpu(self) -> bool:
        """Detect if GPU is available"""
        try:
            # Try to detect CUDA or other GPU backends
            # For now, we'll simulate detection
            return False  # Set to True if GPU detected
        except:
            return False
    
    def auto_select(self, operation: Operation) -> HardwareType:
        """Auto-select hardware for operation"""
        op_hash = hash(operation)
        
        # Check L1 cache
        hardware = self.l1_cache.get(op_hash)
        if hardware is not None:
            return hardware
        
        # Check L2 cache
        hardware = self.l2_cache.get(op_hash)
        if hardware is not None:
            # Promote to L1
            self.l1_cache.set(op_hash, hardware)
            return hardware
        
        # Analyze and decide
        hardware = self._analyze_operation(operation)
        
        # Cache decision
        self.l2_cache.set(op_hash, hardware)
        
        return hardware
    
    def _analyze_operation(self, operation: Operation) -> HardwareType:
        """Analyze operation and decide hardware"""
        # Transform operations - potentially parallel
        if operation.opcode == Opcode.T_TRANSFORM:
            if 'validate' in operation.params or 'normalize' in operation.params:
                return HardwareType.GPU if self.gpu_available else HardwareType.CPU
        
        # Connect operations - async I/O
        if operation.opcode == Opcode.C_CONNECT:
            return HardwareType.WORKER
        
        # Default to CPU
        return HardwareType.CPU
    
    def execute(self, operation: Operation, hardware: HardwareType) -> float:
        """Execute operation on specified hardware"""
        start = time.time()
        
        # Simulate execution time based on hardware
        exec_times = {
            HardwareType.CPU: 0.001,
            HardwareType.GPU: 0.0002,
            HardwareType.WORKER: 0.0005,
        }
        
        time.sleep(exec_times[hardware])
        
        elapsed = time.time() - start
        self.stats[hardware]['count'] += 1
        self.stats[hardware]['time'] += elapsed
        
        return elapsed


# ============================================================================
# SECTION 4: CONTEXT EXECUTORS
# ============================================================================

class ContextExecutor:
    """Execute operations in specific context"""
    
    def __init__(self, context: str):
        self.context = context
        self.output = []
        self.state = {}
    
    def execute(self, operation: Operation, constraints: Optional[EvolutionConstraints] = None) -> str:
        """Execute operation in context"""
        if self.context == 'frontend':
            return self._frontend_output(operation)
        elif self.context == 'backend':
            return self._backend_output(operation)
        elif self.context == 'database':
            return self._database_output(operation)
        return ""
    
    def _frontend_output(self, op: Operation) -> str:
        """Generate HTML output"""
        if op.opcode == Opcode.A_CREATE:
            attrs = ' '.join(f'{k}="{v}"' for k, v in op.params.items() if k != 'type')
            tag = op.params.get('type', 'div')
            return f'<{tag} id="{op.entity}" {attrs}>'
        
        elif op.opcode == Opcode.G_GENERATE:
            content = []
            for k, v in op.params.items():
                if k in ['name', 'title', 'text', 'label']:
                    content.append(f'  <span class="{k}">{v}</span>')
                elif k == 'content':
                    content.append(f'  {v}')
            return '\n'.join(content) if content else ""
        
        elif op.opcode == Opcode.T_TRANSFORM:
            if 'style' in op.params:
                return f'  <style>.{op.entity} {{ {op.params["style"]} }}</style>'
            if 'render' in op.params:
                return f'  <!-- render: {op.params["render"]} -->'
        
        elif op.opcode == Opcode.F_FIX:
            return f'</{op.params.get("type", "div")}>'
        
        return ""
    
    def _backend_output(self, op: Operation) -> str:
        """Generate Rust-like backend code"""
        if op.opcode == Opcode.A_CREATE:
            return f'struct {op.entity.capitalize()} {{'
        
        elif op.opcode == Opcode.G_GENERATE:
            fields = []
            for k, v in op.params.items():
                type_ = self._infer_rust_type(v)
                fields.append(f'    {k}: {type_},')
            return '\n'.join(fields) if fields else ""
        
        elif op.opcode == Opcode.C_CONNECT:
            if 'database' in op.params.get('target', ''):
                return f'// Database connection: {op.params.get("target", "unknown")}'
            if 'endpoint' in op.params:
                return f'// API endpoint: {op.params["endpoint"]}'
        
        elif op.opcode == Opcode.T_TRANSFORM:
            if 'validate' in op.params:
                field = op.params['validate']
                return f'fn validate_{field}(value: &str) -> Result<bool, Error> {{ /* validation */ }}'
            if 'compute' in op.params:
                return f'fn compute_{op.entity}(data: &Data) -> Result<Output, Error> {{ /* computation */ }}'
        
        elif op.opcode == Opcode.I_IF:
            condition = op.params.get('condition', 'true')
            return f'if {condition} {{'
        
        elif op.opcode == Opcode.J_JUMP:
            return '}'
        
        elif op.opcode == Opcode.F_FIX:
            return '}'
        
        return ""
    
    def _database_output(self, op: Operation) -> str:
        """Generate SQL output"""
        if op.opcode == Opcode.A_CREATE:
            return f'CREATE TABLE {op.entity} ('
        
        elif op.opcode == Opcode.G_GENERATE:
            fields = []
            for k, v in op.params.items():
                type_ = self._infer_sql_type(v)
                fields.append(f'    {k} {type_},')
            return '\n'.join(fields) if fields else ""
        
        elif op.opcode == Opcode.C_CONNECT:
            if 'index' in op.params:
                return f'CREATE INDEX idx_{op.entity}_{op.params["index"]} ON {op.entity}({op.params["index"]});'
        
        elif op.opcode == Opcode.T_TRANSFORM:
            if 'query' in op.params:
                return f'-- Query: {op.params["query"]}'
        
        elif op.opcode == Opcode.F_FIX:
            return ');'
        
        return ""
    
    def _infer_rust_type(self, value: Any) -> str:
        """Infer Rust type from value"""
        if isinstance(value, bool):
            return 'bool'
        elif isinstance(value, int):
            return 'i32'
        elif isinstance(value, float):
            return 'f64'
        elif isinstance(value, list):
            return 'Vec<String>'
        else:
            return 'String'
    
    def _infer_sql_type(self, value: Any) -> str:
        """Infer SQL type from value"""
        if isinstance(value, bool):
            return 'BOOLEAN'
        elif isinstance(value, int):
            return 'INTEGER'
        elif isinstance(value, float):
            return 'REAL'
        else:
            return 'VARCHAR(255)'


# ============================================================================
# SECTION 5: RUNTIME
# ============================================================================

class CypherRuntime:
    """Main CYPHER runtime"""
    
    def __init__(self):
        self.parser = CypherParser()
        self.hardware = HardwareManager()
        self.version = __version__
    
    def execute(self, source: str, contexts: List[str] = None) -> Dict[str, Any]:
        """Execute CYPHER source code"""
        if contexts is None:
            contexts = ['backend']
        
        # Parse
        gene = self.parser.parse(source)
        
        # Execute in each context
        results = {}
        for ctx in contexts:
            executor = ContextExecutor(ctx)
            ctx_output = []
            
            for op in gene.operations:
                # Auto-select hardware
                hardware = self.hardware.auto_select(op)
                
                # Execute with timing
                exec_time = self.hardware.execute(op, hardware)
                
                # Generate context output
                constraints = gene.constraints.get(op.entity)
                output = executor.execute(op, constraints)
                
                if output:
                    ctx_output.append(output)
            
            results[ctx] = '\n'.join(ctx_output)
        
        # Add statistics
        results['_stats'] = self._get_stats()
        results['_version'] = self.version
        
        return results
    
    def compile(self, source: str) -> bytes:
        """Compile source to bytecode"""
        gene = self.parser.parse(source)
        bytecode = b''
        
        # Add header
        header = f"CYPHER{self.version}".encode('utf-8').ljust(32, b'\x00')
        bytecode += header
        
        # Add operations
        for op in gene.operations:
            bytecode += op.to_bytecode()
        
        return bytecode
    
    def _get_stats(self) -> Dict:
        """Get execution statistics"""
        return {
            'hardware_usage': dict(self.hardware.stats),
            'cache_hits': self.hardware.l1_cache.hits,
            'cache_misses': self.hardware.l1_cache.misses,
            'cache_hit_rate': self.hardware.l1_cache.hits / 
                            (self.hardware.l1_cache.hits + self.hardware.l1_cache.misses)
                            if (self.hardware.l1_cache.hits + self.hardware.l1_cache.misses) > 0 
                            else 0,
            'gpu_available': self.hardware.gpu_available
        }


# ============================================================================
# SECTION 6: CLI
# ============================================================================

def cli():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='CYPHER Programming Language v' + __version__
    )
    
    parser.add_argument('command', choices=['run', 'build', 'version'],
                       help='Command to execute')
    parser.add_argument('file', nargs='?', help='CYPHER source file (.cy)')
    parser.add_argument('--contexts', '-c', default='backend',
                       help='Execution contexts (comma-separated)')
    parser.add_argument('--output', '-o', help='Output file for build command')
    
    args = parser.parse_args()
    
    if args.command == 'version':
        print(f"CYPHER v{__version__}")
        print(f"Author: {__author__}")
        print(f"License: {__license__}")
        return
    
    if not args.file:
        print("Error: file argument required")
        sys.exit(1)
    
    # Read source file
    try:
        with open(args.file, 'r') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found")
        sys.exit(1)
    
    runtime = CypherRuntime()
    
    if args.command == 'run':
        contexts = args.contexts.split(',')
        results = runtime.execute(source, contexts)
        
        for ctx in contexts:
            print(f"\n{'='*60}")
            print(f"{ctx.upper()} OUTPUT")
            print(f"{'='*60}")
            print(results[ctx])
        
        # Print stats
        print(f"\n{'='*60}")
        print("STATISTICS")
        print(f"{'='*60}")
        stats = results['_stats']
        print(f"Cache hit rate: {stats['cache_hit_rate']*100:.1f}%")
        print(f"GPU available: {stats['gpu_available']}")
    
    elif args.command == 'build':
        bytecode = runtime.compile(source)
        output = args.output or args.file.replace('.cy', '.cyb')
        
        with open(output, 'wb') as f:
            f.write(bytecode)
        
        print(f"Compiled to: {output}")
        print(f"Size: {len(bytecode)} bytes")


# ============================================================================
# SECTION 7: PUBLIC API
# ============================================================================

def execute_cypher(source: str, contexts: List[str] = None) -> Dict[str, Any]:
    """Execute CYPHER source code
    
    Args:
        source: CYPHER source code
        contexts: List of contexts to execute in (frontend, backend, database)
    
    Returns:
        Dictionary with context outputs and statistics
    """
    runtime = CypherRuntime()
    return runtime.execute(source, contexts)


def compile_cypher(source: str) -> bytes:
    """Compile CYPHER source to bytecode
    
    Args:
        source: CYPHER source code
    
    Returns:
        Bytecode bytes
    """
    runtime = CypherRuntime()
    return runtime.compile(source)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    cli()
