from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    email = EmailField(label = 'email:', validators = [DataRequired()])
    password = PasswordField(label = 'password:', validators = [DataRequired()])
    submit = SubmitField(label = "Login")
    
def create_app():
    app = Flask(__name__)
    app.secret_key = "djfsljf"
    Bootstrap(app)

    return app

app = create_app()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied2.html")

# login2.html is used instead of login.html (the initial file
# to show that all the login form could be used with wtf.quick_form(form)
    return render_template("login2.html", form = form)

if __name__ == '__main__':
    app.run(debug=True)
