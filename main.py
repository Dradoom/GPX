import sqlitedb
import fileConverter
from constants import DB_NAME, FILE_PATH

if __name__ == "__main__":
    sql_database = sqlitedb.SqliteDatabase(DB_NAME)
    if not sql_database.database_exists():
        sql_database.create_database()
        sql_database.create_tables()

    file_converter = fileConverter.FileConverter(FILE_PATH,sql_database)

    file_converter.convert_files()