import pymongo


#db_url = 'mongodb://localhost:27017'
client = pymongo.MongoClient('mongodb://localhost:27017/')


# this line for creating a new db or using an existing one
database = client["PyDB_local"]
# Important: In MongoDB, a database is not created until it gets content (at least one collection)!

# get the wanted collection inside this database
# creating a new collection or using an existing one
collection = database["employees"]


# 1

#   document
doc = {
    "first": "Lee",
    "last": "Woo",
    "dob": "19/09/1984",
    "gender": "f",
    "hair_colour": "black",
    "occupation": "designer",
    "nationality": "American"
}

# using  method  insert_one()
collection.insert_one(doc)


#  2

# my_list = [ element1, element2, element3]
# The following array "new_docs" has 3 elements
new_docs = [
    {
        "first": "Leen",
        "last": "cho",
        "dob": "19/09/1984",
        "gender": "f",
        "hair_colour": "black",
        "occupation": "designer",
        "nationality": "USA"
    },
    {
        "first": "Nick",
        "last": "Fog",
        "dob": "19/09/1974",
        "gender": "m",
        "hair_colour": "black",
        "occupation": "programmer",
        "nationality": "USA"
    },
    {
        "first": "Jen",
        "last": "Tea",
        "dob": "19/09/1977",
        "gender": "f",
        "hair_colour": "brown",
        "occupation": "dba",
        "nationality": "China"
    },
    {
        "sky": "this",
        "color": "blue",
        "when": "rightNow",
        "becauseTheNumberIs": 1010
    }
]

# use the insert_many() method
collection.insert_many(new_docs)

employees = collection.find({})
for employee in employees:
    print(employee)
