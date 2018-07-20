from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

# 1. Download webpage
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
html = urlopen(url).read().decode("utf-8")

# 2. Extract ROI 
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", id = "tableContent")

# 3. Extract information
tr_list = table.find_all("tr")

posts = []

for tr in tr_list:
    post = {}
    td = tr.find_all("td")
    for i in range(len(td)):
        post['<Trước  Sau'] = td[0].string
        post['Quý 4-2016'] = td[1].string
        post['Quý 1-2017'] = td[2].string
        post['Quý 2-2017'] = td[3].string
        post['Quý 3-2017'] = td[4].string
    posts.append(post)

pyexcel.save_as(records = posts, dest_file_name = "cafe.xlsx")