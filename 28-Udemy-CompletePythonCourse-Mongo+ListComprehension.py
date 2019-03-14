import pymongo
uri = "mongodb://127.0.0.1:27017" #default address for mongo db on the local machine ##Universal Resource Identifier
client = pymongo.MongoClient(uri)
database=client['fullstack'] #name of db in Mongo
collection=database['students']
students = [someone['mark'] for someone in collection.find({}) if someone['mark']==100.0] # get list with specific elements and values
#students = [someone['mark'] for someone in collection.find({})] - get a value from the one element
#students = [student for student in collection.find({})]  -list comprehension
#  It's the same as:
#students = collection.find({}) #cursor object db
#student_list =[]
#for student in students:
    #student_list.append(student)
print (students)
