import tempfile
import gzip

@contextmanager
def temp_gzip_file(mode='w', compresslevel=9):
  """Creates a temporary file and opens it using the gzip compression format.

  Args:
    mode: The mode to open the file in.
    compresslevel: The compression level to use.

  Yields:
    The gzip-compressed file object.
  """

  # Create a temporary file using `tempfile.NamedTemporaryFile`.
  with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    # Open the file using `gzip.open` in the specified mode and compression level.
    with gzip.open(f, mode=mode, compresslevel=compresslevel) as g:
      # Yield the gzip-compressed file object.
      yield g

  # Delete the temporary file.
  f.close()
