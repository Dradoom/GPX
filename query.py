CREATE_DB = "CREATE DATABASE gpx_daten;"
CREATE_TABLE_PERSON = """CREATE TABLE person 
                         (
                         pid INTEGER PRIMARY KEY AUTOINCREMENT,
                         nick TEXT,
                         name TEXT,
                         vorname TEXT,
                         email TEXT
                         );"""
CREATE_TABLE_VEHICLE = """CREATE TABLE fahrzeug
                          (
                          fzid INTEGER PRIMARY KEY AUTOINCREMENT,
                          polkz TEXT,
                          fahrgestellnummer TEXT
                          );"""
CREATE_TABLE_TRACK = """CREATE TABLE track
                        (
                        tid INTEGER PRIMARY KEY AUTOINCREMENT,
                        dateiname TEXT,
                        pid INTEGER,
                        fzid INTEGER,
                        FOREIGN KEY (pid) REFERENCES person(pid),
                        FOREIGN KEY (fzid) REFERENCES fahrzeug(fzid)
                        );"""
CREATE_TABLE_POINTS = """CREATE TABLE punkt
                         (
                         ptid INTEGER PRIMARY KEY AUTOINCREMENT,
                         lat REAL,
                         lon REAL,
                         ele REAL,
                         dt TEXT,
                         tid INTEGER,
                         FOREIGN KEY (tid) REFERENCES track(tid)
                         );"""