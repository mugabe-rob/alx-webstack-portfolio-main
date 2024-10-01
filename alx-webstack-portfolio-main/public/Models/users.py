from mongoengine import Document, StringField, BooleanField, DateTimeField
from datetime import datetime
from uuid import uuid4
class User(Document):
    _id=StringField(default=lambda: str(uuid4()),primary_key=True)
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    created_at = DateTimeField(defaul=datetime.now())
    status = StringField(default='INACTIVE')
