from bs4 import BeautifulSoup
markup = "<b><!--This is a comment text in HTML--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print (comment, type(comment))
print(soup.b.prettify())