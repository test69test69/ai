import urllib.request
from bs4 import BeautifulSoup
import sys
imxtToSearch = 'hello world'
query = sys.argv[0].strip("\"").replace(" ","+")
url = "https://www.youtube.com/results?search_query=" + query
response = urllib.request.urlopen(url)
html = response.read()
print(html)
soup = BeautifulSoup(html,"lxml")
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
    	flag = 1
    	print('https://www.youtube.com' + vid['href'])
if flag == 0:
	print("No results found")