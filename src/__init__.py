import os
from flask import Flask, render_template
from flask_marshmallow import Marshmallow
from src.database import db
from src.routes.posts import post
from src.routes.auth import auth

#Application Factory Function
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
   

    if test_config is None:
        # load the instance config, if it exists, when not testing
       app.config.from_mapping(
        SECRET_KEY= os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DB_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
    app.register_blueprint(post)
    app.register_blueprint(auth)
   
    app.static_folder = 'static'
    db.app = app
    db.init_app(app)
    Marshmallow(app)

   
    
    # a simple page that says hello
    @app.route('/')
    def home_page(): 
        return render_template('base.html')
    
    @app.route('/about')
    def about_page(): 
        return render_template('about.html')
    
    @app.route('/contact')
    def contact_page(): 
        return render_template('contact.html')
    
    @app.route('/postpage')
    def posts_page(): 
        return render_template('posts.html')    
    
    return app

