# Mental Health in Tech and Machine Learning

Using data and machine learning to analyze and improve mental health conversations in the tech community.

## Table of contents

* [Mental Health in Tech App](#app)
* [Background](#background)
* [Technologies Used](#technologies_used)
* [Getting Started](#getting_started)
* [Database Schema](#database_schema)
* [API](#api)
* [Starting the Flask App](#flask)
* [Using the pgAdmin app to view and query the database locally](#pgadmin)
* [Deploying the app](#deployment)
* [Issues](#Issues)

## <a name="app"></a>Mental Health in Tech App

The results of this project are published at the following URL: <https://mental-health-in-tech.herokuapp.com/>.

## <a name="background"></a>Background

This project looks at different maching learning classification models and compares their ability/accuracy to classify whether or not an employee in the tech community is willing to seek treatment for a mental health condition. The data used for this project comes from the [OSMI (Open Sourcing Mental Illness) Mental Health in Tech Survey](https://osmihelp.org/research), which is an annual survey that captures employees' attitudes and opinions about how mental health is talked about and handled in the workplace in the tech industry. The target question from this survey that this project analyzes is "Have you ever sought treatment for a mental health disorder from a mental health professional?" Along with analyzing whether or not an employee would seek treatment, this project also uses natural language processing and sentiment analysis to build a model used to analyze mental health conversations employees have with their employers and then classify those conversations as either positive or negative.

## <a name="technologies_used"></a> Technologies Used

* AWS S3
* AWS RDS
* Postgres
* Python
* Google Colab
* Pandas
* PySpark
* Flask
* Swagger
* HTML/CSS
* Heroku

## <a name="getting_started"></a>Getting Started

The following section will take you through the steps of setting up this project and getting it running locally on your computer.

If you don't want to set up this project locally and just want to see the deployed app, go to <https://mental-health-in-tech.herokuapp.com/>.

1. [Clone the repository](#clone-repository)
2. [Set up AWS and Google Drive](#aws_setup)
3. [Load csv files from S3 bucket into Pandas dataframes to perform ETL](#cloud_etl)
4. [Create schema and tables](#create_schema)

###  <a name="clone-repository"></a> 1. Clone the repository
The first step is to clone the project repository to a local directory on your computer.

### <a name="aws_setup"></a> 2. Set up AWS and Google Drive

This project uses AWS to store the data files in a S3 bucket and uses Google Colab notebooks to extract, transform, load, and analyze that data.

To set up AWS and Google Drive for this project, run through the cells in the [cloud_setup.ipynb](./cloud_setup.ipynb) notebook.

### <a name="cloud_etl"></a> 3. Load csv files from S3 bucket into Pandas dataframes to perform ETL

After setting up AWS and Google Drive, run through the cells in the [cloud_etl.ipynb](./cloud_etl.ipynb) notebook to load the csv files from the S3 bucket into Pandas dataframes to extract, transform, and eventually load the data into a Postgres database.

### <a name="create_schema"></a> 4. Create schema and tables

Run through the cells in the [schema.ipynb](./schema.ipynb) file to create the schema for the database tables and connect to the database to verify that the tables were created.

## <a name="database_schema"></a>Database Schema

This project uses a SQL database hosted on AWS using AWS' Relational Database Service (RDS) to store the mental health survey results. For more information about the database structure used for this project, see [Database Structure](./docs/database.md).

## <a name="api"></a>API

The data used for this project is stored in a Postgres database that is hosted on AWS using AWS' Relational Database Service (RDS).

To access the survey responses from the database, we built a simple API using Flask.

The API documentation is available in a swagger app. [Start here](https://mental-health-in-tech.herokuapp.com/swagger/) for a basic reference on how to use the endpoints available to query the database for the data you need.

## <a name="flask"></a>Starting the Flask App

The API and frontend for this project are built using flask. To start the flask application locally:

1. Change directory to the **application** folder in this repository.
2. In the **application** folder, create a file called **config.py** that includes the following contents:

```bash
DB_USERNAME = 'username'
DB_PASSWORD = 'password'
DB_ENDPOINT = 'endpoint'
```

Replace username, password, and endpoint with their actual values.

3. Run the following command to start the flask server on port 5000.

```bash
python app.py
```

4. Navigate to <http://localhost:5000> in Chrome (or whatever browser you prefer) to view the app.

## <a name="pgadmin"></a>Using the pgAdmin app to view and query the database locally

This project uses a Postgres database hosted on AWS RDS to store the data. If you have the pgAdmin app, you can view and query the database.

To connect to the database using pgAdmin:

1. Open the pgAdmin app.
2. Right click **Servers**.
3. Click **Create** > **Server...**.
4. Enter a name for the server. For example, ```mental_health_tech_db```.
5. Click the **Connection** tab.
6. In the **Host name/Address** field, enter the AWS RDS endpoint URL.
7. In the **Username** field, enter the database username.
8. In the **Password** field, enter the database password.
9. Check the **Save Password?** checkbox.
10. Click **Save**.

## <a name="deployment"></a> Deploying the app

The app for this project is deployed to and hosted on Heroku. For more information on hosting with Heroku, see <https://devcenter.heroku.com/>. To deploy the app, you will need to have the Heroku CLI installed.

1. Download and Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```bash
heroku login
```

3. Clone the repository

Use Git to clone the repository to your local machine.

```bash
heroku git:clone -a mental-health-in-tech
cd mental-health-in-tech
```

4. Deploy your changes

```bash
git add .
git commit -m "changes"
git push heroku master --no-verify
```

## <a name="Issues"></a> Issues

If you find an issue while using the app or have a request, log the issue or request [here](https://github.com/abbylemon/mental_health_ML/issues). These issues will be addressed in a future code update.
