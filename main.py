from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite3.db"
app.config['SECRET_KEY'] = 'husia888'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))




@app.route('/')
def index():
    employees = User.query.all()
    return render_template('index.html', employees=employees)


@app.route('/delete/<int:id>')
def delete(id):
    res = User.query.get(id)
    db.session.delete(res)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    if request.method == 'POST':
        res = request.form.to_dict()
        update_user = User.query.get(id)
        update_user.name = res['name']
        update_user.email = res['email']
        update_user.phone = res['phone']
        db.session.add(update_user)
        db.session.commit()
        employees = User.query.all()
    return render_template('index.html', employees=employees)


@app.route('/add', methods=['POST', 'GET'])
def add():
    res = request.form.to_dict()
    update_user = User( name = res['name'],
                        email = res['email'],
                        phone = res['phone'])
    db.session.add(update_user)
    db.session.commit()
    employees = User.query.all()
    return render_template('index.html', employees=employees)


if __name__ == '__main__':
    app.run(debug=True)
