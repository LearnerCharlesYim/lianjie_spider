from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bcb4c11b6b4392de4d292a9c0691e2297c0173f0285d2cc9'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@localhost:3306/spider'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'

db = SQLAlchemy(app)
ckeditor = CKEditor(app)
login_manager = LoginManager()
login_manager.login_view = 'login'

login_manager.init_app(app)
from app import routes

from app.models import User
# db.drop_all()
db.create_all()


