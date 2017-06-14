from google.appengine.ext import ndb

class Vehicles(ndb.Model):
    brand = ndb.StringProperty()
    model = ndb.StringProperty()
    price = ndb.StringProperty()
    ps = ndb.StringProperty()

