import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.pyclass.com/example.html",headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c =req.content

# print(c)

soup = BeautifulSoup(c,"html.parser")
# print(soup.prettify())
all = soup.find_all("div",{"class":"cities"})
# print(all)
for i in (all):
	header = i.find_all("h2")[0]
	print(header.text)