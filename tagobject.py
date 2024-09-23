from bs4 import BeautifulSoup

url="https://www.w3schools.com/python/python_strings.asp"
soup=BeautifulSoup('<h1>Python <span class="color_h1">Strings</span></h1>','lxml')

tag=soup.html
print(type(tag))
print(tag.name) # name of tag
tag.name="strong"
print(tag)
print(tag.name)

soup1 = BeautifulSoup('<input type="text" name="name" value="Raju">', 'lxml')
tag1 = soup1.input

print (tag1.attrs) #getting tag attributes
#we can do modifiction to attributes

tag1['value']="Ravi"
print(soup1)

tag1['id']='nm'
del tag1['value']
print(soup1)