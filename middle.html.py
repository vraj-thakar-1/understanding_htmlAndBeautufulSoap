# web scraping by code with harry
# 2 approach to scrape the website
# 1. use the api
# 2. html web scraping using some tool like bs4

''' 
step0:
Install all the requirements
1. pip install requests
2. pip install bs4
3. pip install htm5lib
'''
import requests
from bs4 import BeautifulSoup
import html5lib

url = 'https://www.codewithharry.com'

# step1:
# get the html
r  = requests.get(url)
html_content = r.content
# print(html_content)


# step2: 
# parse the html
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify)
# step 3:
# Html Tree traversal
# commonly used types of objects
# title = soup.title
# 1. Tag print(title)
# 2. NavigableString print(title.string)
# 3. BeautifulSoup  print(type(soup))
# 4. Comment
     

# title = soup.title
# print(title) # <title>Learn to code online - CodeWithHarry</title>
# print(type(title)) # <class 'bs4.element.Tag'>
# print(title.string) #Learn to code online - CodeWithHarry
# print(type(title.string)) # <class 'bs4.element.NavigableString'>
# print(type(soup)) # <class 'bs4.BeautifulSoup'>

# Get the title of HTML  page

title = soup.title

# Get all the paragraphs from the page
paras =soup.find_all('p')
# print(paras)
# Get all anchor tags from the page
# anchors =soup.find_all('a')
# print(anchors)

# get first element in html page.
# print(soup.find('p'))
# # get classes of any element in the html page
# print(soup.find('p')['class']) 
# # get id of any element in the html page
# print(soup.find('p')['id']) 
# find all the elements with class lead
# print(soup.find_all('p',class_='text-sm'))

# get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# get all the links on the page 
# anchors =soup.find_all('a')
# all_links= set()
# for link in anchors:
#     if (link['href'] != "#"):
#         link ="https://codewithharry.com"+link['href']
#         all_links.add(link)
#         print(link)
    
     
# # comment object

# markup = '<p><!--this is a comment --></p>'
# soup2= BeautifulSoup(markup)
# print((soup2.p.string))
# print(type(soup2.p.string))

# get contents by id
search_togl =soup.find(id="search-toggle")

# print(search_togl)
# print(search_togl.children)
#  .contents = a Tag's children are available as a list.
#  .children = a Tag's children are available as a generator.

# for ele in search_togl.contents:
#     print(ele.string)
  
# .parent
# print(search_togl.parent)
# print(search_togl.parents) return generator object
# for item in search_togl.parents:
#     print(item.name)

print(soup.select('#search-toggle'))
# print(soup.select('.search-toggle'))