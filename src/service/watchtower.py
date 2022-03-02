import os
import time
import requests as req

home_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../'))
print('[Watchtower] home dir: ' + home_dir)

print('[Watchtower] Stopping... Monkey Pi server')
try:
    req.get('http://127.0.01:2323/api/status/shutdown')
    time.sleep(1.1)
    print('[Watchtower] Stopped Monkey Pi server')
except:
    print('[Watchtower] Monkey Pi server is not running')
    pass



print('[Watchtower] pulling latest codes')
# cmd = 'ls -alh ' + home_dir
cmd = ' '.join(['cd', home_dir, '&& git pull'])
print('[Watchtower] ' + cmd)
print('[Watchtower] ------------------------')
os.system(cmd)
print('[Watchtower] ------------------------')

cmd = ' '.join(['cd', os.path.join(home_dir, 'src/service'), '&& python3 app.py '])
print('[Watchtower] Starting Monkey Pi Server')
print('[Watchtower] ' + cmd)
os.system(cmd)
