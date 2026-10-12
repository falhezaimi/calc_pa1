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

## Saved version

The three assignment files are the unchanged initial Gemini calculator response saved on October 6, 2026. The original evaluation identifies this as a provisional first attempt; its exact model version and original prompt were not recorded.

The saved evaluation passed all 10 instructor examples and 26 additional development cases (36/36). Held-out evaluation was deferred.

The review also identified two language-preservation failures: the grammar rejects `2^-3` and `log 2+6 base 2`, although the assignment's original grammar accepts them. These additional diagnostics were separate from the fixed development score. The saved code is therefore an initial version with documented limitations, rather than a claim of full assignment compliance.
