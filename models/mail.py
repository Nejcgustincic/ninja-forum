from google.appengine.ext import ndb

class Mail(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    subscribed = ndb.BooleanProperty(default=True)