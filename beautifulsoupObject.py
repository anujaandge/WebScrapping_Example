from bs4 import BeautifulSoup
fp=open("index.html")
soup=BeautifulSoup(fp,'html.parser')

print(soup)
print(soup.name)
print('type:',type(soup))

#beautifulsoup object can be combined
obj1 = BeautifulSoup("<book><title>Python</title></book>", features="xml")
obj2 = BeautifulSoup("<b>Beautiful Soup parser</b>", "lxml")

obj2.find('b').replace_with(obj1)
print (obj2)