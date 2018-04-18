"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def play_game():
    """Start game madlibs"""
   
    option = request.args.get("is_playing")
    if option:
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Display madlib from user input"""
    words = {}
    words["nouns"] = request.args.get("noun").split()
    words["person"] = request.args.get("person")
    words["adjs"] = choice(request.args.get("adj").split())
    words["colors"] = choice(request.args.getlist("colors"))

    # print words["colors"]
    madlibs = ["madlib1.html", "madlib2.html", "madlib3.html"]

    if len(words["nouns"]) == 2:
        madlib = madlibs[0]
    elif len(words["nouns"]) < 2:
        madlib = madlibs[1]
    else:
        madlib = madlibs[2]

    return render_template(madlib, m_words = words)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
