# Combining Context Managers

Here's an exercise that illustrates and teaches how to use parentheses to invoke more than one context manager at a time in Python:

## Bite: Multi-Context Manager

In this Bite, you will write a context manager that combines two existing context managers using parentheses.

The two context managers are:

1. `tempfile.NamedTemporaryFile`: Creates a temporary file and deletes it when the context manager exits.
2. `gzip.open`: Opens a file for reading or writing using the gzip compression format.

Your task is to create a context manager that combines these two context managers, so that you can use them together in a with statement.

### Signature

```python
@contextmanager
def temp_gzip_file(mode='w', compresslevel=9):
    pass
```

### Example

Here's an example of how you might use the `temp_gzip_file` context manager:

```python
with temp_gzip_file(mode='wb') as f:
    f.write(b'Hello, world!')
```

This code creates a temporary file using `NamedTemporaryFile`, opens it using `gzip.open` in write mode with binary encoding, writes the string `Hello, world!` to the file, and closes the file.

### Tips

- You can use parentheses to invoke more than one context manager at a time. For example, `with context_manager_1() as a, context_manager_2() as b:` creates two context managers `context_manager_1()` and `context_manager_2()` and assigns their context managers to the variables `a` and `b`.
- You can use the `yield` statement to pass control to the body of the with statement, and then use `try` and `finally` blocks to handle the setup and cleanup code for the context managers.