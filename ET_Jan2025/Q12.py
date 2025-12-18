from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/hello')
def hello():
 return 'Hello World!'

@app.route('/user/<username>')
def user(username):
 return f'Welcome {username}!'

@app.route('/')
def base():
  return(redirect(url_for('hello', username='John')))

with app.test_request_context(): # url_for('hello') -> /hello 
    # url_for('user', username="parameter") -> /user/parameter url_for(function name) -> corresponding route
# == print statement == #
     #?id=101
    app.run()