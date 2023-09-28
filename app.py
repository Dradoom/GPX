from flask import Flask, render_template
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5

load_dotenv() 


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/", methods=["POST", "GET"])
@app.route("/index", methods=["POST", "GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)