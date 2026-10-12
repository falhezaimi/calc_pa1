# calc_pa1

CPSC 354 Programming Languages — Calculator PA1, Fares Alhezaimi.

## Files

- `Assignment1/calculator_cfg.py`: command-line calculator that builds and recursively evaluates an abstract syntax tree.
- `Assignment1/grammar.lark`: Lark grammar for addition, subtraction, multiplication, unary minus, exponentiation, logarithms, and parentheses.
- `Assignment1/specs.md`: program flow, AST classes, grammar, precedence, and associativity.
- `requirements.txt`: the dependency version used for the saved evaluation.

## Run

Use Python 3.12. From the repository root:

```bash
python -m pip install -r requirements.txt
cd Assignment1
python calculator_cfg.py "2^3^2"
```

The example prints `512`. Run the calculator from `Assignment1`, because it loads `grammar.lark` from the current working directory.

Other examples:

```bash
python calculator_cfg.py "2-(4+2)"
python calculator_cfg.py "log 8 base 2 + 1"
python calculator_cfg.py "-3^2"
```

These print `-4`, `4`, and `-9`, respectively.


