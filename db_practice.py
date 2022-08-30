#
# Python: 3.6.4
#
# Author: Jacob A. Lopez
#
#
# Purpose: The Tech Academy - Python Course, Creating a database with a script
#                             that iterates through a tuple to adds only files that end in .txt


import sqlite3

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test2.db')

# tuple of files
file_tuple = ('information.docx', 'Hello.txt', 'myImage.png', \
              'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each object in the tuple to find files that end in .txt
for x in file_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple therefore (x,)
        # will denote a one element tuple for each file ending with .txt
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES (?)", (x,))
            print(x)
conn.close()


