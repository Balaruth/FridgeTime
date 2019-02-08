from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
