import io


def get_char_dict(input_file):
  char_dict = {}
  try:
    with io.open(input_file, 'r', encoding="utf-8") as f:
      for line in f.readlines():
        key_char = line.replace('\n', '')
        char_dict[key_char] = 0

    return char_dict
  except:
    print("ERROR! Could not read key char list")



def get_sequence_dict(input_file):
  char_list = []
  sequence_dict = {}
  try:
    with io.open(input_file, 'r', encoding="utf-8") as f:
      for line in f.readlines():
        key_char = line.replace('\n', '')
        char_list.append(key_char)

    for x in char_list:
      for y in char_list:
        sequence_dict[str(x) + str(y)] = 0

    return sequence_dict

  except:
    print("ERROR! Could not read key char list")


# print(get_char_dict("input/key_char_list.txt"))
# print("-------------")
# print(get_sequence_dict("input/key_char_list.txt"))