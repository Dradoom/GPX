import os
import gpxpy
import gpxpy.gpx

class FileConverter:
    def __init__(self, folder_path, database):
        self.folder_path = folder_path
        self.database = database

    def convert_files(self):
        files_dir = os.fsdecode(self.folder_path)
        count = 1
        for file in os.listdir(files_dir):
            gpx_file = open(self.folder_path + "/" + file, 'r')
            gpx = gpxpy.parse(gpx_file)
            print(gpx)