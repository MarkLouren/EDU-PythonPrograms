import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor() #set up connection to db
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table) #create a table
user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
(2, 'rolf', 'asdf'),
(3, 'mike', 'xyz')
]
cursor.executemany(insert_query,users) #to safe many users
select_query ="SELECT * FROM users" # or "SELECT id FROM users"
for row in cursor.execute(select_query): #show data from the database
    print(row)
#save a query
connection.commit()
#close connection to db
connection.close()
