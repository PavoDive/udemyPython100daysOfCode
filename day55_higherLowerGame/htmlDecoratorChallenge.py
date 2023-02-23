from flask import Flask

app = Flask(__name__)

#define decorator to make bold, emphasis and underline

def make_bold(function):
    def mb():
        a = f"<b>{function()}</b>" # I was actually very close. I had: f"<b>{function}</b>". I just missed the parenthesis :(
        return a
    return mb

def make_emphasis(function):
    def me():
        return "<em>" + function() + "</em>"
    return me

@app.route("/bye")
@make_bold
@make_emphasis
def say_bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug = True)

