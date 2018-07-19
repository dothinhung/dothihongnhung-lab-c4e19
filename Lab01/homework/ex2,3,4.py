from pymongo import MongoClient

import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# uri = "mongodb://admin:admin123@ds137651.mlab.com:37651/c4e19"

# 1. Connect database
client = MongoClient(uri)

# 2. Get database
db = client.get_default_database()

# 3. Create database
posts = db['posts']
customers = db['customers']

# 4. Create document
# quote = {
#     "title": "Quote",
#     "author": "Đ.T.H.Nhung",
#     "content": """Only I can change my life.
#                   No one can do it for me 
#                        -Carol Burnett-"""
# }


# 5. Insert document into collection
# posts.insert_one(quote)
count_ads = customers.count({"ref": "ads"})
count_wom = customers.count({"ref": "wom"})
count_events = customers.count({"ref": "events"})
print(count_ads, count_wom, count_events)



#  use matplotlib to draw a pie chart
# 1. Prepare data
labels = ["Advertisements", "Events", "World of mouth"]
values = [count_ads, count_events, count_wom]
colors = ["green", "red", "yellow"]

# 2. plot
pyplot.pie(values, 
        labels=labels,
        colors=colors)
pyplot.axis("equal")

# 3. Show
pyplot.show()
