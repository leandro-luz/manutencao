from flask_admin import Admin
from .. import db
from .controllers import CustomModelView, CustomView, CustomFileAdmin, PostView
from ..blog.models import Post, Comment, Tag
from ..auth.models import User, Role


admin = Admin()


def create_module(app, **kwargs):
    admin.init_app(app)
    admin.add_view(CustomView(name='Custom'))

    models = [User, Role, Comment, Tag]

    for model in models:
        admin.add_view(CustomModelView(model, db.session, category='Models'))

    admin.add_view(PostView(Post, db.session, category='Models'))
    # admin.add_view(CustomFileAdmin(app.static_folder, '/static/', name='Static Files'))
