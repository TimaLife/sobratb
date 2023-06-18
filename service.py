import peewee
from model import *

def connect():
    try:
        db.connect()
    except peewee.InternalError as px:
        print(str(px))

def close():
    db.close

def getAdmin():
    return User.select().where(User.login == 'admin').get()

def getUser(name, passw):
    try:
        user = User.select().where(User.login == name).get()
    except:
        er = Error()
        er.text = "identific"
        return er
    if user.passw == passw:
        return user
    else: 
        er = Error()
        er.text = "authintific"
        return er
