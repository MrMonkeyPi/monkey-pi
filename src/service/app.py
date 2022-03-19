from flask import Flask

from routers import status, setting, walk 

app = Flask(__name__,
            static_url_path='/', 
            static_folder='../dist',
            instance_relative_config=True)

app.register_blueprint(status.bp, url_prefix= "/api/status")
app.register_blueprint(setting.bp, url_prefix= "/api/setting")
app.register_blueprint(walk.bp, url_prefix= "/api/walk")

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 2323)