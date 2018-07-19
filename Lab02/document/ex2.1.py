from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel


# Download webpage
url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
html_content = urlopen(url).read().decode("utf-8")

# 2. Extract ROI (region of interest) 
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", id="tableContent")


# 3. Extract information
list_tr = table.find_all("tr")
# print(list_tr)
content_items = [' <Trước   Sau> ', 'Quý 4-2016', 'Quý 1-2017', 'Quý 2-2017', 'Quý 3-2017'] 
posts = []
for tr in list_tr:
    td = tr.find_all("td")
    print(len(td))
    if len(td) == 0:
        continue
    # print(len(td))
    for i in range(len(content_items)):
        post = {}
        post[content_items[i]] = td[i].string
        
    posts.append(post)
pyexcel.save_as(records = posts, dest_file_name = "cafe.xlsx")