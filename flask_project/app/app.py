from flask import Flask

app = Flask(__name__)


@app.route('/')
def Hello_world():
    return '<h1>Hello world!</h1>'


@app.route('/welcome/<name>/<uid>/')
def welcome(name, uid):
    return 'Hello {} {}'.format(uid, name)


@app.route('/user/<int:uid>/')
def user(uid):
    return 'Hello {}'.format(uid)


@app.route('/path/<path:p>')
def path(p):
    return p


if __name__ == '__main__':
    app.run(debug=True)
