from peewee import *

user = 'root'
password = '1234'
db_name = 'phpin'

db = MySQLDatabase(
                   db_name, 
                   user=user,
                   password=password,
                   host='127.0.0.1', 
                   port=3306
                   )


class User(Model):
    id = CharField()
    login = CharField()
    passw = CharField(column_name='pass')

    class Meta:
        database = db
        db_table = "users"
        
        

class Note(Model):
    id = CharField()
    userId = ForeignKeyField(User, related_name='id')
    subject = CharField()

    class Meta:
        database = db
        db_table = "notes"

class Error():
    text = "er"