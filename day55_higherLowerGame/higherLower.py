from flask import Flask
from random import randint

target_number = randint(1, 10)

app = Flask(__name__)

def decorate_page(function):
    def wrapper(**kwargs):
        return f'<h1>{function(**kwargs)["message"]}</h1><img src="' + function(**kwargs)['gif'] + '">'
    return wrapper

@decorate_page
def feedback(message, gif, guess_n = None):
    return {"message": message, "gif": gif}

@app.route("/")
#@decorate_page
def guess_number():
    return feedback(message = "Guess a Number from 1 to 10", gif = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif')


@app.route("/<int:guess>")
#@decorate_page
def process_number(guess, message = None, gif = None):
    if guess == target_number:
        return feedback(message = "You got it right", gif = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif')
    elif guess < target_number:
        return feedback(message = "Too low!", gif = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif')
    else:
        return feedback(message = "Too high!", gif = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif')


if __name__ == "__main__":
    app.run(debug = True)


