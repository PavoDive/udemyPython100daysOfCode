from flask import Flask
app = Flask(__name__)

@app.route('/') # this is a decorator
def hello_world():
    return 'Hello, World!'

# To run the file it's necessary to do this at a terminal:
# $ export FLASK_APP=hello.py
# $ python -m flask run

# and then visiting the rendered site at:
#  * Running on http://127.0.0.1:5000/

# The following line checks if the file is the application itself, and if so, it runs it:

if __name__ == "__main__":
    app.run()
