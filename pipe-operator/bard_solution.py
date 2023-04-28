def recommended_books(books: list) -> list:
  """Returns a list of recommended books based on the given list of books.

  Args:
    books: A list of books.

  Returns:
    A list of recommended books.
  """

  # Filter out any books with less than 200 pages.
  filtered_books = books | filter(lambda book: book['pages'] >= 200)

  # Sort the remaining books by author.
  sorted_books = filtered_books | sorted(key=lambda book: book['author'])

  # Return the top 3 books by author.
  return sorted_books[:3]
