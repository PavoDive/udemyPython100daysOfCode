import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import pandas as pd

UPLOAD_FOLDER = '/home/gp/Documents/python/udemyPython100daysOfCode/day92_image_palette_generator/static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def find_colors(image):
    width, length, _ = image.shape
    if _ == 4:
        image = image[:,:,0:3]
    colors = np.reshape(image, (width * length, 3))
    flattened_colors = colors.view(dtype=[('R', 'uint8'), ('G', 'uint8'), ('B', 'uint8')])

    # Convert the flattened view to a 1D array of structured dtype
    structured_colors = flattened_colors.reshape(colors.shape[0])

    # Get unique colors and their counts
    unique_colors, counts = np.unique(structured_colors, return_counts=True)

    df = pd.DataFrame(unique_colors)
    df["counts"] = counts
    df.reset_index(drop = True, inplace = True)
    df["hex"] = df.apply(lambda y: f"#{y['R']:02x}{y['G']:02x}{y['B']:02x}", axis = 1)
    df["rgb"] = df.apply(lambda y: f"({y['R']},{y['G']},{y['B']})", axis = 1)
    return df.sort_values(by = "counts", ascending = False).iloc[0:19, :]
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filename_path)
            img = Image.open(filename_path)
            colors_top_20 = find_colors(np.asarray(img))
            df = colors_top_20[["rgb", "hex", "counts"]]
            tables = df.to_html(index = False, classes = "data")
            titles = df.columns.values
            return render_template('output.html', df = df, user_image = filename)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)




# from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# app = Flask(__name__)

# app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# ##CREATE TABLE IN DB
# # UserMixin is a flask_login class for users with methods to check if user is loged in, etc.
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
# #Line below only required once, when creating DB. 
# # db.create_all()


# # this part here is to remember login users and to avoid non-registered users accessing users-only pages

# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# @app.route('/')
# def home():
#     return render_template("index.html")


# @app.route('/register', methods = ["GET", "POST"])
# def register():
#     if request.method == "POST":
#         name = request.form.get("name")
#         email = request.form.get("email")
#         passwd = generate_password_hash(request.form.get("password"), method = "pbkdf2:sha256", salt_length= 8 )

#         if db.session.query(User).filter_by(email = email).count() < 1:
#             new_user = User(name = name, email = email, password = passwd)
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user)
#         else:
#             flash("User already exists", "danger")
#             return redirect(url_for("login"))

#         # notice the use of redirect + url_for
#         return redirect(url_for("secrets", name = new_user.name))

#     return render_template("register.html")


# @app.route('/login', methods = ["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get("email")
#         passwd = request.form.get("password")

#         user = User.query.filter_by(email=email).first()
#         # This is the case when user comes empty:
#         if type(user).__name__ == "NoneType":
#             flash("Email is not in database", "danger")
#         else:
#             if check_password_hash(pwhash = user.password, password = passwd):
#                 login_user(user)
#                 return redirect(url_for('secrets', name = user.name))
#             else:
#                 flash("Invalid Username or password!", "danger")

#     return render_template("login.html")


# @app.route('/secrets')
# @login_required
# def secrets():
#     # notice the capture of the name by means of request.args.get
#     name = request.args.get('name')
#     return render_template("secrets.html", name = name)


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for("home"))


# @app.route('/download')
# @login_required
# def download():
#     # send_from_directory(directory, path, **kwargs)
#     return send_from_directory("static", "files/cheat_sheet.pdf", as_attachment = True)


# if __name__ == "__main__":
#     app.run(debug=True)
