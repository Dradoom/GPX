import os
import sqlite3
import query

class SqliteDatabase:
    def __init__(self, db_name):
        self.database = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect("{}.db".format(self.database))

    def create_database(self):
        self.connect()

    def drop_database(self):
        if self.database_exists():
            os.remove("{}.db".format(self.database))

    def database_exists(self):
        return os.path.exists("{}.db".format(self.database))

    def create_tables(self):
        with self.connection:
            cursor = self.connection.cursor()
            sql = query.CREATE_TABLE_PERSON
            cursor.execute(sql)

            cursor = self.connection.cursor()
            sql = query.CREATE_TABLE_VEHICLE
            cursor.execute(sql)

            cursor = self.connection.cursor()
            sql = query.CREATE_TABLE_TRACK
            cursor.execute(sql)

            sql = query.CREATE_TABLE_POINTS
            cursor.execute(sql)
            print("Tables created!")
            cursor.close()

            self.connection.commit()