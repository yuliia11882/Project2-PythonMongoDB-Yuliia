import pymongo


db_url = 'mongodb://localhost:27017/'       # or          client = pymongo.MongoClient("mongodb://localhost:27017/")
client = pymongo.MongoClient(db_url)
#  get these two things: database name ["PyDB-local"] + the collection name ["employees"]
# access database: PyDB-local
# creating a new db or using an existing one

database = client["PyDB-local"]


 #  get the collection inside this database
collection = database["employees"]


#  Create/Define a function that display a list of options named "display_options"        
def display_options():

    print("") # for space
    print("1. Add a record")
    print("2. View a record")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    #  assing (=) the returned value of input() method
    # to a varible named "user_option"
    user_option = input("Enter option number: ")
    return user_option


#
#
#


# ....more CRUD continue ........


#
#
#



# helping function        Display/GET RECORD

def get_record():
    print("") # for space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")

    try:
        document=collection.find_one({'first':first.lower(), 'last':last.lower()})
    except:
        print("SURPRISE =>>>>>   ERROR accessing the database")
    
    if not document: #  if doc has no value (has nothing)
        # then  print another blank line 
        print("")
        # and then say "Error! No results found"
        print("Error! No results found.")
   
    return document # we will return document whether a record is found or not found



#TRy
#   Display/GET ALL RECORDS

# def get_All_records():
    # print("") # for space 
    # first = input("Enter the first name: ")
    # last = input("Enter the last name: ")
    # dob = input("Enter the dob: ")
    # gender = input("Enter the gender: ")
    # hair_colour = input("Enter the hair_colour: ")
    # occupation = input("Enter the occupation: ")
    # nationality = input("Enter the nationality: ")

   # try:
    #    document=collection.find_one({'first':first.lower(), 'last':last.lower(),"dob": dob,"gender":gender.lower(),"hair_colour":hair_colour.lower(),"occupation": occupation.lower(),"nationality":nationlity.lower()})
    # or
    #   document=collection.find({new_doc})
   # except:
        #print("SURPRISE =>>>>>   ERROR accessing the database")
    
    #if not document: #  if doc has no value (has nothing)
        # then  print another blank line 
      #  print("")
        # and then say "Error! No results found"
      #  print("Error! No results found.")
   
   # return document # we will return document whether a record is found or not found

# ? get all records   ???
#employees = collection.find({})
#for employee in employees:
    #print(employee)

# ?is there such thing like   document=collection.find_MANY?





# first CRUD function:


#  ADD/insert
def add_record(): 

    print("") # for space 
    first = input("Enter the first name: ")
    last = input("Enter the last name: ")
    dob = input("Enter the date of birth: ")
    gender = input("Enter the gender: ")
    hair_colour = input("Enter the hair colour: ")
    occupation = input("Enter the occupation: ")
    nationlity = input("Enter the nationality: ")
    salary = input("enter your salary: ")
# building  dictionary to insert into the database


    new_doc =   { 
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender.lower(),
        "hair_colour": hair_colour.lower(),
        "occupation": occupation.lower(),
        "nationality": nationlity.lower(),
        "salary": salary.lower()
    }

  # test code
    try:
        collection.insert_one(new_doc)
        print("")
        print("Document inserted")

# handle error
    except:
        print("Error accessing the database")
 





# VIEW

def view_record():
    doc = get_record()
    if doc:
        # if we do have some results we will continue with printing the full record
        for key, value in doc.items():
            if key!="_id":
                if (isinstance(value,str)):
                    print(key.capitalize(),": ", value.capitalize())    
                else:
                      print(key.capitalize(),": ", value)  









# DELETE
               
def delete_record():
    # We also need to get the reocord by the name by calling our helper function get_record()
    doc = get_record() # getting the result from get_record() function

    if doc: # check if any result has been returned from get_record()
        print("")
        for key, value in doc.items():
            if key!="_id":
                if (isinstance(value,str)):
                    print(key.capitalize(),": ", value.capitalize())    
                else:
                      print(key.capitalize(),": ", value)  

        print("")
        confirm = input("Is this the document you want to delete?\nY or N: ")
        print("")

        # Our if condition to perform the delete operation or just ignore it based on the user's input
        if confirm.lower()=='y':
            try:
                collection.delete_one(doc)
                print("")
                print("Document deleted")
    
            # The except block lets you handle the error.
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")















# EDIT

def edit_record():
    #  store the results of our get_record() function in variable "doc"
    doc = get_record()
    if doc: # check if there is something in doc
        #  create an empty dictionary called "update_doc"
        update_doc = {} # to create a new empty doc
        # this "update_doc" is empty now but later it will contain the field(s) values that the user input
        print("") #space
        #  iterate through doc items using k,v in doc.items:
        #  add values to that dictionary. 
        
       

        for key, value in doc.items():
        # filter out the ID field
            if key != "_id":    
                # add values to our update_doc dictionary
                #  value will be equal to  input : using input() method
                
               
                update_doc[key] = input(key+ f" [{value}] :").lower() 
               

                # leave information the same as it was before
                if  update_doc[key]==" ":
                    # we will reasign the current value to the same key again
                    update_doc[key] = value

        # for testing we will print the udpate_doc that contains all the values:
        print("") # space
        print ("The new updated document:")
        print ("_____________________________")
        for key, value in update_doc.items():
            print(key, ": [", value, "]")

      
        try:
            # collection.update_one() method: 
            collection.update_one(doc, { '$set': update_doc})     
          

            print("")
            print("Document updated")
        except:
            print("Error accessing the database")
      




#
#
#  Create a function keep_asking()
def keep_asking():
    # use while True,
    #  will run  until terminate it
    while True:
        #  call/run the function):
        # because our function is returning a value (1,2,3,4, 5) base on the user input
        #  save  returned value into  variable  "option"
        # Or store the result of our   display_options   function in a variable called "option".
        option = display_options()
        if option == "1":
            print("You have selected option 1: ADD NEW RECORD ")
            add_record()

        elif option == "2":
            print("You have selected option 2: VIEW  RECORD  ")
            view_record() 

        elif option == "3":
            print("You have selected option 3: EDIT  RECORD ")
            edit_record()

        elif option == "4":
            print("You have selected option 4: DELETE RECORD ")
            delete_record()


        elif option == "5":


            #  to close  connection with the database
            # use method named "close()"
            #close our connection with MongoDB
            client.close()

          

            input(" THE END :) ")


           #"break" to stop the while loop:
            break

       
        # if we don't select options 1, 2, 3, 4, 5
        # then "Invalid Option!"
        else:
            print("Invalid Option!")


#  Call function keep_asking()
keep_asking()
