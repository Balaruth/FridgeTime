from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e64498bd6adeb194264c388d1aa84a46'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship('Recipe', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(30), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # table name in lower case
    ingredients = db.relationship('Ingredient', backref='recipe', lazy=True)

    def __repr__(self):
        return f"Recipe('{self.recipe_name}', '{self.ingredients}')"


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(30))
    quantity = db.Column(db.Integer)
    type = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))


    def __repr__(self):
        return f"Recipe('{self.ingredient_name}', '{self.quantity}', '{self.type}')"


testdata = [
    {
        'user': 'Grant Donoghue',
        'recipename': 'Omelette',
        'ingredients': '3 Eggs'
    }
]


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', testdata=testdata)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()  # passed from forms.py
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)  # passed from form variable


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You have been logged in!', 'success')
        return redirect(url_for('index'))
    else:
        flash(f'Login unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
