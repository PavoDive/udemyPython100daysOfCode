from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
# UserMixin is a flask_login class for users with methods to check if user is loged in, etc.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


# this part here is to remember login users and to avoid non-registered users accessing users-only pages

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        passwd = generate_password_hash(request.form.get("password"), method = "pbkdf2:sha256", salt_length= 8 )

        if db.session.query(User).filter_by(email = email).count() < 1:
            new_user = User(name = name, email = email, password = passwd)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        else:
            flash("User already exists", "danger")
            return redirect(url_for("login"))

        # notice the use of redirect + url_for
        return redirect(url_for("secrets", name = new_user.name))

    return render_template("register.html")


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        passwd = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        # This is the case when user comes empty:
        if type(user).__name__ == "NoneType":
            flash("Email is not in database", "danger")
        else:
            if check_password_hash(pwhash = user.password, password = passwd):
                login_user(user)
                return redirect(url_for('secrets', name = user.name))
            else:
                flash("Invalid Username or password!", "danger")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    # notice the capture of the name by means of request.args.get
    name = request.args.get('name')
    return render_template("secrets.html", name = name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    # send_from_directory(directory, path, **kwargs)
    return send_from_directory("static", "files/cheat_sheet.pdf", as_attachment = True)


if __name__ == "__main__":
    app.run(debug=True)
