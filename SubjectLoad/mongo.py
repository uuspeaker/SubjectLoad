import pymongo

myclient = pymongo.MongoClient('mongodb://129.211.21.250:27017/')

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")