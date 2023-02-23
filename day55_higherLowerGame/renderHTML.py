from flask import Flask
app = Flask(__name__)

# it is possible to render html code 
@app.route('/') # this is a decorator
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
        '<p>This is a paragraph.</p>'\
        '<img src="https://media.giphy.com/media/3NtY188QaxDdC/giphy.gif">'

# The following line checks if the file is the application itself, and if so, it runs it:


if __name__ == "__main__":
    app.run(debug = True) # this puts the debug mode on and debug output is thrown on errors
