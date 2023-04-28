Here's an exercise that illustrates and teaches Python's new match statement:

## Bite: Match Statements

In this Bite, you will write a function that uses Python's new match statement to parse a string containing a mathematical expression and return the result.

The expression can contain any of the following operators: `+`, `-`, `*`, `/`.

### Signature

```python
def calculate(expression: str) -> float:
    pass
```

### Example

```python
>>> calculate('2+3')
5.0

>>> calculate('4*5-6/2')
18.0
```

### Tips

- The new match statement can be used as a more expressive and concise replacement for complex if/elif chains or nested if/else statements.
- Use the `re.match()` function to extract the operands and operator from the input string.
- Use the `match` statement to match the operator and perform the corresponding calculation. 

Here's a possible implementation:

```python
import re

def calculate(expression: str) -> float:
    match = re.match(r'(\d+)\s*([\+\-\*/])\s*(\d+)', expression)
    if not match:
        raise ValueError('Invalid expression')

    a, op, b = match.groups()

    result = match(op):
        case '+':
            return float(a) + float(b)
        case '-':
            return float(a) - float(b)
        case '*':
            return float(a) * float(b)
        case '/':
            return float(a) / float(b)

    raise ValueError('Invalid operator')
```