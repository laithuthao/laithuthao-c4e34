from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = 'https://www.apple.com/itunes/charts/songs/'
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode('utf8')

soup = BeautifulSoup(content,"html.parser")
ul = soup.find("ul","")

li_list = ul.find_all("li")

empty_list = []
# print(li_list)
for li in li_list:
    dic = OrderedDict({"Name":None, "Artist":None})
    a = li.h3.a
    a1= li.h4.a
    name = a.string.strip() 
    print(name)
    # print(a)
    artist = a1.string.strip()
    
    dic["Name"] = name
    dic["Artist"] = artist
    dic = empty_list.append(dic)

    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (video)
    'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download(name)
