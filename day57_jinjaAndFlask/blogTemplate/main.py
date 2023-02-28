from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blogs = response.json()

@app.route('/')
def home():
    return render_template("index.html", blogs = blogs)

@app.route("/blog/<int:id>")
def get_blog(id):
    post = [post for post in blogs if post["id"] == id][0]
    return render_template("post.html", post = post)


if __name__ == "__main__":
    app.run(debug=True)
