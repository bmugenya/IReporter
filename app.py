from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


users = []
title = []
issue = []
location = []
comment = []


@app.route("/")
def index():
    return render_template('index.html', users=users)


@app.route("/profile", methods=['GET', 'POST'])
def profile():

    if request.method == 'GET':
        return render_template('profile.html', users=users)
    else:
        f_name = request.form.get('f_name')
        # l_name = request.form.get('l_name')
        # email = request.form.get('email')
        # password = request.form.get('password')
        # data = {
        #     'f_name': f_name,
        #     'l_name': l_name,
        #     'email': email,
        #     'paassword': password
        # }

        users.append(f_name)

        return render_template('profile.html', users=users)


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html', users=users)
    else:
        utitle = request.form.get('title')
        uissue = request.form.get('type')
        ulocation = request.form.get('location')
        ucomment = request.form.get('comment')

        date = datetime.datetime.now()
        posted = ("%d - %d - %d") % (date.year, date.month, date.day)
        title.append(utitle)
        issue.append(uissue)
        location.append(ulocation)
        comment.append(ucomment)

        return render_template('admin.html', users=users, title=title, issue=issue, location=location, posted=posted, comment=comment)


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():

    return render_template('register.html',)


if __name__ == '__main__':
    app.run(debug=True)
