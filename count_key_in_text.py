def count_key_in_text(key_dict, text):


  new_key_dict = {}
  for key in key_dict:
    new_key_dict[key] = int(key_dict[key]) + text.count(key)

  return new_key_dict