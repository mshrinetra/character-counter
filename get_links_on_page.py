import random
import requests
from bs4 import BeautifulSoup
import re


def get_links_on_page(start_url):
  response = requests.get(start_url)
  soup = BeautifulSoup(response.content, 'html.parser', fromEncoding="utf-8")

  link_set = set()
  indices_of_slash = [i.start() for i in re.finditer('/', start_url)]
  last_index = int(indices_of_slash[2])
  start_url_base = start_url[0:last_index]
  anchors = soup.find_all('a', href=True)
  for anchor in anchors:
    href_link = anchor["href"]
    indices_of_slash = [i.start() for i in re.finditer('/', href_link)]
    
    if len(indices_of_slash) > 2:
      last_index = int(indices_of_slash[2])
      href_link = href_link[0:last_index]

    if href_link[0] == '/' and href_link[1] != '/':
      link_set.add(start_url_base + href_link)

  return link_set

  # new_link_set = set()
  # for k in random.sample(link_set, 2):
  #   new_link_set.add(k)
  # return new_link_set


