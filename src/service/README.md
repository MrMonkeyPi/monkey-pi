

## Installation
```sh
python3 -m venv venv
. venv/bin/activate

# pip install flask
# pip install requests
# pip3 freeze > requirements.txt
pip install -r requirements.txt 

```

### Run

```sh

export MEDIA_HOME=/some/media/root1/:/some/media/root2/ && python3 setup.py

python3 app.py

```

### Watchtower

Watch git and pull latest code then restart server

```sh

export home="/data/app"

echo "*/5 * * * * python3 ${home}/src/service/watchtower.py" | sudo crontab -

```