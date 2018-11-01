from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_blog/')
def add_blog():
    return render_template('add_blog.html')


@app.route('/blog_detail/')
def blog_detail():
    return render_template('blog_detail.html')


if __name__ == '__main__':
    app.run(debug=True)
