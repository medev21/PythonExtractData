from bs4 import BeautifulSoup
import urllib.request
import re

html_page = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals")
# soup = BeautifulSoup(html_page, "html.parser")
# for link in soup.findAll('a'):
#     print(link.get('href'))

soup = BeautifulSoup(html_page, "html.parser")
myyear = []
mylist = []
for rows in soup.findAll('table')[2].findAll('tr'):
    # print(link.get('class'))
    # print(rows)
    mydict = {}

    #for each row in table data country
    for tabledata in rows.findAll('td'):
        # print(row)
        # country = ''.join(tabledata.findAll(text=True))
        # print(mystring)
        name = rows.findAll('td')[0].findAll(text=True)
        mylist.append(name[0])
        # print(name)
        # mydict[name]
        break



    # print(rows.findAll('td')[0].findAll(text=True))


    #for each row in table header - year
    for tableheader in rows.findAll('th'):
        # print(row)
        year = ''.join(tableheader.findAll(text=True))
        myyear.append(year)
    # myyear = myyear[0:]
myyear = myyear[9:]
# print(myyear)
# print(mylist)
mydict = {}
i = 0
for entry in myyear:
    mydict[entry] = mylist[i]
    i += 1

print(mydict["1938"])
# print(soup.table.tbody.findAll("tr")[1].text)
