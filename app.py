from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import gpxpy
from database import init_db, db_session
from fileConverter import FileConverter
from flask_bootstrap import Bootstrap5
from models.point import Point
from models.track import Track
from models.person import Person
from models.vehicle import Vehicle
import json

load_dotenv() 

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def index():
    items1 = Track.query.all()
    items2 = Person.query.all()
    items3 = Vehicle.query.all()
    return render_template("index.html", items1=items1, items2=items2, items3=items3)

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form['user_text']
    file_converter = FileConverter(text, db_session)
    file_converter.convert_files()

    return redirect(url_for('index'))

@app.route('/process_selection', methods=['POST'])
def process_selection():
    selected_item_ids = request.form.getlist('selected_items')
    selected_items = Track.query.filter(Track.tid.in_(selected_item_ids)).all()

    # Gather all points of the selected tracks
    track_points = []
    tracks = []
    for item in selected_items:
        points = Point.query.filter_by(tid = item.tid).all()
        track_points = []
        for point in points:
            tp = {
                'tid': point.tid,
                'lat': point.lat,
                'lon': point.lon,
                'ele': point.ele,
            }

            track_points.append(tp)
        
        track = {
            'tid': item.tid,
            'points': track_points,
        }

        tracks.append(track)


    tracks_json = json.dumps(tracks)

    return render_template('index.html', items1 = Track.query.all(), items2 = Person.query.all(), items3 = Vehicle.query.all(), tracks=tracks_json)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
