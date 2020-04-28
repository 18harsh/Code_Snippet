import requests
res = requests.get("http://automatetheboringstuff.com/files/rj.txt")
print(res.status_code)
print(res.text[:500])
print(res.raise_for_status())

# badreq = requests.get("qwertyuio")
# print(badres.raise_for_status())

playfile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
	playfile.write(chunk)