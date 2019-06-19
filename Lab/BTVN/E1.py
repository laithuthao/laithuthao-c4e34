from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url) # Tao duong ong dan du lieu
raw_data = conn.read() #Keo du lieu ve phia minh
content = raw_data.decode('utf8') #decode data, utf8 la ngon ngu chuan de may tinh hieu dc

soup = BeautifulSoup(content, "html.parser")
ul = soup.find("ul", "") 

li_list = ul.find_all("li")
new_list=[]

for li in li_list:

    a = li.h3.a
    name = a.string.strip()

    b=li.h4.a
    artist = b.string.strip()
    print(name)
    print(artist)

    chart= OrderedDict({
        "Name": name,
        "Artist": artist,
    })

    chart["Name"] = name
    chart["Artist"] = artist
    chart = new_list.append(chart)

pyexcel.save_as(records=new_list,dest_file_name="itune.xlsx")

for name in new_list:
    options = {
        'default_search': 'ytsearch', 
        'max_downloads': 1, 
        'format': 'bestaudio/audio'
    }
    

    dl = YoutubeDL(options)
    dl.download([name])
    
