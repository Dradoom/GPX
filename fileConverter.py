import os
import gpxpy
import gpxpy.gpx
from models.person import Person
from models.vehicle import Vehicle
from models.track import Track
from models.point import Point
from database import db_session

class FileConverter:
    def __init__(self, folder_path, database):
        self.folder_path = folder_path
        self.database = database

    def convert_files(self):
        files_dir = os.fsdecode(self.folder_path)

        for file in os.listdir(files_dir):
            gpx_file = open(self.folder_path + "/" + file, 'r')
            gpx = gpxpy.parse(gpx_file)
            file_name_arry = file.split('_')
            person = Person(file_name_arry[0], '','','')
            self.get_name(person.nick, person)
            personDB = db_session.query(Person).filter(Person.name == person.name, person.vorname == person.vorname)
            print(personDB)
            if(db_session.execute(personDB, person.name)):
                db_session.add(person)
                db_session.commit()

            vehicle = Vehicle(file_name_arry[1],'')
            db_session.add(vehicle)
            db_session.commit()

            track = Track(file, person, vehicle)
            db_session.add(track)
            db_session.commit()

            # for waypoint in gpx.waypoints:
            #     if(waypoint.latitude == None):
            #         continue
            #     point = Point()
            #     point.lat = waypoint.latitude
            #     point.lon = waypoint.longitude
            #     point.ele = waypoint.elevation
            #     point.dt = waypoint.time
            #     point.tid = track.tid
            #     db_session.add(point)
            #     db_session.commit()
            
            # for waytrack in gpx.tracks:
            #     for segments in waytrack.segments:
            #          for waypoint in segments.points:
            #             if(waypoint.latitude == None):
            #                  continue
            #             point = Point()
            #             point.lat = waypoint.latitude
            #             point.lon = waypoint.longitude
            #             point.ele = waypoint.elevation
            #             point.dt = waypoint.time
            #             point.tid = track.tid

            #             db_session.add(point)
            #             db_session.commit()

    def get_name(self, nick, person):
            match nick:
                 case 'AA':
                      person.name = 'Alef'
                      person.vorname = 'Andreas'
                      person.email = person.vorname + '.' + person.name + '@web.de'
                      return
                 case 'BL':
                      person.name = 'Lange'
                      person.vorname = 'Basti'
                      person.email = person.vorname + '.' + person.name + '@web.de'
                      return
                 case 'KA':
                      person.name = 'Anderson'
                      person.vorname = 'Karin'
                      person.email = person.vorname + '.' + person.name + '@web.de'
                      return
                 case 'PL':
                      person.name = 'Lenz'
                      person.vorname = 'Phil'
                      person.email = person.vorname + '.' + person.name + '@web.de'
                      return
                 case 'SH':
                      person.name = 'Hauser'
                      person.vorname = 'Silke'
                      person.email = person.vorname + '.' + person.name + '@web.de'
                      return
                 case 'SL':
                      person.name = 'Loose'
                      person.vorname = 'Sonia'
                      person.email = person.vorname + '.' + person.name + '@web.de'
                      return
                 case _:
                      return