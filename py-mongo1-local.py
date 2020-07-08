import pymongo

# local connection to local mongo server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Using this database
database = client['PyDB_local']
print(database)

# calling this collection "employees"
collection = database['employees']
print(collection)

#  call our variable collection
employees = collection.find({})
print(employees)

for employee in employees:
    print(employee)
