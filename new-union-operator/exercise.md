Sure! Here's an exercise that illustrates and teaches the use of Python's new union operator `|`, which can be used to combine dictionaries and sets:

## Bite: Combine and Count

In this Bite, you will write a function that takes two dictionaries, `dict1` and `dict2`, and returns a dictionary that combines the keys and values of both dictionaries. If a key appears in both dictionaries, the values will be added together. You will also use the new union operator `|` to combine two sets of unique items.

The function should work as follows:

```python
>>> dict1 = {'apple': 3, 'banana': 2, 'orange': 1}
>>> dict2 = {'pear': 5, 'orange': 2, 'kiwi': 1}
>>> combine_and_count(dict1, dict2)
{'apple': 3, 'banana': 2, 'orange': 3, 'pear': 5, 'kiwi': 1}

>>> dict3 = {'apple': 3, 'banana': 2, 'orange': 1}
>>> dict4 = {'pear': 5, 'mango': 2, 'kiwi': 1}
>>> combine_and_count(dict3, dict4)
{'apple': 3, 'banana': 2, 'orange': 1, 'pear': 5, 'mango': 2, 'kiwi': 1}
```

If either dictionary is empty, the function should return the other dictionary:

```python
>>> dict5 = {'apple': 3, 'banana': 2, 'orange': 1}
>>> dict6 = {}
>>> combine_and_count(dict5, dict6)
{'apple': 3, 'banana': 2, 'orange': 1}

>>> dict7 = {}
>>> dict8 = {'pear': 5, 'mango': 2, 'kiwi': 1}
>>> combine_and_count(dict7, dict8)
{'pear': 5, 'mango': 2, 'kiwi': 1}
```

### Signature

```python
def combine_and_count(dict1: dict, dict2: dict) -> dict:
    pass
```
