import sqlite3

class DataHandling():

    def get_connection(self):
        return sqlite3.connect('.\\tmp\\gpx_daten.db')

    def get_cursor(self):
        try:
            sqliteConnection = self.get_connection()
            return sqliteConnection.cursor()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)