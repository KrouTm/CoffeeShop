from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from sqlalchemy import table, column
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import table, column

app = Flask(__name__)

ENV = 'prod'

if ENV =='dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hulck1@localhost/Reservation'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fmcqaikodisqta:897ac9071a746f941115952debb2b122d7d2058f63090509b197541ed2e49ec8@ec2-3-229-11-55.compute-1.amazonaws.com:5432/dfg2oaannn6r70'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Reservation(db.Model):
    __tablename__='reservation'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(200))
    time = db.Column(db.String(200))
    name = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    nperson = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, date, time, name, lastname, email, phone, nperson, comments):
        self.date = date
        self.time = time
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.nperson = nperson
        self.comments = comments

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/script')
def script():
    return render_template('script.js')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        nperson = request.form['nperson']
        comments = request.form['comments']
        print(date, time, name, lastname, email, phone, nperson, comments)
        data = Reservation(date, time, name, lastname, email, phone, nperson, comments)
        db.session.add(data)
        db.session.commit()
        send_mail(date, time, name, lastname, email, phone, nperson, comments)
        return render_template('success.html')

if __name__ == '__main__':
    app.run()