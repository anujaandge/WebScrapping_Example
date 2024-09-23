#NavigableString object represents the contents of a tag

from bs4 import BeautifulSoup
soup=BeautifulSoup("<h2 id='message'>Hello, World!</h2>",'html.parser')
print(soup.string)
print(type(soup.string))

#NavigableString can be converted to a Unicode string with str() function.
tag=soup.h2
string=str(tag.string)
print(string)

#modify NavigableString with the help of replace_with()
tag1=soup.h2
tag1.string.replace_with("Hello India")
print(tag1.string) 