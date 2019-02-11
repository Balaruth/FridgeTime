from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e64498bd6adeb194264c388d1aa84a46'

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
