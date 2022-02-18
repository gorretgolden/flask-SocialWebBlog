from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    content = db.Column(db.String(200))
    # date_created = db.Column(db.String, default=datetime.datetime.utcnow())


    def __init__(self,title,content):
        self.title = title
        self.content = content
        # self.date_created = date_created
 
 
 # creating all tables, put after the model

       
 
 #product schema
class PostSchema(ma.Schema):
    model = Post
    class Meta:
        fields = ("title","content","date_created")

#initialize the schema
posts_schema = PostSchema(many= True)  







