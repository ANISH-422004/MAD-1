from flask import Flask , render_template


app = Flask(__name__)


@app.route('/' , methods = ['GET'] )
def home():
    return render_template('index.html')

@app.route('/dashboard' , methods = ['GET'] )
def dashboard():
    return render_template('dashboard.html')

@app.route("/random")
def random_child():
    return render_template('random child.html')


if __name__ == '__main__':
    app.run(debug=True)
    