from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

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
movie_list = []
# TODO:
# Create the HTML for the form below so the user can check off a movie from their list 
# when they've watched it.
# Name the action for the form '/crossoff' and make its method 'post'.

# a form for crossing off watched movies
crossoff_form = """
    <form action="/crossoff" method="post">
        <label for="viewed-movie">
            I want to cross off
            <select name="cars">
                <option value="clueless">Clueless</option>
                <option value="firefly">Firefly</option>
                <option value="equilibrium">Fiat</option>
                <option value="ipman">Ip Man</option>
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
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']    

# TODO:
# modify the crossoff_form above to use a dropdown (<select>) instead of
# an input text field (<input type="text"/>)

@app.route("/add", methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']
    movie_list.append(new_movie)
    # build response content
    new_movie_element = "<strong>" + new_movie + "</strong>"
    sentence = new_movie_element + " has been added to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content

@app.route("/crossoff", methods=['POST'])
def remove_movie():
    viewed_movie = request.form['viewed-movie']
    movie_list.remove(viewed_movie)
    # build response content
    viewed_movie_element = "<strike>" + viewed_movie + "</strike>"
    sentence = viewed_movie_element + " has been removed to your Watchlist!"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content

@app.route("/")
def index():
    edit_header = "<h2>Edit My Watchlist</h2>"

    # build the response string
    # accumulator
    movie_content = """<ul>"""
    # loop through list
    temp = "<li>{0}</li>"
    # other way
    #temp = """<li> """ + movie + """</li>"""
    for movie in movie_list:
        # combine <li> and movie 
        movie_content += temp.format(movie)
    # make html fragment for list
    movie_content += "</ul>"
    content = page_header + movie_content + edit_header + add_form + crossoff_form + page_footer

    return content


app.run()