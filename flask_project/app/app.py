from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    # return request.method
    uid = request.args.get('uid', 'none')
    age = request.args.get('age', 0)
    return "uid:{},age:{}".format(uid, age)


@app.route('/login/', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # return "username:{}<br/> password:{}".format(request.form.get('username'), request.form.get('password'))
        return redirect(url_for('Hello_world'))

@app.route('/hello/')
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


@app.route('/profile/')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
