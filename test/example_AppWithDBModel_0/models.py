from google.appengine.ext import ndb

class User(ndb.Model):

    username = ndb.Stringproperty()
    password = ndb.Stringproperty()