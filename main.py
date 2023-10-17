from flask import Flask
from database import init_db, db_session
from fileConverter import FileConverter
from constants import FILE_PATH
import sqlite3

if __name__ == "__main__":

    init_db()

    file_converter = FileConverter(FILE_PATH, db_session)
    file_converter.convert_files()

    app = Flask(__name__)