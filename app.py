from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(10), nullable=False)
    is_available = db.Column(db.Boolean, default=True)

@app.route("/")
def index():
    seats = Seat.query.all()
    return render_template("seats.html", seats=seats, event_name="Live Concert")

@app.route("/api/seats")
def get_seats():
    seats = Seat.query.all()
    for seat in seats:
        seat.is_available = random.choice([True, False])
    db.session.commit()
    data = [{"id": s.id, "seat_number": s.seat_number, "is_available": s.is_available} for s in seats]
    return jsonify(data)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if Seat.query.count() == 0:
            for i in range(1, 21):
                db.session.add(Seat(seat_number=f"S{i:02}"))
            db.session.commit()
    app.run(debug=True)