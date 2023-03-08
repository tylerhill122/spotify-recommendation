from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import main

app = Flask(__name__)

# MongoDB Setup
app.config["MONGO_URI"] = "mongodb://localhost:27017/spotify"
mongo = PyMongo(app)

# Spotify global playlist
playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/playlist")
def playlist():
    pList = main.grabber(playlist_link)
    playlist_db = mongo.db.playlists
    playlist_db.insert_one(pList)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)