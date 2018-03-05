import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL:")
count = input("Enter count:")
position = input("Enter postion:")
count = int(count)
position = int(position)

i = count+1
while i>0:
    print("Retrieving:", url)
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    url = tags[position-1].get('href', None)
    i=i-1
