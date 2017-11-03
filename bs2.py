from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

#print(soup.title) #returns title of file with tags
#print(soup.title.name) #returns title
#print(soup.title.string) #returns title of file as a string
#print(soup.a) #returns first link with tag a found
#print(soup.find_all('a')) #returns list of all links with tag a
tag = soup.a
#print(tag.name) #returns a
#print(tag) #returns the whole tag
#print(tag['href']) #return the 'value' of the key (attribute of the tag) that was accessed
#print (tag.attrs)

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
#print(css_soup.p['class'])
#print(tag.string)
print(css_soup.p.attrs)
print(soup.head.title)