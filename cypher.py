"""
CYPHER v0.1.0
Bio-inspired programming language with 6 primitives
Langage de programmation bio-inspiré avec 6 primitives

Author: Daouda Abdoul Anzize
Organization: Nexus Studio
Contact: nexusstudio100@gmail.com
GitHub: https://github.com/tryboy869/cypher
License: MIT

Changelog v0.1.0:
- Initial release / Version initiale
- 6 core primitives (ACGTFL)
- Rust + Web backends
- Entity system from Nexus-Stellar
- Single-file runtime (~1500 lines)
"""

import subprocess
import ctypes
import os
import sys
import json
import hashlib
import time
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum

# ============================================================
# PRIMITIVES / PRIMITIVES
# ============================================================

class PrimitiveType(Enum):
    """Core CYPHER primitives / Primitives de base CYPHER"""
    CREATE = 'A'      # Create entity / Créer entité
    CONNECT = 'C'     # Connect entities / Connecter entités
    GENERATE = 'G'    # Generate content / Générer contenu
    TRANSFORM = 'T'   # Transform style/behavior / Transformer style/comportement
    FIX = 'F'         # Fix state / Fixer état
    LIFE = 'L'        # Launch execution / Lancer exécution

@dataclass
class Instruction:
    """Single CYPHER instruction / Instruction CYPHER unique"""
    primitive: PrimitiveType
    params: Dict[str, Any]
    line: int
    context: str = 'general'

@dataclass
class AST:
    """Abstract Syntax Tree / Arbre de syntaxe abstrait"""
    instructions: List[Instruction]
    metadata: Dict[str, Any]

# ============================================================
# PARSER / ANALYSEUR
# ============================================================

class CypherParser:
    """
    Parse CYPHER code into AST
    Analyse le code CYPHER en AST
    """
    
    PRIMITIVES = {
        'A': PrimitiveType.CREATE,
        'C': PrimitiveType.CONNECT,
        'G': PrimitiveType.GENERATE,
        'T': PrimitiveType.TRANSFORM,
        'F': PrimitiveType.FIX,
        'L': PrimitiveType.LIFE
    }
    
    def __init__(self):
        self.current_line = 0
    
    def parse(self, source: str) -> AST:
        """
        Parse source code to AST
        Analyse le code source en AST
        """
        instructions = []
        lines = source.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            self.current_line = line_num
            
            # Skip comments and empty lines / Ignorer commentaires et lignes vides
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # Parse gene (line ending with :)
            # Analyser gène (ligne se terminant par :)
            if line.endswith(':'):
                line = line[:-1]  # Remove trailing : / Retirer : final
            
            # Split instructions by ; / Diviser instructions par ;
            parts = line.split(';')
            
            for part in parts:
                part = part.strip()
                if not part:
                    continue
                
                instr = self._parse_instruction(part, line_num)
                if instr:
                    instructions.append(instr)
        
        return AST(
            instructions=instructions,
            metadata={'version': '0.1.0', 'lines': len(lines)}
        )
    
    def _parse_instruction(self, text: str, line_num: int) -> Optional[Instruction]:
        """
        Parse single instruction like A(home) or T(flex;column)
        Analyser une instruction comme A(home) ou T(flex;column)
        """
        if not text:
            return None
        
        # Extract primitive letter / Extraire lettre primitive
        primitive_char = text[0].upper()
        
        if primitive_char not in self.PRIMITIVES:
            raise SyntaxError(f"Line {line_num}: Unknown primitive '{primitive_char}'")
        
        primitive = self.PRIMITIVES[primitive_char]
        
        # Extract parameters / Extraire paramètres
        params = {}
        if '(' in text and ')' in text:
            param_str = text[text.index('(')+1:text.rindex(')')]
            params['value'] = param_str
            
            # Parse sub-params (e.g., flex;column)
            # Analyser sous-paramètres (ex: flex;column)
            if ';' in param_str:
                params['values'] = [p.strip() for p in param_str.split(';')]
            else:
                params['values'] = [param_str.strip()]
        
        return Instruction(
            primitive=primitive,
            params=params,
            line=line_num
        )

# ============================================================
# COMPILER / COMPILATEUR
# ============================================================

