import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_cors import CORS, cross_origin

try
    from config import DB_USERNAME, DB_PASSWORD, DB_ENDPOINT
except ImportError:
    config = None

app = Flask(__name__)
CORS(app)

# Constants
is_prod = os.environ.get('DB_USERNAME', '')
api_version = 'v1.0'
api_base_url = os.environ.get('API_BASE_URL', '') or 'http://localhost:5000/api/'

# Cors
app.config['CORS_HEADERS'] = 'Content-Type'

# No more page caching/need to hard refresh.
# Still need to soft refresh the page though when making changes to static files...
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# If this app is on production/deployed.
if is_prod:
  app.debug = False
  username = os.environ.get('DB_USERNAME', '')
  password = os.environ.get('DB_PASSWORD', '')
  db_endpoint = os.environ.get('DB_ENDPOINT', '')

# else if you are running the app locally.
else:
  app.debug = True

mongo = PyMongo(app)


@app.route("/")
def home_page():
  data = {'api_base_url': f'{api_base_url}{api_version}'}
  return render_template("index.html", data=data)

@app.route("/machine-learning")
def charts_page():
  data = {'api_base_url': f'{api_base_url}{api_version}', 'API_KEY': map_api_key }
  return render_template("charts.html", data=data)

@app.route("/form")
def form_page():
  data = {'api_base_url': f'{api_base_url}{api_version}' }
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
    data = {'api_base_url': f'{api_base_url}{api_version}' }
    return render_template("api.html", data=data)

if __name__ == "__main__":
    app.run()