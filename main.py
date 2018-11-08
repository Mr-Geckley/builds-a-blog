from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://builds-a-blog:buildsablog@localhost:8889/builds-a-blog'
app.config['SQLALCHEMY_ECHO']=True
db = SQLAlchemy(app)

class Title(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name



@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        title_name = request.form['title']
        new_title = Title(title_name)
        db.session.add(new_title)
        db.session.commit()

    titles = Title.query.all()
    return render_template('main.html', title="BUILD-A-BLOG", titles=titles)

if __name__ == '__main__':
    app.run()