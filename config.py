import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\x18\x88\x7f8>P\xb6\x94a=}\xfe6\xaayo'

    MONGO_SETTINGS = { 'db' : 'UTA_Enrollment', 'host': 'mongodb://localhost:27017/UTA_Enrollment' }