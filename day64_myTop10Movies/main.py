from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, FloatField, HiddenField
from wtforms.validators import DataRequired
import requests


class MyForm(FlaskForm):
    title = StringField(label = 'Title:', validators = [DataRequired()])
    year = IntegerField(label = 'Year:')
    description = StringField(label = "Description:", validators = [DataRequired()])
    rating = FloatField(label = "Rating:", validators = [DataRequired()])
    ranking = IntegerField(label = "Ranking:", validators = [DataRequired()])
    review = StringField(label = "Review:", validators = [DataRequired()])
    img_url = StringField(label = "Img. URL:", validators = [DataRequired()])
    submit = SubmitField(label = "Submit")


class UpdateForm(FlaskForm):
    rating = FloatField(label = "Rating:", validators = [DataRequired()])
    review = StringField(label = "Review:", validators = [DataRequired()])
    id = HiddenField()
    submit = SubmitField(label = "Submit")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
Bootstrap(app)

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(250), unique = True, nullable = False)
    year = db.Column(db.Integer)
    description = db.Column(db.String(500), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    ranking = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String(500), nullable = False)
    img_url = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return '<Movie %r>' % self.title


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = Movie.query.all()
    return render_template("index.html", movies = movies)


@app.route("/edit", methods = ["GET", "POST"])
def edit():
    edit_form = UpdateForm()
    movie_id = request.args.get("id")
    if request.method == "POST":
        new_rating = edit_form.rating.data
        new_review = edit_form.review.data
        movie_to_update = Movie.query.get(movie_id)
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", form = edit_form)

@app.route("/add", methods = ["GET", "POST"])
def add():
    form = MyForm()
    if form.validate_on_submit():
        new_movie = Movie(title = form.title.data,
                          year = form.year.data,
                          description = form.description.data,
                          rating = form.rating.data,
                          ranking = form.ranking.data,
                          review = form.review.data,
                          img_url = form.img_url.data)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form = form)


@app.route("/delete", methods = ["GET", "POST"])
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)


