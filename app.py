from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_wtf.csrf import CSRFProtect
from flask_heroku import Heroku
app = Flask( __name__ )
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    birthday = db.Column(db.String())

@app.route("/Success", methods=["POST"])
def post_to_db():
    dbdata = User(request.form['name'], request.form['email'], request.form['birthday'])
    db.session.add(dbdata)
    db.session.commit()
    return('Success!  We\'re searching for your twin now')

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    #app.debug = True
    app.run()

