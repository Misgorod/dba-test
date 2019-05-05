from v1 import api as api_v1
from flask import Flask

app = Flask(__name__)
app.register_blueprint(api_v1, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(host='0.0.0.0')