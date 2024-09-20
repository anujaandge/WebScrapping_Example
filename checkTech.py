#biltwith module helps to find out from which technology website id build
import builtwith
print(builtwith.parse('https://www.tutorialspoint.com/python_web_scraping/legality_of_python_web_scraping.htm'))

#whois tells obout the owner of the website
import whois
print(whois.whois('https://www.tutorialspoint.com/'))