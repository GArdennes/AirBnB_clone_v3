#!/usr/bin/python3
"""Contains a Flask web application API"""
import os 
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
"""Flask web application instance"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_flask(exception):
    """Flask app context end event listener."""
    storage.close()


if __name__ == '__main__':
    app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(
            host=app_host,
            port=app_port,
            threaded=True
            )