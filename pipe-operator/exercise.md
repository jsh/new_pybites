# Pipe Operator

Here's an exercise that illustrates and teaches the use of Python's new pipe operator `|>`, which can be used to chain function calls:

## Bite: Book Recommendations

In this Bite, you will write a function that takes a list of books and applies a series of filters and sorts to produce a list of recommended books. You will use the new pipe operator `|>` to chain the function calls.

The function should work as follows:

```python
>>> books = [
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'pages': 224},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'pages': 336},
    {'title': '1984', 'author': 'George Orwell', 'pages': 328},
    {'title': 'One Hundred Years of Solitude', 'author': 'Gabriel Garcia Marquez', 'pages': 417},
    {'title': 'Brave New World', 'author': 'Aldous Huxley', 'pages': 288},
    {'title': 'Animal Farm', 'author': 'George Orwell', 'pages': 112},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'pages': 180},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'pages': 226},
    {'title': 'Wuthering Heights', 'author': 'Emily Bronte', 'pages': 288},
    {'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde', 'pages': 176}
]

>>> recommended_books(books)
[
    {'title': 'One Hundred Years of Solitude', 'author': 'Gabriel Garcia Marquez', 'pages': 417},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'pages': 180},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'pages': 336}
]
```

The function should first filter out any books with less than 200 pages, then sort the remaining books by author, and finally return the top 3 books by author.

### Signature

```python
def recommended_books(books: list) -> list:
    pass
```

