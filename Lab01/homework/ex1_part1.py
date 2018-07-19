# 1. Download Webpage
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL


url = "https://www.apple.com/itunes/charts/songs"
html_content = urlopen(url).read().decode("utf-8")


# 2. Extract ROI (Region of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
div = soup.find("div", "section-content")


# 3. Extract information
titles = []

li_list = div.find_all("li")
for li in li_list:
    title = {} 

    name = li.h3.a
    song_name = name.string
    print(song_name)

    artist = li.h4.a
    artist_name = artist.string

    title["Song"] = song_name
    title["Artist"] = artist_name

    titles.append(title)


# 4. Save to file excel
pyexcel.save_as(records= titles, dest_file_name="iTunes.xlsx")


# Search and download them
for song in titles:
    options = {
        'default_search': 'ytsearch',
        'max_download': 1
    }
dl = YoutubeDL(options)
dl.download("Song")
