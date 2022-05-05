import io

from clear_path import *
from get_links_on_page import *
from get_text_from_page import *
from get_char_and_sequence_dict import *
from count_key_in_text import *


start_url = "https://hi.wikipedia.org/wiki/%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4"


key_char_list_file = "input/key_char_list.txt"

count_summary = "output/count_summary.csv"
sequence_summary = "output/sequence_summary.csv"
links_visited = "output/links_visited.txt"


def main():
  link_set = set()
  link_set = get_links_on_page(start_url)
  link_set.add(start_url)

  char_dict = get_char_dict(key_char_list_file)
  sequence_dict = get_sequence_dict(key_char_list_file)

  clear_path(links_visited);

  try:
    with io.open(links_visited, 'w', encoding='utf-8') as f:
      for link in link_set:
        print("working: " + link)
        full_text = get_text_from_page(link)
        if(len(full_text) > 1):
          char_dict = count_key_in_text(char_dict, full_text)
          sequence_dict = count_key_in_text(sequence_dict, full_text)
        f.write(link + "\n")
  
  except:
    print("ERROR! Could Not Complete")


  clear_path(count_summary)
  with io.open(count_summary, 'w', encoding='utf-8') as f:
    f.write("Character,Frequency\n")
    for key_char in char_dict:
      f.write(key_char + "," + str(char_dict[key_char]) + "\n")

  clear_path(sequence_summary)
  with io.open(sequence_summary, 'w', encoding='utf-8') as f:
    f.write("Sequence,Frequency\n")
    for sequence in sequence_dict:
      f.write(sequence + "," + str(sequence_dict[sequence]) + "\n")


if __name__=="__main__":
  main()