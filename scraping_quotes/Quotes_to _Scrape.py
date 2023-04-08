import requests

from bs4 import BeautifulSoup
page = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')

