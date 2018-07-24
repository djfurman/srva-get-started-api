from orator import Model
from database import db

Model.set_connection_resolver(db)

class Message(Model):
    __fillable__ =  [
        'name',
        'uuid',
        'email_address',
        'phone_number',
        'message',
    ]
