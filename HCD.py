# import code; code.interact(local=dict(globals(), **locals()))
from flask import Flask, request
import shopify
from models import db
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'admin',
    'db': 'demo_hcd',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)
API_KEY = '65c703a61049d706fee3af82bf772df1'
PASSWORD = '131625b9f4ba96a751aac14ab990e071'

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == "POST":
        return 'This is demo post'
    else:
        shop_url = "https://%s:%s@honeycando-com.myshopify.com/admin" % (API_KEY, PASSWORD)
        shop = shopify.ShopifyResource.set_site(shop_url)
        product = shopify.Product.find()[0]
        product.title = 'Testing changed'
        product.save()
        return 'This is demo get'

db.init_app(app)

if __name__ == '__main__':
   app.run()

