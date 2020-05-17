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
app.config['JSON_SORT_KEYS'] = False

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

Survey = Base.classes.survey_responses

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

@app.route(f"/api/{api_version}/surveys", methods=['GET'])
@cross_origin()
def surveys():
    session = Session(engine)

    surveys = session.query(
      Survey.id,
      Survey.year,
      Survey.number_employees,
      Survey.employer_provides_mental_health_benefits,
      Survey.employer_formally_discussed_mental_health,
      Survey.employer_mental_health_importance,
      Survey.sought_treatment_for_mental_health,
      Survey.mental_health_in_interview,
      Survey.employer_offers_resources,
      Survey.is_anonymity_protected_by_employer,
      Survey.level_difficulty_asking_for_leave,
      Survey.currently_has_mental_health_disorder,
      Survey.interferes_with_work_treated).limit(100)

    session.close()

    output = []

    for survey in surveys:
      survey_dict = {}
      output.append({
        "id": survey[0],
        "year": survey[1],
        "number_employees": survey[2],
        "employer_provides_mental_health_benefits": survey[3],
        "employer_formally_discussed_mental_health": survey[4],
        "employer_mental_health_importance": survey[5],
        "sought_treatment_for_mental_health": survey[6],
        "mental_health_in_interview": survey[7],
        "employer_offers_resources": survey[8],
        "is_anonymity_protected_by_employer": survey[9],
        "level_difficulty_asking_for_leave": survey[10],
        "currently_has_mental_health_disorder": survey[11],
        "interferes_with_work_treated": survey[12]
      })

    return jsonify({ 'result': output })


if __name__ == "__main__":
    app.run()
