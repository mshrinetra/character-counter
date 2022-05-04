import requests
from bs4 import BeautifulSoup


def get_text_from_page(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser', fromEncoding="utf-8")

  paras = soup.find_all('p')

  text = " "
  for para in paras:
    text = text + para.text

  return text