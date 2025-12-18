from flask import Flask , render_template, request , requset 
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import matplotlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


@app.route('/' , methods=['GET', 'POST'])
def home():
    if(request.method == "GET") :
        return render_template('index.html')    

    

if __name__ == '__main__':
    app.run(debug=True) 