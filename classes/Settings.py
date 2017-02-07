import json

class Settings(object):
    """This class represents the settings"""
    def __init__(self):
        self.settings = json.load(open('settings.json'))
        
