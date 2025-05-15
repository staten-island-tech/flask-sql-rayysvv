from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 📌 Tell Flask where the database file will be stored
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 📌 Create the database object
db = SQLAlchemy(app)

# 🎬 Sample movie data
movies = [
    {"id": 1, "title": "Avengers: Endgame", "price": 12},
    {"id": 2, "title": "Spider-Man: No Way Home", "price": 10},
    {"id": 3, "title": "Inception", "price": 8}
]

# 📌 Define the Booking Model (Table)
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each booking
    name = db.Column(db.String(100), nullable=False)  # User's name
    movie_title = db.Column(db.String(100), nullable=False)  # Movie booked
    seats = db.Column(db.Integer, nullable=False)  # Number of seats booked

# 📌 Create the database table
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html', movies=movies)