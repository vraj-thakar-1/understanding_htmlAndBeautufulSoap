
from bs4 import BeautifulSoup
SIMPLE_HTML ='''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>this is a title</h1>
    <p class="subtitle">Lorem ipsum dolor sit amet. Consectrslkfjfj</p>

    <p>Here's another p without a class</p>
    <ul>
      <li>vraj</li>
      <li>trag</li>
      <li>vgfggdraj</li>
      <li>vrdgaj</li>
      <li>vrddj</li>
    </ul>
  </body>
</html>
'''
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all("li")
    list_content = [i.string for i in list_items]
    print(list_content)

def find_subtitle():
    paragraph = simple_soup.find('p', {'class' : 'subtitle'})
    print(paragraph.string)
def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p.string for p in paragraphs if 'subtitle' not in p.attrs.get('class',[]) ]
    print(other_paragraph)
find_title()
find_list_items()
find_subtitle()
find_other_paragraph()