from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

html_content = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")

sec = soup.find("section", "section chart-grid")

li_list = sec.find_all("li")

posts = []

for li in li_list:
    post = {}
    a = li.h3.a
    song_name = a.string
    b = li.h4.a
    artist = b.string
    post['Song name'] = song_name
    post['Artist'] = artist
    posts.append(post)

# pyexcel.save_as (records = posts, dest_file_name = "iTunes_top_songs.xlsx")

for name in posts:
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1
    }
    dl = YoutubeDL(options)
    dl.download([name['Song name']])