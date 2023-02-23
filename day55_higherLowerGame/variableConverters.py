from flask import Flask
app = Flask(__name__)

@app.route('/') # this is a decorator
def hello_world():
    return 'Hello, World!'


@app.route("/<username>") #whatever is between <> will be taken as a variable:
def say_hello(username):
    return f"Hello there {username}." # {username + 12}." # + 12 was added to test the debug functionality. At run time it provides a code that can be used to further debug from the front end.

# it is even possible to get several variables of different types (see https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules): string, int, float, path (like string but also accepts slashes) and uuid (universally unique identifier like 123e4567-e89b-12d3-a456-426614174000)

@app.route("/<user>/<int:age>")
def greet(user, age):
    return f"Welcome {user}. You are {age} years old."

# To run the file it's necessary to do this at a terminal:
# $ export FLASK_APP=hello.py
# $ python -m flask run

# and then visiting the rendered site at:
#  * Running on http://127.0.0.1:5000/

# The following line checks if the file is the application itself, and if so, it runs it:

# this was the original code
# if __name__ == "__main__":
#     app.run()


if __name__ == "__main__":
    app.run(debug = True) # this puts the debug mode on and debug output is thrown on errors
