from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from main import db

views = Blueprint(__name__, "views/")

@views.route("/", methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')

        from bd_commands import HRs
        new_HR = HRs(name= name, phone= phone, email=email)
        db.session.add(new_HR)
        db.session.commit()

        # return redirect(url_for('/'))
        return render_template("index.html")

    return render_template("index.html",name= "xdd")


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


