from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
data = conn.read()
html = data.decode("utf-8")

# save to file
# html_file = open("cafef.html", "wb")
# html_file.write(data)
# html_file.close

# Extract ROI 
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", id = "tableContent")
# print(table.prettify())
tr_list = table.find_all("tr")

posts = []
content_items = [' <| Trước     Sau |> ', 'Quy 4-2016', 'Quý 1-2017', 'Quý 2-2017', 'Quý 3-2017', 'Tăng trưởng'] 
for tr in tr_list:
    post = {}
    td = tr.find_all("td")
    # print(len(td))
    if len(td) == 0:
        continue
    print(len(td))
    for i in range(len(content_items)):
        post[content_items[i]] = td[i].string
        
    posts.append(post)

pyexcel.save_as(records = posts, dest_file_name = "cafe.xlsx")