from flask import Flask, render_template
from random import randint
import time
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = randint(1, 100)
    ## variables can be given as arguments to the render_template function:
    current_year = time.strftime("%Y")
    return render_template("index.html", rand = random_number, current_year = current_year, user_name = "Gio Pavo")

@app.route("/<username>")
def get_username_data(username):
    response = requests.get("https://api.agify.io?name="+username)
    age = response.json()["age"]

    response2 = requests.get("https://api.genderize.io?name=" + username)
    gender = response2.json()["gender"]

    return render_template("age-gender.html", age = age, gender = gender, username = username.title())


@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    return render_template("blog.html", blogs = blogs)

    
if __name__ == "__main__":
    app.run(debug= True)
