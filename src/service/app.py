from flask import Flask

from routers import status, setting, robot

app = Flask(__name__,
            static_url_path='/', 
            static_folder='../dist',
            instance_relative_config=True)

app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

app.register_blueprint(status.bp, url_prefix= "/api/status")
app.register_blueprint(setting.bp, url_prefix= "/api/setting")
app.register_blueprint(robot.bp, url_prefix= "/api/robot")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    if path is not None:
        return app.send_static_file(path)

    return app.send_static_file('index.html')

@app.errorhandler(404)   
def not_found(e):   
  return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 2323)