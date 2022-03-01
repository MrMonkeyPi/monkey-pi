import os
import shelve

APP_SETTING_FILE =  os.path.join(os.getcwd(), 'instance', "data", "app")
CACHE_DIR = os.path.join(os.getcwd(), 'instance', 'cache')

try:
    os.makedirs(CACHE_DIR)
    os.makedirs(os.path.dirname(APP_SETTING_FILE))
except OSError:
    pass

# for item, value in os.environ.items():
#     print(f"{item} > {value}")

MEDIA_HOME = os.environ.get('MEDIA_HOME')
if MEDIA_HOME is not None: 
    with shelve.open(APP_SETTING_FILE) as db:
        db['MEDIA_HOME'] = list(map(lambda x: os.path.abspath(x), MEDIA_HOME.split(':'))) 

with shelve.open(APP_SETTING_FILE) as db:
    print(dict(db))

