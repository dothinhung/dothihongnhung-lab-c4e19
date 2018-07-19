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

3. Extract information
tr = table.find("tr", id="01")