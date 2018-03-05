import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter-")
html = urllib.request.urlopen(url,context=ctx).read()

soap = BeautifulSoup(html,"html.parser")
tags = soap("span")

lst = list()

for tag in tags:
    lst.append(float(tag.contents[0]))

print("Count:", len(lst))
print("Sum:", sum(lst))
