import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html5lib')

links = soup.find_all('a')
for link in links:
    print(link)
