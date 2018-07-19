from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'
html_content = urlopen(url).read().decode("utf-8")


# 2. Extract ROI (region of interest) 
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
div = soup.find("div", "main")

# 3. Extract information
li_list = div.find_all("li")

titles = []

for li in li_list:

    title = {}

    song = li.h3.a
    song_name = song.string

    artist = li.h4.a
    artist_name= artist.string

    title["Song's name"] = song_name
    title["Artist"] = artist_name

    titles.append(title)

# 4. Save to file excel
pyexcel.save_as(records=titles, dest_file_name="iTunes.xlsx")

# Search and download them 

for name in titles:
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1, 
    }
    dl = YoutubeDL(options)
    dl.download([name["Song's name"]])
