
# for local execution

cd ../ui
npm i && npm run build

cd ../service

. venv/bin/activate
export MEDIA_HOME=/some/media/root1/:/some/media/root2/ && IN_LOCAL=TRUE && python3 setup.py
python3 app.py