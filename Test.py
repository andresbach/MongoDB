# mydb.get_collection('mytable').find_one({"author": "Duke"})
# mydb.get_collection('mytable').find_one({"author": "blah"})


from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')
mydb = client['pruebaDB']

mydb.posts.drop()

post = {
        "author": "Duke 5",
        "title" : "PyMongo 101 - 5",
        "tags" : ["MongoDB 5", "PyMongo 101 - A5", "Tutorial 5"],
        "date" : datetime.datetime.utcnow()
        }

posts = mydb.posts
post_id = posts.insert_one(post)

print(post_id)
print(mydb.list_collection_names())

new_posts = [{"author": "Duke 6",
              "title" : "PyMongo 101-A6",
              "tags" : ["MongoDB 6", "PyMongo 6", "Tutorial 6"],
              "date" : datetime.datetime(2015, 9, 12, 19, 31, 45, 430540)},
             {"author": "Adja",
              "title": "MongoDB 101-A7",
              "note": "Schema free MongoDB",
              "date": datetime.datetime(2016, 8, 11, 12, 30, 40, 330740)}
            ]
mydb.posts.insert_many(new_posts)
