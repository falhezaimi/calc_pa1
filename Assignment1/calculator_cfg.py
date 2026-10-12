import sys
import math
from lark import Lark, Transformer

# --- AST Node Definitions ---
class ExprNode:
    """Base class for all AST nodes."""
    def evaluate(self) -> float:
        raise NotImplementedError()

class NumNode(ExprNode):
    def __init__(self, value: float):
        self.value = value
        
    def evaluate(self) -> float:
        return self.value

class AddNode(ExprNode):
    def __init__(self, left: ExprNode, right: ExprNode):
        self.left = left
        self.right = right
        
    def evaluate(self) -> float:
        return self.left.evaluate() + self.right.evaluate()

class SubNode(ExprNode):
    def __init__(self, left: ExprNode, right: ExprNode):
        self.left = left
        self.right = right
        
    def evaluate(self) -> float:
        return self.left.evaluate() - self.right.evaluate()

class MulNode(ExprNode):
    def __init__(self, left: ExprNode, right: ExprNode):
        self.left = left
        self.right = right
        
    def evaluate(self) -> float:
        return self.left.evaluate() * self.right.evaluate()

class PowNode(ExprNode):
    def __init__(self, left: ExprNode, right: ExprNode):
        self.left = left
        self.right = right
        
    def evaluate(self) -> float:
        return math.pow(self.left.evaluate(), self.right.evaluate())

class LogNode(ExprNode):
    def __init__(self, val: ExprNode, base: ExprNode):
        self.val = val
        self.base = base
        
    def evaluate(self) -> float:
        return math.log(self.val.evaluate(), self.base.evaluate())

class NegNode(ExprNode):
    def __init__(self, operand: ExprNode):
        self.operand = operand
        
    def evaluate(self) -> float:
        return -self.operand.evaluate()

# --- Lark Transformer ---
class ASTBuilder(Transformer):
    """Transforms the Lark parse tree into our custom AST."""
    
    def num(self, args):
        return NumNode(float(args[0]))
        
    def add(self, args):
        return AddNode(args[0], args[1])
        
    def sub(self, args):
        return SubNode(args[0], args[1])
        
    def mul(self, args):
        return MulNode(args[0], args[1])
        
    def pow(self, args):
        return PowNode(args[0], args[1])
        
    def log_op(self, args):
        return LogNode(args[0], args[1])
        
    def neg(self, args):
        return NegNode(args[0])

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
        
    expression = sys.argv[1]

    # Load grammar
    with open("grammar.lark", "r") as f:
        grammar = f.read()

    # Generate parser
    parser = Lark(grammar, start='start', parser='lalr')
    
    # 1. Parse into Lark Tree
    tree = parser.parse(expression)
    
    # 2. Build custom AST
    ast_builder = ASTBuilder()
    ast_root = ast_builder.transform(tree)
    
    # 3. Evaluate AST
    result = ast_root.evaluate()
    
    # Print result formatting as integer if round, else float
    if result.is_integer():
        print(int(result))
    else:
        print(result)

if __name__ == "__main__":
    main()

