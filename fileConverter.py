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
            db_session.add(person)
            db_session.commit()
            
            for waypoint in gpx.waypoints:
                waypoint_lat = waypoint.latitude
                waypoint_lon = waypoint.longitude
                waypoint_ele = waypoint.elevation