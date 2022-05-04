from encodings import utf_8
import io
from msilib import sequence

from get_text_from_page import *
from get_links_on_page import *
from count_chars_in_text import *
from clear_path import *
from merge_counts import *
from count_sequence_in_text import *


start_url = "https://hi.wikipedia.org/wiki/%E0%A4%AD%E0%A4%BE%E0%A4%B0%E0%A4%A4"
full_text_file = "output/full_text.txt"
count_summary = "output/count_summary.csv"
sequence_summary = "output/sequence_summary.csv"
links_visited = "output/links_visited.txt"

def main():
  link_set = set()
  link_set = get_links_on_page(start_url)
  link_set.add(start_url)

  char_count = {}
  sequence_count = {}

  clear_path(links_visited);

  try:
    with io.open(links_visited, 'w', encoding='utf-8') as f:
      for link in link_set:
        print("working: " + link)
        full_text = get_text_from_page(link)
        if(len(full_text) > 1):
          char_count = merge_counts(char_count, count_chars_in_text(full_text))
          # sequence_count = merge_counts(sequence_count, count_sequence_in_text(full_text))
        f.write(link + "\n")
  
  except:
    print("ERROR! Could Not Complete")


  clear_path(count_summary)
  with io.open(count_summary, 'w', encoding='utf-8') as f:
    f.write("Character,Frequency\n")
    for character in char_count:
      f.write(character + "," + str(char_count[character]) + "\n")

  # clear_path(sequence_summary)
  # with io.open(sequence_summary, 'w', encoding='utf-8') as f:
  #   f.write("Sequence,Frequency\n")
  #   for sequence in sequence_count:
  #     f.write(sequence + "," + sequence_count[sequence] + "\n")


if __name__=="__main__":
  main()