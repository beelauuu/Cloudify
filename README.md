# Cloudify

Web application which generates a custom wordcloud of a user's top 50 artists in the past month, 6 months, and all-time.

The web application is hosted on: https://cloudify.herokuapp.com/.

Admittedly, this is my first attempt at a medium-scale project so a lot of the code isn't great. I tried to leave things like comments to help.

## Setting up the App Locally

This app runs completely on Python Flask in the backend + vanilla JavaScript/HTML/CSS on the front end. 

Simply clone the repository and install the libraries in the requirements file running:

    $ pip install -r requirements.txt
 
I'd advise you make a virtual environment first before installing though of course :)

### Running the App 

You will need to register your app and get your own credentials from the Spotify for Developers Dashboard in order for this to work.

To do so, go to [your Spotify for Developers Dashboard](https://beta.developer.spotify.com/dashboard) and create your application. In my own development process, I registered these Redirect URIs:

- http://localhost:3000/callback

Once you have created your app, load the `CLIENT_ID`, `REDIRECT_URI` and `CLIENT_SECRET` into the app.py file.

Finally to run the app, open the folder, and run its `app.py` file:

    $ flask run --host=localhost --port=5000

Then, open `http://localhost:5000` in a browser or just follow the link it prints out in the terminal if run correctly.