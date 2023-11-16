from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from . import db
views = Blueprint('views', __name__)

@views.route("/", methods= ['GET','POST'])
def home():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        from website.bd_commands import HRs
        new_HR = HRs(name= name, phone= phone, email=email)
        db.session.add(new_HR)
        db.session.commit()
        print("New HR!")

        result = db.session.query(HRs.id, HRs.name).all()
        # print(db.session.query(HRs).all())



        return redirect(url_for('views.home'))
        # return render_template("index.html")

    return render_template("index.html")


@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)


@views.route("/json")
def get_json():
    return jsonify({'name': 'xdd', 'coolness': 10})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))


