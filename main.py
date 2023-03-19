from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

class Data(db.Model):
    name = db.Column(db.String, primary_key=True)
    r_no = db.Column(db.String(10), primary_key=True)
    email = db.Column(db.String, primary_key=True)
    phone = db.Column(db.String(10), primary_key=True)
    branch = db.Column(db.String, primary_key=True)
    section = db.Column(db.String, primary_key=True)
    gender = db.Column(db.String, primary_key=True)
    address = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, primary_key=True)

    def __repr__(self) -> str:
        return '<Student> %r' % self.r_no

@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



