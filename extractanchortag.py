from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print(link.get('href'))
