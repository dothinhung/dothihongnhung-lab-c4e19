from pymongo import MongoClient

uri = "mongodb://admin:admin123@ds137651.mlab.com:37651/c4e19"
# uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# 1. Connect to database
client = MongoClient(uri)

# 2. Get database (lấy database ra)
db = client.get_default_database()

# 3. Create collection (dictionary)
games = db['games']
profies = db['profies']
poems = db['poems']

# # 4. Create document
# new_game = {
#     "name": "Hứng bia",
#     "des": "Best game ever"
# }

# infor = {
#     "name": "Huyen",
#     "age": 21,
#     "address": "Phu Tho"
# }

new_poem = {
    "title": "Tôi yêu em",
    "author": "Mãi yêu em",
    "content": "Tôi buồn thổi khúc tiêu xa. Nhờ cơn gió lạ mang qua bên nàng"
}
# # 5. Insert doc into collection
# games.insert_one(new_game)
# profies.insert_one(infor)
poems.insert_one(new_poem)

# get all documents
all_games = games.find()

print(all_games[0]['name'])

