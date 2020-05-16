import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
    db_username = os.environ.get('DB_USERNAME', '')
    db_password = os.environ.get('DB_PASSWORD', '')
    db_endpoint = os.environ.get('DB_ENDPOINT', '')
else:
    app.debug = True
    db_username = DB_USERNAME
    db_password = DB_PASSWORD
    db_endpoint = DB_ENDPOINT

rds_connection_string = f"{db_username}:{db_password}@{db_endpoint}:5432/mental_health_tech_db"
engine = create_engine(f'postgresql://{rds_connection_string}')

Base = automap_base()
Base.prepare(engine, reflect=True)

survey_responses = Base.classes.survey_responses
print(Base.classes.keys())


@app.route("/")
def home_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("landing.html", data=data)

@app.route("/team")
def team_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("team.html", data=data)


@app.route("/overview")
def overview_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("index.html", data=data)


@app.route("/machine-learning")
def machine_learning_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("machine2.html", data=data)


@app.route("/predict")
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

@app.route(f"/api")
def api_docs():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("api.html", data=data)

@app.route(f"/nlp")
def nlp_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("nlp.html", data=data)

@app.route(f"/visualizations")
def visualizations_page():
    data = {'api_base_url': f'{api_base_url}{api_version}'}
    return render_template("visualizations.html", data=data)


if __name__ == "__main__":
    app.run()
