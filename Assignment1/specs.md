# Calculator Specifications

## Overall Program Flow
1. **CLI Input**: The calculator reads a mathematical expression string from `sys.argv[1]`.
2. **Parsing**: It uses `Lark` with the LALR parsing algorithm to parse the string against the rules defined in `grammar.lark`. 
3. **AST Construction**: The parse result (a Lark `Tree`) is passed through `ASTBuilder`, a `lark.Transformer` subclass. `ASTBuilder` converts the Lark tree nodes directly into instances of our custom AST classes.
4. **Evaluation**: The evaluator calls the `evaluate()` method on the root AST node, recursively traversing the structure and computing the final mathematical value using Python's standard `math` module.
5. **Output**: The result is printed to `stdout` (formatted as an integer if it represents a whole number, otherwise a float).

## Methods and Functions
### AST Nodes
The AST is heavily object-oriented, mapping expressions to distinct nodes inheriting from `ExprNode`. 
- `NumNode(value)`: Represents a terminal numeric value. `evaluate()` returns its `float` value.
- `AddNode(left, right)`, `SubNode(left, right)`, `MulNode(left, right)`: Represent standard binary operations. They evaluate their left and right children and return the sum, difference, or product.
- `PowNode(left, right)`: Represents exponentiation, evaluated via `math.pow()`.
- `LogNode(val, base)`: Represents the custom log operator, evaluated via `math.log(val, base)`.
- `NegNode(operand)`: Represents the unary minus, flipping the sign of its child's evaluated result.

### ASTBuilder (Lark Transformer)
- Maps named Lark rules (`add`, `sub`, `mul`, `pow`, `log_op`, `neg`, `num`) to the instantiation of their corresponding AST nodes. 
- Anonymous terminals (like `+`, `-`, `"log"`, `"base"`, `(`, `)`) are inherently dropped by Lark, leaving the `args` array containing exactly the nested nodes.

## Context-Free Grammar (CFG) Design
The original ambiguous grammar was refactored into a layered, unambiguous structure by enforcing strict precedence levels:
1. `exp`: Handles Addition and Subtraction (`+`, `-`).
2. `term`: Handles Multiplication (`*`).
3. `factor`: Handles Unary Minus (`-`).
4. `power`: Handles Exponentiation (`^`).
5. `atom`: Handles Logarithms (`log ... base ...`), Numbers, and Parentheses.

Parentheses correctly control grouping using `"(" exp ")"`. The `?` modifier is placed on each rule in the `.lark` file to inline rules with only one child, ensuring parentheses control parse hierarchy but do not artificially generate "parenthesis" nodes in the AST.

## Precedence and Order of Operations (Lowest to Highest)
1. **Addition (`+`) / Subtraction (`-`)**
2. **Multiplication (`*`)**
3. **Unary Minus (`-`)**: Parsed at the `factor` level. This effectively binds tighter than multiplication but looser than exponentiation, so `-3^2` correctly parses as `-(3^2)` returning `-9`. Note that stacked minus signs (e.g. `--1`) parse as sequentially nested `neg` nodes.
4. **Exponentiation (`^`)**: Binds tighter than unary operators and basic arithmetic.
5. **Logarithms (`log a base b`) / Parentheses / Numbers**: Bind tightest.

## Associativity Specifications
- **Left-Associative Operations (`+`, `-`, `*`)**: Evaluated from left to right. Enforced by left-recursive rules (e.g., `?exp: exp "+" term`).
- **Right-Associative Operations (`^`)**: Exponentiation groups right-to-left. `2^3^2` is parsed as `2^(3^2)`. This is strictly enforced in the CFG using a right-recursive rule (`?power: atom "^" power`).
- **Logarithm Operands**: The `log` operator is defined at the `atom` level (`"log" atom "base" atom`). This was chosen over lower tiers to strictly avoid precedence leaks (like `log 8 base 2 + 1` parsing incorrectly). As a result, the operands to `log` and `base` tightly bind primary constructs only. For composite operands in logarithms (e.g., $log(2^3)$), parentheses are naturally enforced (e.g., `log 8 base (2^3)`), which ensures uniquely predictable AST geometry.

