from flask import Flask, render_template
import main

app = Flask(__name__)

# Spotify global playlist
playlist_link = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f'

@app.route("/")
def hello_world():
    return render_template("index.html", data=main.grabber(playlist_link), len = len(main.grabber(playlist_link)['track_name']))

if __name__ == "__main__":
    app.run(debug=True)