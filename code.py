import pymongo

client=pymongo.MongoClient("mongodb+srv://adhiraj135:mongodb123@cluster0.3rcw4.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)


d={
    "name":"adhiraj",
    "email":"adhiraj.singh483@gmail.com"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)