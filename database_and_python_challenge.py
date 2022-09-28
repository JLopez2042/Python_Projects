import sqlite3
from sqlite3 import *


def create_connection():
    """ create a database connection to a database that resides
        in the memory
    """
    conn = None;
    
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")
        conn.commit()
        cur.execute("INSERT INTO Roster(Name) VALUES ('Jean-Baptiste Zorg', 'Korben Dallas', 'Ak\'not') \
                     INSERT INTO Roster(Species) VALUES ('Human', 'Meat Popsicle', 'Mangalore') \
                     INSERT INTO Roster(IQ) VALUES ('122', '100', '-5') \
                    ")
        conn.commit()
        cur.execute()
    conn.close()

sql = "UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'"

sql = "SELECT * FROM Roster WHERE Species ='Human'"


if __name__ == '__main__':
    create_connection()