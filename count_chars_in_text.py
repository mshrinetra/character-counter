def count_chars_in_text(text):
  char_dict = {}

  for i in text:
    if i in char_dict:
      char_dict[i] += 1
    else:
      char_dict[i] = 1

  return char_dict