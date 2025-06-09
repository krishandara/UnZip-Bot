import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", 27536109))
    API_HASH = os.environ.get("API_HASH", "b84d7d4dfa33904d36b85e1ead16bd63")
    MAX_FILE_SIZE = 2194304000
    
    
