def get_file_type(file_name: str) -> str:
  """Returns the type of file based on its extension.

  Args:
    file_name: The name of the file.

  Returns:
    The type of file.
  """

  # Split the file name into its base name and extension.
  base_name, extension = os.path.splitext(file_name)

  # Convert the extension to lower case for matching.
  extension = extension.lower()

  # Match the extension against a set of patterns.
  match = {
    '.txt': 'Text File',
    '.jpg': 'Image File',
    '.exe': 'Executable File',
    '.zip': 'Archive File',
  }

  # Return the matching type.
  return match.get(extension, 'Unknown File')
