from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


def generate_movie_list(movies):
    movie_content ="<ul>"

    list_item = "<li>{0}</li>"

    for movie in movies:
        movie_content += list_item.format(movie)
    
    movie_content += "</ul>"

    return movie_content

def generate_select_list(movies):
    options = ""

    for movie in movies:
        options += "<option value='{0}'>{0}</option>".format(movie)
    
    return options

movie_list = []

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>FlickList</h1>
"""

page_footer = """
    </body>
</html>
"""

# a form for adding new movies
add_form = """
    <form action="/add" method="post">
        <label for="new-movie">
            I want to add
            <input type="text" id="new-movie" name="new-movie"/>
            to my watchlist.
        </label>
        <input type="submit" value="Add It"/>
    </form>
"""

# TODO:
# Create the HTML for the form below so the user can check off a movie from their list 
# when they've watched it.
# Name the action for the form '/crossoff' and make its method 'post'.

# TODO:
# modify the crossoff_form above to use a dropdown (<select>) instead of
# an input text field (<input type="text"/>)

# a form for crossing off watched movies
crossoff_form = """
    <form action="/crossoff" method="post">
        <label for="crossed-off-movie">
            Cross off
            <select id="crossed-off-movie" name="crossed-off-movie">
                {0}
            </select>
            from my watchlist.
        </label>
        <input type="submit" value="Remove It"/>
    </form>
"""

# TODO:
# Finish filling in the function below so that the user will see a message like:
# "Star Wars has been crossed off your watchlist".
# And create a route above the function definition to receive and handle the request from 
# your crossoff_form.
@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']    

    index = movie_list.index(crossed_off_movie)

    del movie_list[index]

    crossed_movie_element = "<strike>" + crossed_off_movie + "<strike>"
    sentence = crossed_movie_element + " has been crossed off your Watchlist!"
    link = """
        <p>
            <a href="/">back to index</a>
        </p>
    """
    content = page_header + "<p>" + sentence + "</p>" + link + page_footer

    return content

@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']

    movie_list.append(new_movie)

    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    link = """
        <p>
            <a href="/">back to index</a>
        </p>
    """
    content = page_header + "<p>" + sentence + "</p>" + link + page_footer

    return content


@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    movie_content = generate_movie_list(movie_list)

    # build the response string
    content = page_header + movie_content + edit_header + add_form + crossoff_form.format(generate_select_list(movie_list)) + page_footer

    return content


app.run()
