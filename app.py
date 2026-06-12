from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "app.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

db = SQLAlchemy(app)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    public = db.Column(db.Boolean, default=False)
    code = db.Column(db.String(6), nullable=True)
    members = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Room {self.id}: {self.name}>"

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/product')
def productPage():
    return render_template('product.html')

if __name__ == "__main__":
    app.run(debug=True)