class CypherCompiler:
    """
    Compile AST to base-4 bytecode
    Compiler AST en bytecode base-4
    """
    
    BASE4_MAPPING = {
        PrimitiveType.CREATE: 0b00,      # 0
        PrimitiveType.CONNECT: 0b01,     # 1
        PrimitiveType.GENERATE: 0b10,    # 2
        PrimitiveType.TRANSFORM: 0b11,   # 3
    }
    
    def __init__(self):
        self.registry = {}  # String -> ID mapping / Correspondance String -> ID
        self.next_id = 0
    
    def compile(self, ast: AST) -> bytes:
        """
        Compile AST to bytecode
        Compiler AST en bytecode
        """
        bytecode = bytearray()
        
        for instr in ast.instructions:
            # Get opcode / Obtenir opcode
            if instr.primitive in self.BASE4_MAPPING:
                opcode = self.BASE4_MAPPING[instr.primitive]
            else:
                # F and L are control flow, not compiled
                # F et L sont contrôle de flux, non compilés
                continue
            
            # Get operand ID / Obtenir ID opérande
            operand = self._register_param(instr.params.get('value', ''))
            
            # Pack as 32-bit instruction / Empaqueter en instruction 32-bit
            instruction = (opcode << 16) | (operand & 0xFFFF)
            bytecode.extend(instruction.to_bytes(4, byteorder='little'))
        
        return bytes(bytecode)
    
    def _register_param(self, param: str) -> int:
        """
        Register parameter and return ID
        Enregistrer paramètre et retourner ID
        """
        if param not in self.registry:
            self.registry[param] = self.next_id
            self.next_id += 1
        return self.registry[param]

# ============================================================
# BACKENDS / MOTEURS
# ============================================================

class WebBackend:
    """
    Generate HTML/CSS/JS from CYPHER
    Générer HTML/CSS/JS depuis CYPHER
    """
    
    def __init__(self):
        self.html_stack = []
        self.css_rules = []
        self.current_element = None
    
    def execute(self, instructions: List[Instruction]) -> Dict[str, str]:
        """
        Generate web output
        Générer sortie web
        """
        for instr in instructions:
            if instr.primitive == PrimitiveType.CREATE:
                self._create_element(instr.params)
            elif instr.primitive == PrimitiveType.GENERATE:
                self._add_content(instr.params)
            elif instr.primitive == PrimitiveType.TRANSFORM:
                self._add_style(instr.params)
        
        html = self._build_html()
        css = self._build_css()
        
        return {
            'html': html,
            'css': css,
            'js': ''  # Future implementation / Implémentation future
        }
    
    def _create_element(self, params: Dict):
        """Create HTML element / Créer élément HTML"""
        element_id = params.get('value', 'div')
        
        # Infer element type / Déduire type élément
        tag = 'div'
        if 'button' in element_id:
            tag = 'button'
        elif 'header' in element_id:
            tag = 'header'
        elif 'input' in element_id:
            tag = 'input'
        
        self.current_element = {
            'tag': tag,
            'id': element_id,
            'classes': [],
            'content': '',
            'children': []
        }
        self.html_stack.append(self.current_element)
    
    def _add_content(self, params: Dict):
        """Add content to current element / Ajouter contenu à élément actuel"""
        if self.current_element:
            self.current_element['content'] = params.get('value', '')
    
    def _add_style(self, params: Dict):
        """Add CSS styles / Ajouter styles CSS"""
        if not self.current_element:
            return
        
        values = params.get('values', [])
        for value in values:
            # Convert to CSS class / Convertir en classe CSS
            class_name = value.replace(':', '-').replace(';', ' ')
            self.current_element['classes'].append(class_name)
            
            # Generate CSS rule / Générer règle CSS
            if ':' in value:
                prop, val = value.split(':', 1)
                rule = f".{class_name} {{ {prop}: {val}; }}"
                self.css_rules.append(rule)
            else:
                # Utility class / Classe utilitaire
                self._add_utility_class(value)
    
    def _add_utility_class(self, class_name: str):
        """Add utility CSS class / Ajouter classe utilitaire CSS"""
        utilities = {
            'flex': 'display: flex;',
            'column': 'flex-direction: column;',
            'grid': 'display: grid;',
            'primary': 'background: #3b82f6; color: white; padding: 0.5rem 1rem; border-radius: 0.25rem;'
        }
        
        if class_name in utilities:
            rule = f".{class_name} {{ {utilities[class_name]} }}"
            if rule not in self.css_rules:
                self.css_rules.append(rule)
    
    def _build_html(self) -> str:
        """Build final HTML / Construire HTML final"""
        if not self.html_stack:
            return '<div></div>'
        
        html_parts = []
        for element in self.html_stack:
            classes = ' '.join(element['classes'])
            tag = element['tag']
            
            if tag == 'input':
                html_parts.append(f'<input id="{element["id"]}" class="{classes}" />')
            else:
                html_parts.append(f'<{tag} id="{element["id"]}" class="{classes}">')
                html_parts.append(element['content'])
                html_parts.append(f'</{tag}>')
        
        return '\n'.join(html_parts)
    
    def _build_css(self) -> str:
        """Build final CSS / Construire CSS final"""
        return '\n'.join(self.css_rules)


