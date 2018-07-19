# 1. Dowload webpage
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
html_content = urlopen(url).read().decode("utf-8")
# print(url)

# 1.1. Open connection
conn = urlopen(url)

# 1.2 read data
data = conn.read()
# print(data)

# 1.3 Decode
html = data.decode("utf-8")
# print(html)

# save to file html
# cách 1, cách này ở bài tập về nhà k dùng được
# html_file = open("dantri.html","wb")
# html_file.write(data)
# html_file.close()

# cách 2
f = open("dantri.html", "wb")
f.write(data)


# 2. Extract ROI (region of interest) tách vùng mình cần quan tâm
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")

ul = soup.find("ul", "ul1 ulnew")


# 3. Extract information
li_list = ul.find_all("li")
# li = li_list[0] 

posts = []

for li in li_list:
    post = {}
    # cách viết gọn của hàm find() vì bên trong li chỉ có 1 h4, và bên trong h4 chỉ có 1 a
    h4 = li.h4
    a = h4.a
    # cách viết đầy đủ 
    # h4 = li.find("h4")
    # a = h4.find("a")


    title = a.string
    href = url + a['href']
    

    post['title'] = title
    post['href'] = href
    posts.append(post)
   


# 4. Save data to excel 
# a_list_of_dictionaries = [
#     {
#        "Name": 'Adam',
#         "Age": 28
#     },
#     {
#         "Name": 'Beatrice',
#         "Age": 29
#     },
# ]


pyexcel.save_as(records=posts, dest_file_name="c4e.xlsx")
