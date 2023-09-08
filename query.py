CREATE_DB = "CREATE DATABASE gpx_daten;"
CREATE_TABLE_PERSON = """CREATE TABLE person 
                         (
                         pid INTEGER PRIMARY KEY AUTOINCREMENT,
                         nick TEXT,
                         name TEXT,
                         vorname TEXT,
                         email TEXT
                         );"""
INSERT_PERSON= """INSERT INTO person (nick, name, vorname, email)
                VALUES ({}, {}, {}, {})"""
CREATE_TABLE_VEHICLE = """CREATE TABLE fahrzeug
                          (
                          fzid INTEGER PRIMARY KEY AUTOINCREMENT,
                          polkz TEXT,
                          fahrgestellnummer TEXT
                          );"""
INSERT_VEHICLE= """INSERT INTO vehicle (polkz, fahrgestellnummer)
                VALUES ({}, {})"""
CREATE_TABLE_TRACK = """CREATE TABLE track
                        (
                        tid INTEGER PRIMARY KEY AUTOINCREMENT,
                        dateiname TEXT,
                        pid INTEGER,
                        fzid INTEGER,
                        FOREIGN KEY (pid) REFERENCES person(pid),
                        FOREIGN KEY (fzid) REFERENCES fahrzeug(fzid)
                        );"""
INSERT_TRACK= """INSERT INTO vehicle (dateiname, pid, fzid)
                VALUES ({}, {}, {})"""
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
INSERT_TRACK= """INSERT INTO vehicle (lat, lon, ele, dt, tid)
                VALUES ({}, {}, {}, {}, {})"""