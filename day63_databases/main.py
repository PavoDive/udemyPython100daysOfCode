from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'

db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique = True, nullable = False)
    author = db.Column(db.String(250), nullable = False)
    rating = db.Column(db.Float(), nullable = False)

    def __repr__(self):
        return '<Books %r>' % self.title

# https://stackoverflow.com/questions/73999854/flask-error-runtimeerror-working-outside-of-application-context
with app.app_context():
    db.create_all()

# after this I had  to run this in the shell:
# flask --app main shell
# then in that shell I had to run
# from main import db
# db.create_all()
# from main import Books
# book1 = Books(title = "djsflsjf", author = "jdlfsjf", rating = 3.5)
# db.session.add(book1)
# db.session.commit()

# ---------- This is pure sqlite ----------
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
# ---------- end of pure sqlite ----------

all_books = []

@app.route('/')
def home():
    bks = Books.query.all()
    return render_template("index.html", books = bks)


@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Books(title = request.form["title"], author = request.form["author"], rating = request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        # new_book = {"title": request.form["title"],
        #             "author": request.form["author"],
        #             "rating": request.form["rating"]
        #             }
        # all_books.append(new_book)
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods = ["GET", "POST"])
def edit():
    # I needed help on this one. The hidden input was a trick!
    if request.method == "POST":
        book_id = request.form["id"] # the hidden input
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get("id")
    book_to_display = Books.query.get(book_id)
    return render_template("edit.html", book = book_to_display)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)

