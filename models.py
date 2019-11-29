import datetime
from environs import Env
from playhouse.sqlcipher_ext import SqlCipherDatabase, Model, CharField, \
    ForeignKeyField, DateTimeField

env = Env()
env.read_env()
db = SqlCipherDatabase('config.db', passphrase=env.SQLITE_ENCRYPTION_KEY)

class BaseModel(Model):
    class Meta:
        database = db

class Client(BaseModel):
    db_user = CharField()
    db_password = CharField()
    db_host = CharField()
    db_driver = CharField()
    db_host = CharField()

class Configuration(BaseModel):
    timestamp = DateTimeField(default=datetime.datetime.now)
    connection_info = ForeignKeyField(Client, backref='clients')
    application = CharField()
    environment = CharField()
