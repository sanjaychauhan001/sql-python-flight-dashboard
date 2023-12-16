import mysql.connector

# connect to the database server
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='indigo'
    )
    mycorsor = conn.cursor()
    print("Connection Established")

except:
    print('Connection Error')

# create a database on the db server
"""try:
    mycorsor.execute("CREATE DATABASE indigo")
    conn.commit()
    print("database created")
except:
    print("some error occured")"""

# create a table
# airport-> airport_id / code/ name

#try:
    #mycorsor.execute("""
    #CREATE TABLE airport(
     #    airport_id INTEGER PRIMARY KEY,
      #   code VARCHAR(10) NOT NULL,
       #  city VARCHAR(50) NOT NULL,
        # name VARCHAR(255) NOT NULL
    #)
    #""")
    #conn.commit()
    #print('table created')
#except:
 #      print('some error occured')


# Insert data into table
#try:
#    mycorsor.execute("""
 #   INSERT INTO airport VALUES
  #  (1, 'DEL', 'New Delhi', 'IGIA'),
   # (2, 'CCU', 'Kolkata', 'NSCA'),
    #(3, 'BOM', 'Mumbai', 'CSMA')
    #""")
    #conn.commit()
    #print("values inserted")
#except:
 #   print('some error occured')

# search/retrive
mycorsor.execute("SELECT * FROM airport WHERE airport_id > 1")
data = mycorsor.fetchall()
print(data)

# update
mycorsor.execute("""
UPDATE airport
SET city = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

mycorsor.execute("SELECT * FROM airport")
data = mycorsor.fetchall()
print(data)

# delet
mycorsor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycorsor.execute("SELECT * FROM airport")
data = mycorsor.fetchall()
print(data)
