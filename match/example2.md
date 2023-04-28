Here's an exercise that illustrates and teaches Python's new match statement:

## Bite: File Type Checker

In this Bite, you will write a function that takes a file name and returns the type of file based on its extension using Python's new match statement.

The function should work as follows:

```python
>>> get_file_type('example.txt')
'Text File'

>>> get_file_type('example.jpg')
'Image File'

>>> get_file_type('example.exe')
'Executable File'

>>> get_file_type('example.zip')
'Archive File'
```

### Signature

```python
def get_file_type(file_name: str) -> str:
    pass
```

### Example

The function should work with any file name with a valid extension:

```python
>>> get_file_type('example.txt')
'Text File'

>>> get_file_type('example.jpg')
'Image File'

>>> get_file_type('example.exe')
'Executable File'

>>> get_file_type('example.zip')
'Archive File'

>>> get_file_type('example')
'Unknown File'
```

### Tips

- Use the `os.path.splitext()` function to split a file name into its base name and extension.
- Use the match statement to match the extension against a set of patterns.
- Use the `str.lower()` method to convert the extension to lower case for matching.
- Use `case` blocks in the match statement to handle each pattern.