from tinydb import TinyDB, Query
from os.path import exists
import json

db = TinyDB('db.json')

def update(text):
    if text == 'like':
        db.update({'like': str(int(db.all()[0]['like']) + 1)}, Query().like.exists())
    elif text == 'dislike':
        db.update({'dislike': str(int(db.all()[0]['dislike']) + 1)}, Query().dislike.exists())

def init():
    if len(db.all()) == 0:
        db.insert({'like': 0, 'dislike': 0})
    else:
        db.all()[0]['like'] = 0
        db.all()[0]['dislike'] = 0

def get():
    return json.dumps(db.all()[0])

# def create_db():
#     is_exists = exists('db.json')
#     if is_exists is False:
#         db = TinyDB('db.json')
#     else:
#         db = TinyDB('db.json')