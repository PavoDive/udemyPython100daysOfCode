from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)



@app.route("/")
def home():
    return render_template("index.html")
    

@app.route("/random", methods = ["GET"])
def random_cafe():
    cafes = db.session.query(Cafe).all()
    rand_cafe = random.choice(cafes)
    rand_cafe = rand_cafe.__dict__
    del rand_cafe["_sa_instance_state"] # can't be passed to json
    return jsonify(cafe = rand_cafe)
    

@app.route("/all", methods = ["GET"])
def all_cafes():
    cafes = db.session.query(Cafe).all()
    all_cafes = []
    for cafe in cafes:
        cafe = cafe.__dict__
        del cafe["_sa_instance_state"]
        all_cafes.append(cafe)
    return jsonify(all_cafes)


@app.route("/search", methods = ["GET"])
def search_cafe():
    target_location = request.args.get("loc")
    cafes_in_location = Cafe.query.filter_by(location = target_location).all()
    if len(cafes_in_location) == 0:
        return jsonify({"error": {"Not Found": "Sorry, we don't have a cafe at that location."}})
    else:
        matching_cafes = []
        for cafe in cafes_in_location:
            cafe = cafe.__dict__
            del cafe["_sa_instance_state"]
            matching_cafes.append(cafe)
        return jsonify(matching_cafes)


@app.route("/add", methods = ["POST"])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("loc"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("toilet")),
        has_wifi = bool(request.form.get("wifi")),
        has_sockets = bool(request.form.get("sockets")),
        can_take_calls = bool(request.form.get("calls")),
        coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response = {"Success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods = ["PATCH"])
def update_price(cafe_id):
    target_cafe = Cafe.query.get(cafe_id)
    new_price = request.form.get("new_price")
    if target_cafe:
        target_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response = {"Success": "Successfully updated the price of the cafe."}), 200 # 200 is ok
    else:
        return jsonify(response = {"Error": f"Sorry we didn't find a cafe with id {cafe_id}."}), 404 # 404 is not found


@app.route("/report-closed/<int:cafe_id>", methods = ["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        target_cafe = db.session.query(Cafe).get(cafe_id)
        if target_cafe:
            db.session.delete(target_cafe)
            db.session.commit()
            return jsonify(response = {"Success": f"Successfully deleted cafe with id {cafe_id} from the database."}), 200
        else:
            return jsonify(response = {"Error": f"Sorry, we didn't find a cafe with id {cafe_id}."}), 404
    else:
        return jsonify(response = {"Error": f"Sorry, you're not allowed to do this. Please verify your API key."}), 403 

    


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
