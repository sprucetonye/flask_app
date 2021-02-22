from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'


db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='NA')
    datetime_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
            return 'Blog post ' + str(str.id)
all_post = [
    {'title': 'post 1',
    'content': 'this is the content of post 1',
    'author': 'Tonye'
    },
    
    {
        'title': 'post 2',
        'content': 'this is the'
    }
]

@app.route('/home')

def hello():
    return "Welcome to Tonye's blog post"

@app.route('/post')
def post():
    return render_template('post.html', post=all_post)

@app.route('/onlyget', methods=['GET', 'POST'])
def get_req():
    return "you can only get"

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)