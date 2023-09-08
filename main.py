import sqlitedb
from constants import DB_NAME

def get_db_connection():
    connection = sqlitedb.connect()

    return connection

if __name__ == "__main__":
    if not sqlitedb.database_exists(DB_NAME):
        sqlitedb.create_database()
        connection = sqlitedb.connect()
        sqlitedb.create_tables(connection)
    else:
        sqlitedb.drop_database(DB_NAME)
        sqlitedb.create_database()
        connection = sqlitedb.connect()
        sqlitedb.create_tables(connection)