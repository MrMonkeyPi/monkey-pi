# for local execution

rm -r ../dist

cd ../ui
npm i && npm run build

cd ../service

. venv/bin/activate
export MEDIA_HOME=/media/srepond/Projects/MonkeyPi/Audio/:/some/other/path && python3 setup.py
python3 app.py