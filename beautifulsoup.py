from bs4 import BeautifulSoup
import requests

r=requests.get('https://docs.python.org/2/library/cmath.html')

soup=BeautifulSoup(r.text,'lxml')
print(soup.title)
print(soup.title.text)


print("second website")
url="https://www.tutorialspoint.com/index.htm"
req=requests.get(url)
soup1=BeautifulSoup(req.content,"html.parser")
print(soup1.title)

#for extracting all the urls within webpage
print("\n printing all the urls from website\n")
for link in soup1.find_all('a'):
    print(link.get('href'))
    
    
#accessing web page stored locally in the current working directory
print("\naccessing web page stored locally in the current working directory\n")
with open("index.html") as fp:
    soup3=BeautifulSoup(fp,'html.parser')
    
print(soup3)    