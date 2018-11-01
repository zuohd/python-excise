from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    con = sqlite3.connect("soderberg_blog")
    rows = con.cursor().execute("select id,title from myblogs")
    blogs = []
    for row in rows:
        blog = {}
        blog['id'] = row[0]
        blog['title'] = row[1]
        blogs.append(blog)
    return render_template('index.html', blogs=blogs)


@app.route('/add_blog/', methods=['get', 'post'])
def add_blog():
    if request.method == 'GET':
        return render_template('add_blog.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        sql = "insert into myblogs values(null,'{}','{}')".format(title, content)
        con = sqlite3.connect("soderberg_blog")
        con.cursor().execute(sql)
        con.commit()
        con.close()
        return redirect("/")


@app.route('/blog_detail/')
def blog_detail():
    blogid=request.args.get('id',0)
    con = sqlite3.connect("soderberg_blog")
    row = con.cursor().execute("select title,content from myblogs where id={}".format(blogid)).fetchone()
    blog={}
    blog['title']=row[0]
    blog['content']=row[1]
    print(blog)
    return render_template('blog_detail.html',blog=blog)


if __name__ == '__main__':
    app.run(debug=True)