class RustBackend:
    """
    Generate and compile Rust code
    Générer et compiler du code Rust
    """
    
    def __init__(self):
        self.cache_dir = Path.home() / ".cypher_cache"
        self.cache_dir.mkdir(exist_ok=True)
    
    def execute(self, instructions: List[Instruction]) -> Dict[str, Any]:
        """
        Generate Rust code from instructions
        Générer code Rust depuis instructions
        """
        rust_code = self._generate_rust(instructions)
        
        # For MVP, return generated code (compilation optional)
        # Pour MVP, retourner code généré (compilation optionnelle)
        return {
            'rust_code': rust_code,
            'compiled': False
        }
    
    def _generate_rust(self, instructions: List[Instruction]) -> str:
        """
        Generate Rust function from CYPHER
        Générer fonction Rust depuis CYPHER
        """
        template = """
// Generated by CYPHER v0.1.0
// Généré par CYPHER v0.1.0

#[no_mangle]
pub extern "C" fn cypher_function() {
    // TODO: Implement logic from instructions
    // TODO: Implémenter logique depuis instructions
    println!("CYPHER Rust backend");
}
"""
        return template

# ============================================================
# ENTITY SYSTEM / SYSTÈME D'ENTITÉS
# ============================================================

class Entity:
    """
    Entity with state and behavior
    Entité avec état et comportement
    """
    _id_counter = 0
    
    def __init__(self, name: str, state: Any = None):
        self.id = Entity._id_counter
        Entity._id_counter += 1
        self.name = name
        self.state = state or {}
        self.is_frozen = False
    
    def freeze(self):
        """Freeze entity state / Geler état entité"""
        self.is_frozen = True
    
    def unfreeze(self):
        """Unfreeze entity state / Dégeler état entité"""
        self.is_frozen = False


class EntitySystem:
    """
    Manage entities and their interactions
    Gérer entités et leurs interactions
    """
    
    def __init__(self):
        self.entities = []
        self.is_fixed = False
    
    def add(self, entity: Entity):
        """Add entity to system / Ajouter entité au système"""
        self.entities.append(entity)
    
    def freeze(self):
        """Freeze entire system / Geler système entier"""
        self.is_fixed = True
        for entity in self.entities:
            entity.freeze()
    
    def run(self):
        """Run system lifecycle / Exécuter cycle de vie système"""
        if not self.is_fixed:
            raise RuntimeError("System must be fixed before running / Système doit être fixé avant exécution")
        
        # Execute system logic / Exécuter logique système
        pass

# ============================================================
# RUNTIME / EXÉCUTION
# ============================================================

