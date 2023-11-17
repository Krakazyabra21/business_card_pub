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
        print(name, phone, email)

        from website.bd_commands import hrs
        new_HR = hrs(name= name, phone= phone, email=email)
        print(new_HR)
        db.session.add(new_HR)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("GG")
        print("New HR!")

        result = db.session.query(hrs.id, hrs.name, hrs.phone, hrs.email).all()
        print(result)




        return redirect(url_for('views.home'))
        # return render_template("index.html")

    return render_template("index.html")

@views.route("/json", methods= ['GET'])
def json():
    from website.bd_commands import hrs
    result = db.session.query(hrs.id, hrs.name, hrs.phone, hrs.email).all()
    return f"<h1>{result}<h1>"