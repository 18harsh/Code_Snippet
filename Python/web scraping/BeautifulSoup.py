import bs4
import requests
import re
res= requests.get("https://nostarch.com/NLPPython")
print(res.raise_for_status())
soup = bs4.BeautifulSoup(res.text,'html.parser')
print(type(soup))
elems = (soup.select('#edit-attributes-1 > div:nth-child(1) > label'))
content = (elems[0].text.strip())
print(content)
price = re.compile(r'\$\d+\.\d+')
print(price.search(content).group())

