def combine_and_count(dict1: dict, dict2: dict) -> dict:
  """Combines two dictionaries and returns a new dictionary with the combined keys and values.

  Args:
    dict1: The first dictionary.
    dict2: The second dictionary.

  Returns:
    The combined dictionary.
  """

  # Combine the sets of unique keys from both dictionaries.
  combined_keys = set(dict1) | set(dict2)

  # Create a new dictionary with the combined keys and values.
  combined_dict = {}
  for key in combined_keys:
    combined_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

  return combined_dict
