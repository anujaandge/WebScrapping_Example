#extracting data using regular expression
import re
import urllib.request
response =urllib.request.urlopen('https://docs.python.org/2/library/cmath.html')
html = response.read()
text = html.decode()
# Search for <td> elements with the class "function"
functions = re.findall(r'<dt id="cmath\.(.*?)">', text)

# Output the matched functions
print(functions)