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
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
from flask_swagger_ui import get_swaggerui_blueprint
from textblob import TextBlob
import pickle
import pandas as pd
import numpy as np


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

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return score

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

@app.route(f"/api/docs")
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

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
  SWAGGER_URL,
  API_URL,
  config={
    'app_name': 'Mental Health in Tech API'
  }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

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

@app.route('/nlp', methods=['POST'])
@cross_origin()
def submit():
  if request.method == 'POST':
    comments = request.form['comments']
    if comments == '':
      return render_template(
        'nlp.html',
        message='Need to enter at least one word to perform sentiment analysis.',
        data = {'api_base_url': f'{api_base_url}{api_version}'}
      )

    sentiment_type = request.form['library']

    if sentiment_type == 'vader':
      vader_score = sentiment_analyzer_scores(comments)
      return render_template(
        'nlp.html',
        data = {'api_base_url': f'{api_base_url}{api_version}'},
        vader_score = vader_score,
        textblob_score = None
        )

    else:
      blob = TextBlob(comments)
      textblob_score = blob.sentiment[0]
      return render_template(
        'nlp.html',
        data = {'api_base_url': f'{api_base_url}{api_version}'},
        textblob_score = textblob_score,
        vader_score = None
        )


@app.route(f"/api/{api_version}/sentiment_scores", methods=['GET'])
@cross_origin()
def sentiment_scores():
  session = Session(engine)

  surveys = session.query(Survey.id, Survey.year, Survey.conversation_with_employer).all()

  session.close()

  ids = []
  years = []
  conversations = []

  for survey in surveys:
    if survey[2] != None:
      ids.append(survey[0])
      years.append(survey[1])
      conversations.append(survey[2])
  
  output = []

  number_conversations = len(conversations)
  number_positive_vader = 0
  number_neutral_vader = 0
  number_negative_vader = 0
  number_positive_textblob = 0
  number_negative_textblob = 0
  number_neutral_textblob = 0

  for index, conversation in enumerate(conversations):
    positive_score = sentiment_analyzer_scores(conversation)["pos"]
    negative_score = sentiment_analyzer_scores(conversation)["neg"]
    neutral_score = sentiment_analyzer_scores(conversation)["neu"]
    compound_score = sentiment_analyzer_scores(conversation)["compound"]
    blob = TextBlob(conversation)
    textblob_score = blob.sentiment[0]

    if compound_score >= 0.05:
      conversation_class_vader = 'positive'
      number_positive_vader += 1

    if compound_score <= -0.05:
      conversation_class_vader = 'negative'
      number_negative_vader += 1
    
    if compound_score < 0.05 and compound_score > -0.05:
      conversation_class_vader = 'neutral'
      number_neutral_vader += 1

    if textblob_score < 0:
      conversation_class_textblob = 'negative'
      number_negative_textblob += 1

    if textblob_score == 0:
      conversation_class_textblob = 'neutral'
      number_neutral_textblob += 1

    if textblob_score > 0:
      conversation_class_textblob = 'positive'
      number_positive_textblob += 1

    survey_dict = {}
    output.append({
      "id": ids[index],
      "conversation": conversation,
      "conversation_class_vader": conversation_class_vader,
      "conversation_class_textblob": conversation_class_textblob,
    })
  
  return jsonify({ 'result': output,
      "number_positive_vader": number_positive_vader,
      "number_neutral_vader": number_neutral_vader,
      "number_negative_vader": number_negative_vader,
      "number_positive_textblob": number_positive_textblob,
      "number_neutral_textblob": number_neutral_textblob,
      "number_negative_textblob": number_negative_textblob })


model_file = "model/ml_model.pkl"
with open(model_file, 'rb') as file:
  model = pickle.load(file)


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
  
  if request.method == 'POST':
    input_company = request.form['company']
    input_employees = request.form['employees']
    input_benefits = request.form['benefits']
    input_resources = request.form['resources']
    input_discussion = request.form['discussion']
    input_anonymity = request.form['anonymity']
    input_supporitve = request.form['supportive']
    
    if ((input_company=='') or (input_employees=='') or (input_benefits=='') or (input_resources=='') or (input_discussion=='') or (input_anonymity=='') or (input_supporitve=='')):
      return render_template(
        'predict.html',
        form_message='Please answer the questions to run machine learning model',
        data = {'api_base_url': f'{api_base_url}{api_version}'}
      )

    if input_company == 'True':
      resp_company = 1
    elif input_company == "False":
      resp_company = 0
    else:
      resp_company = []
    
    if input_employees == "1 to 5":
      resp_employees = [0, 0, 0, 0, 0]
    elif input_employees == "6 to 25":
      resp_employees = [0, 0, 0, 1, 0]
    elif input_employees == "26 to 100":
      resp_employees = [0, 1, 0, 0, 0]
    elif input_employees == "100 to 500":
      resp_employees = [1, 0, 0, 0, 0]
    elif input_employees == "500 to 1000":
      resp_employees = [0, 0, 1, 0, 0]
    elif input_employees == "More than 1000":
      resp_employees = [0, 0, 0, 0, 1]
    else:
      resp_employees = []
    
    if input_benefits == "Yes":
      resp_benefits = [0, 0, 1]
    elif input_benefits == "No":
      resp_benefits = [1, 0, 0]
    elif input_benefits == "I'm not elibile for coverage/NA":
      resp_benefits = [0, 1, 0]
    elif input_benefits == "I don't know":
      resp_benefits = [0, 0, 0]
    else: 
      resp_benefits = []
    
    if input_resources =="Yes":
      resp_resources = [0, 1]
    elif input_resources == "No":
      resp_resources = [1, 0]
    elif input_resources == "I don't know":
      resp_resources = [0, 0]
    else:
      resp_resources = []
    
    if input_discussion =="Yes":
      resp_discussion = [0, 1]
    elif input_discussion == "No":
      resp_discussion = [1, 0]
    elif input_discussion == "I don't know":
      resp_discussion = [0, 0]
    else:
      resp_discussion = []
    
    if input_anonymity =="Yes":
      resp_anonymity = [0, 1]
    elif input_anonymity == "No":
      resp_anonymity = [1, 0]
    elif input_anonymity == "I don't know":
      resp_anonymity = [0, 0]
    else:
      resp_anonymity = []
    
    if input_supporitve =="I've always been self-employed":
      resp_supportive = [0, 0, 0, 0]
    elif input_supporitve == "No":
      resp_supportive = [0, 1, 0, 0]
    elif input_supporitve == "Maybe/Not Sure":
      resp_supportive = [1, 0, 0, 0]
    elif input_supporitve == "Yes, I observed":
      resp_supportive = [0, 0, 0, 1]
    elif input_supporitve == "Yes, I experienced":
      resp_supportive = [0, 0, 1, 0]
    else:
      resp_supportive = []
    
    user_input = np.concatenate(([resp_company], resp_employees[:], resp_benefits[:], resp_resources[:], resp_discussion[:], resp_anonymity[:], resp_supportive[:]))

    
    
    prediction = model.predict([user_input])
  
    return render_template(
        'predict.html',
        data = {'api_base_url': f'{api_base_url}{api_version}'},
        user_predict = prediction,
        user_company = input_company,
        user_employees = input_employees,
        user_benefits = input_benefits,
        user_resources = input_resources,
        user_discussion = input_discussion,
        user_anonymity = input_anonymity,
        user_supportive = input_supporitve
        )

if __name__ == "__main__":
    app.run()