class CypherRuntime:
    """
    Main CYPHER runtime
    Runtime principal CYPHER
    """
    
    def __init__(self):
        self.parser = CypherParser()
        self.compiler = CypherCompiler()
        self.web_backend = WebBackend()
        self.rust_backend = RustBackend()
        self.entity_system = EntitySystem()
    
    def execute(self, source: str, target: str = 'web') -> Dict[str, Any]:
        """
        Execute CYPHER code
        Exécuter code CYPHER
        
        Args:
            source: CYPHER source code / Code source CYPHER
            target: 'web' or 'rust' / 'web' ou 'rust'
        
        Returns:
            Execution result / Résultat exécution
        """
        # Parse / Analyser
        ast = self.parser.parse(source)
        
        # Check for F(fixed) and L(life)
        # Vérifier F(fixed) et L(life)
        has_fix = any(i.primitive == PrimitiveType.FIX for i in ast.instructions)
        has_life = any(i.primitive == PrimitiveType.LIFE for i in ast.instructions)
        
        if has_fix:
            self.entity_system.freeze()
        
        # Route to backend / Acheminer vers backend
        if target == 'web':
            result = self.web_backend.execute(ast.instructions)
        elif target == 'rust':
            result = self.rust_backend.execute(ast.instructions)
        else:
            raise ValueError(f"Unknown target: {target}")
        
        if has_life:
            self.entity_system.run()
        
        return result
    
    def compile_to_bytecode(self, source: str) -> bytes:
        """
        Compile to bytecode
        Compiler en bytecode
        """
        ast = self.parser.parse(source)
        return self.compiler.compile(ast)

# ============================================================
# PUBLIC API / API PUBLIQUE
# ============================================================

def execute_cypher(source: str, target: str = 'web') -> Dict[str, Any]:
    """
    Execute CYPHER code (convenience function)
    Exécuter code CYPHER (fonction pratique)
    
    Example / Exemple:
        result = execute_cypher('''
        A(button);G("Click me");T(primary):
        ''')
        print(result['html'])
    """
    runtime = CypherRuntime()
    return runtime.execute(source, target)


def parse_cypher(source: str) -> AST:
    """
    Parse CYPHER to AST
    Analyser CYPHER en AST
    """
    parser = CypherParser()
    return parser.parse(source)


def compile_cypher(source: str) -> bytes:
    """
    Compile CYPHER to bytecode
    Compiler CYPHER en bytecode
    """
    runtime = CypherRuntime()
    return runtime.compile_to_bytecode(source)

# ============================================================
# CLI / INTERFACE LIGNE DE COMMANDE
# ============================================================

def main(args: List[str]):
    """
    CLI entry point
    Point d'entrée CLI
    """
    if len(args) < 2:
        print_help()
        return
    
    command = args[1]
    
    if command == 'run':
        if len(args) < 3:
            print("Error: Missing file path / Erreur: Chemin de fichier manquant")
            return
        
        file_path = args[2]
        target = args[3] if len(args) > 3 else 'web'
        
        with open(file_path, 'r') as f:
            source = f.read()
        
        result = execute_cypher(source, target)
        
        if target == 'web':
            print("=== HTML ===")
            print(result['html'])
            print("\n=== CSS ===")
            print(result['css'])
        elif target == 'rust':
            print("=== Rust Code ===")
            print(result['rust_code'])
    
    elif command == 'build':
        if len(args) < 3:
            print("Error: Missing file path / Erreur: Chemin de fichier manquant")
            return
        
        file_path = args[2]
        
        with open(file_path, 'r') as f:
            source = f.read()
        
        bytecode = compile_cypher(source)
        
        output_path = file_path.replace('.cypher', '.cyb')
        with open(output_path, 'wb') as f:
            f.write(bytecode)
        
        print(f"Compiled to: {output_path}")
        print(f"Compilé vers: {output_path}")
    
    elif command == 'version':
        print("CYPHER v0.1.0")
        print("By Nexus Studio / Par Nexus Studio")
    
    else:
        print_help()


def print_help():
    """Print CLI help / Afficher aide CLI"""
    help_text = """
CYPHER v0.1.0 - Bio-inspired Programming Language
Langage de Programmation Bio-inspiré

Usage / Utilisation:
    cypher run <file.cypher> [target]    Execute CYPHER file / Exécuter fichier CYPHER
    cypher build <file.cypher>           Compile to bytecode / Compiler en bytecode
    cypher version                       Show version / Afficher version
    cypher help                          Show this help / Afficher cette aide

Targets / Cibles:
    web     Generate HTML/CSS/JS (default) / Générer HTML/CSS/JS (défaut)
    rust    Generate Rust code / Générer code Rust

Examples / Exemples:
    cypher run app.cypher
    cypher run api.cypher rust
    cypher build program.cypher

Documentation: https://github.com/tryboy869/cypher
"""
    print(help_text)


if __name__ == "__main__":
    main(sys.argv)