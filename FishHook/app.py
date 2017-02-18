from server import app
from setting import port

class FishHook(object):
    def __init__(self, **keywords):
        self.secret = keywords['secret']
        app.run(host=keywords['host'], port=keywords['port'])