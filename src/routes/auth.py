from flask import Blueprint, jsonify, make_response, render_template, request
from src.database import Post, PostSchema
from src.database import db

auth = Blueprint('auth',__name__,url_prefix='/api/auth')


@auth.route('/posts/create', methods=["POST"])
def create_post():
    data = request.get_json()
    title = request.json['title']
    content = request.json['content'] 
    # date_created = request.json['date_created']      
    
    #instatiating a new product
    new_post = Post(title=title,content=content)

    #add the new product to the db
    db.session.add(new_post)
    db.session.commit()
    posts_schema = PostSchema()
    post = posts_schema.load(data)
    result = posts_schema.dump(post)
    
    return render_template('create_post.html')

#getting the posts
@auth.route('/posts', methods=["GET"])
def get_posts():
 all_posts = Post.query.all()
 posts_schema = PostSchema()
 result = posts_schema.dump(all_posts)
 return jsonify({"posts":result})

@auth.route('/posts/<id>', methods=["GET"])
def get_post(id):
#getting the products
 single_post = Post.query.get(id)
 schema = PostSchema(many=True)
 new = schema.dump(single_post)
 return make_response(jsonify({"product":new}))
    

#getting a single post    
@auth.route('/posts/<id>', methods=["DELETE"])
def delete_post(id):
#getting the posts
 deleted_post = Post.query.get(id)
 db.session.delete(deleted_post)
 db.session.commit()
 return make_response("Item deleted sucessfully",204)


@auth.route('/login')
def login():
    return render_template('login.html') 

