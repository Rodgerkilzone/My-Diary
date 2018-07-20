
import os

class Config():

    DEBUG = False

class Development(Config):
   
    DEBUG = True

class Testing(Config):

    DEBUG = True

class Production(Config):
   
    DEBUG = False

app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
    }