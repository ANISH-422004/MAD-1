from flask import Flask, render_template

app = Flask(__name__)

itemlist = [
{'value': '0', 'content': 'zero'},
{'value': '1', 'content': 'one'},
{'value': '2', 'content': 'two'},
{'value': '3', 'content': 'three'},
]

@app.route('/')
def func(): 
    return render_template('doc.html', itemlist = itemlist)

app.run() #<option value="field value">content value</option>

