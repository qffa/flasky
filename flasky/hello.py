from flask import Flask, render_template, request
from flask.ext.script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    return '<h1>hello, %s!</h1> <p>your browser is %s</p>' %(name, user_agent)



if __name__ == '__main__':
#    app.run(debug = True)
    manager.run()


