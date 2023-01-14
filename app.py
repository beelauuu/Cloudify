import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for

import colors
import shape
import os

load_dotenv()

app = Flask(__name__)

# Spotify Application API details
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPES = ["user-top-read"]


# Home Page
@app.route("/")
def index():
    # Render a template with a login button
    return render_template("index.html")


# Redirect To Login
@app.route("/login")
def login():
    # Redirect the user to the Spotify authorization URL
    return redirect(
        f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={'%20'.join(SCOPES)}&response_type=code&show_dialog=true"
    )


# Settings Page
@app.route("/intermediate")
def intermediate():
    # Grabbing the access token after being passed in from the callback and passing in as a parameter
    access_token = request.args.get("access_token")
    return render_template("intermediate.html", parameter=access_token)


@app.route("/callback")
def callback():
    # Get the authorization code from the query string
    code = request.args.get("code")

    # Use the authorization code to request an access token
    token_response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    # Grab access token and then redirect it to the settings page
    access_token = token_response.json()["access_token"]
    return redirect(url_for("intermediate", access_token=access_token))


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Final Page Display
@app.route("/final", methods=["GET", "POST"])
def final():
    try:
        # Getting the options
        color = request.form["color"]
        shapes = request.form["shape"]
        duration = request.form["duration"]
        access_token = request.form["parameter"]

        # Getting Time-Frame
        if duration == "1 Month":
            top_artists_response = requests.get(
                "https://api.spotify.com/v1/me/top/artists",
                headers={
                    "Authorization": f"Bearer {access_token}",
                },
                params={"limit": "50", "time_range": "short_term"},
            )
            top_artists = top_artists_response.json()["items"]
            artist_names = [artist["name"] for artist in top_artists]
        elif duration == "6 Months":
            top_artists_response = requests.get(
                "https://api.spotify.com/v1/me/top/artists",
                headers={
                    "Authorization": f"Bearer {access_token}",
                },
                params={"limit": "50", "time_range": "medium_term"},
            )
            top_artists = top_artists_response.json()["items"]
            artist_names = [artist["name"] for artist in top_artists]
        else:
            top_artists_response = requests.get(
                "https://api.spotify.com/v1/me/top/artists",
                headers={
                    "Authorization": f"Bearer {access_token}",
                },
                params={"limit": "50", "time_range": "long_term"},
            )
            top_artists = top_artists_response.json()["items"]
            artist_names = [artist["name"] for artist in top_artists]

        # Color
        if color == "Spotify Green":
            color = colors.spotify_green_color_func
        elif color == "Red":
            color = colors.red_color_func
        elif color == "Orange":
            color = colors.orange_color_func
        elif color == "Yellow":
            color = colors.yellow_color_func
        elif color == "Green":
            color = colors.green_color_func
        elif color == "Blue":
            color = colors.blue_color_func
        elif color == "Purple":
            color = colors.violet_color_func
        elif color == "Pink":
            color = colors.pink_color_func
        elif color == "White":
            color = colors.white_color_func
        elif color == "Christmas Mix":
            color = colors.christmas_color_func
        elif color == "Summer Mix":
            color = colors.summer_color_func
        elif color == "Fall Mix":
            color = colors.fall_color_func
        elif color == "Rainbow Mix":
            color = colors.rainbow_color_func
        elif color == "Chinese New Year Mix":
            color = colors.chinese_new_year_color_func

        # Shape
        if shapes == "Spotify":
            shape.generate_spotify_word_cloud(color, artist_names)
        elif shapes == "Moon":
            shape.generate_moon_word_cloud(color, artist_names)
        elif shapes == "Heart":
            shape.generate_heart_word_cloud(color, artist_names)
        elif shapes == "Star":
            shape.generate_star_word_cloud(color, artist_names)
        elif shapes == "Tree":
            shape.generate_tree_word_cloud(color, artist_names)
        elif shapes == "Pacman":
            shape.generate_pacman_word_cloud(color, artist_names)
        elif shapes == "None":
            shape.generate_normal_word_cloud(color, artist_names)

        # Rendering the final page
        return render_template("wordcloud.html")
    except:
        handle_error(400)


@app.errorhandler(Exception)
def handle_error(e):
    return redirect(url_for("login"))


# Running the app
if __name__ == "__main__":
    app.run(debug=True)
