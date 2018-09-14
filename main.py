import random
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie_today = get_random_movie()
    movie_tomorrow = get_random_movie()

    while movie_today is movie_tomorrow:
        movie_today = get_random_movie()
        movie_tomorrow = get_random_movie()

    # build the response string
    today_content = "<h1>Movie of the Day</h1>"
    today_content += "<ul>"
    today_content += "<li>" + movie_today + "</li>"
    today_content += "</ul>"
    
    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    tomorrow_content = "<h1>Tommorrow's Movie</h1>"
    tomorrow_content += "<ul>"
    tomorrow_content += "<li>" + movie_tomorrow + "</li>"
    tomorrow_content += "</ul>"

    return today_content + tomorrow_content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = [
        "The Big Lebowski",
        "Firefly",
        "Love Actually",
        "Clueless",
        "Hitchhiker's Guide to the Galaxy"]

    # TODO: randomly choose one of the movies, and return it
    return random.choice(movie_list)


app.run(port=5001)
