import os
from flask_admin import Admin
from .models import db, User, CycleData, DailyLog, RelationshipLog
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    admin = Admin(app, name="NexaFemme")

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(CycleData, db.session))
    admin.add_view(ModelView(DailyLog, db.session))
    admin.add_view(ModelView(RelationshipLog, db.session))
