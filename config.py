import os

class Config(object):
    SECRET_KeY = os.environ.get('SECRET_KEY') or 'This_is_a_secret'