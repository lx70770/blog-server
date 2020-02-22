from app import db
from app.models.user import User
from index import app

with app.app_context():
    with db.auto_commit():
        user = User()
        user.nickname = '_admin'
        user.email = '666@163.com'
        user.password = 'password'
        db.session.add(user)
