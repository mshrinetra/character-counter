def merge_counts(old_dict, new_dict):
  combined_dict = {}

  if not old_dict is None:
    for key in old_dict:
      combined_dict[key] = old_dict[key]

  if not new_dict is None:
    for key in new_dict:
      if key in combined_dict:
        combined_dict[key] = int(combined_dict[key]) + new_dict[key]
      else:
        combined_dict[key] = new_dict[key]

  return combined_dict