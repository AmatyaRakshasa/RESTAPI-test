import os
from flask import Flask, request
from flask_restful import Api
from db import db


from flask_jwt import JWT
from Resources.user import UserRegister
from security import authenticate, identity
from Resources.item import Item, ItemList
from Resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'anshu'
api = Api(app)




jwt = JWT(app, authenticate, identity) #/auth



api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
