import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

try:
    from config import DB_USERNAME, DB_PASSWORD, DB_ENDPOINT
except ImportError:
    config = None

app = Flask(__name__)
CORS(app)

is_prod = os.environ.get('DB_USERNAME', '')
api_version = 'v1.0'
api_base_url = os.environ.get(
    'API_BASE_URL', '') or 'http://localhost:5000/api/'

app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

if is_prod:
    app.debug = False
    username = os.environ.get('DB_USERNAME', '')
    password = os.environ.get('DB_PASSWORD', '')
    db_endpoint = os.environ.get('DB_ENDPOINT', '')
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{db_endpoint}/mental_health_tech_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/")
def home_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("index.html", data=data)


@app.route("/machine-learning")
def machine_learning_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("machine2.html", data=data)


@app.route("/form")
def form_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("predict.html", data=data)


@app.route("/data")
def data_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("data.html", data=data)


@app.route("/etl")
def etl_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("etl.html", data=data)


@app.route(f"/api/{api_version}/docs")
def api_docs():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("api.html", data=data)


if __name__ == "__main__":
    app.run()
