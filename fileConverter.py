import os
import gpxpy
import gpxpy.gpx
from models.person import Person
from models.vehicle import Vehicle
from models.track import Track
from models.point import Point
from database import db_session
from dataHandling import DataHandling
import query

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
               personDB = None
               personDB = db_session.query(Person).filter_by(name=person.name).first()
               if(personDB == None or personDB.pid == None):
                    db_session.add(person)
               else:
                    person = personDB

               db_session.commit()

               vehicle = Vehicle(file_name_arry[1],'')
               vehicleDB = None
               vehicleDB = db_session.query(Vehicle).filter_by(polkz=vehicle.polkz).first()
               if(vehicleDB == None or vehicleDB.fzid == None):
                    db_session.add(vehicle)
               else:
                    vehicle = vehicleDB
               db_session.commit()

               track = Track(file, person, vehicle)
               trackDB = None
               trackDB = db_session.query(Track).filter_by(dateiname=file).first()
               if(trackDB == None or trackDB.tid == None):
                    db_session.add(track)
               else:
                    track = trackDB

               db_session.commit()

               print(track.dateiname)

               for waypoint in gpx.waypoints:
                    point = Point()
                    point.lat = waypoint.latitude
                    point.lon = waypoint.longitude
                    point.ele = waypoint.elevation
                    point.dt = waypoint.time
                    point.tid = track.tid

                    pointDB = None
                    pointDB = db_session.query(Point).filter_by(dt=point.dt, lat=point.lat, lon=point.lon, ele=point.ele, tid=point.tid).first()
                    if(pointDB == None or pointDB.ptid == None):
                         db_session.add(point)
                    else:
                         point = pointDB
               db_session.commit()

               dataHandling = DataHandling()
               connection = dataHandling.get_connection()
               cursor = connection.cursor()
               for waytrack in gpx.tracks:
                    for segments in waytrack.segments:
                         
                        
                         if(cursor is None):
                              print("keine Connection")
                              continue

                         for waypoint in segments.points:                             
                              point = Point()
                              point.lat = waypoint.latitude
                              point.lon = waypoint.longitude
                              point.ele = waypoint.elevation
                              point.dt = waypoint.time
                              point.tid = track.tid
                              
                              cursor.execute(query.SELECT_POINT, (point.lat, point.lon, point.ele, point.dt, point.tid))
                              existing_point = cursor.fetchall()
                              if(existing_point.__len__() == 0):
                                   cursor.execute(query.INSERT_POINT, (point.lat, point.lon, point.ele, point.dt, point.tid))
               connection.commit()
               connection.close()  

               # for waytrack in gpx.tracks:
               #      for segments in waytrack.segments:
               #           for waypoint in segments.points:
               #                point = Point()
               #                point.lat = waypoint.latitude
               #                point.lon = waypoint.longitude
               #                point.ele = waypoint.elevation
               #                point.dt = waypoint.time
               #                point.tid = track.tid

               #                pointDB = None
               #                pointDB = db_session.query(Point).filter_by(dt=point.dt, lat=point.lat, lon=point.lon, ele=point.ele).first()
               #                if(pointDB == None or pointDB.ptid == None):
               #                     db_session.add(point)
               #                else:
               #                     point = pointDB
               # db_session.commit()
               # db_session.close()

        

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