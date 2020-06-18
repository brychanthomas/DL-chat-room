#class for adding and retreiving messages from DB

import sqlite3
import time

class DB():
    def __init__(self, filename): #connects to database
        self.conn = sqlite3.connect(filename)

    def add_message(self, user, message): #adds a message to the database
        self.conn.executescript("""INSERT INTO messages (username, messageText, time)
VALUES (\""""+user+'", "'+message+'", '+str(round(time.time()))+" )")
        self.conn.commit()

    def get_new_messages(self): #gets the last 30 messages from the database as a list of tuples
        cursor = self.conn.execute("""SELECT username, messageText, time
FROM messages
ORDER BY time ASC""")
        try:
            return list(cursor.fetchall())[-30:]
        except IndexError:
            return list(cursor.fetchall())

    def execute_command(self, command): #executes a specified SQL command
        self.conn.executescript(command)
        self.conn.commit()




##a.execute_command("""CREATE TABLE messages (
##ID INTEGER PRIMARY KEY AUTOINCREMENT,
##username TEXT,
##messageText TEXT,
##time INTEGER
##)""")
