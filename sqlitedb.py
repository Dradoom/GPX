import os
import sqlite3
import query
from constants import DB_NAME

def connect(database = DB_NAME):
    return sqlite3.connect("{}.db".format(database))

def create_database(database=DB_NAME):
    connect(database)

def drop_database(database = DB_NAME):
    if database_exists(database):
        os.remove("{}.db".format(database))

def database_exists(database=DB_NAME):
    return os.path.exists("{}.db".format(database))

def create_tables(connection):
    with connection:
        cursor = connection.cursor()
        sql = query.CREATE_TABLE_PERSON
        cursor.execute(sql)

        cursor = connection.cursor()
        sql = query.CREATE_TABLE_VEHICLE
        cursor.execute(sql)

        cursor = connection.cursor()
        sql = query.CREATE_TABLE_TRACK
        cursor.execute(sql)

        sql = query.CREATE_TABLE_POINTS
        cursor.execute(sql)
        print("Tables created!")
        cursor.close()

        connection.commit()