def count_sequence_in_text(text):
  sequenc_dict = {}

  text_length = len(text)
  i = 0
  j = 1
  while (i < (text_length - 2)) and (j < (text_length - 1)):
    key = text[i] + text[j]
    if key in sequenc_dict:
      sequenc_dict[key] += 1
    else:
      sequenc_dict[key] = 1

  return sequenc_dict