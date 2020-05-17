# Mental Health in Tech and Machine Learning

## Getting Started

### Set up AWS and Google Drive

This project uses AWS to store the data files in a S3 bucket and uses Google Colab notebooks to extract, transform, load, and analyze that data.

To set up AWS and Google Drive for this project, run through the cells in the [cloud_setup.ipynb](./cloud_setup.ipynb) notebook.

### Load csv files from S3 bucket into Pandas dataframes to perform ETL

After setting up AWS and Google Drive, run through the cells in the [cloud_etl.ipynb](./cloud_etl.ipynb) notebook to load the csv files from the S3 bucket into Pandas dataframes to extract, transform, and eventually load the data into a Postgres database.

### Create schema and tables

Run through the cells in the [schema.ipynb](./schema.ipynb) file to create the schema for the database tables and connect to the database to verify that the tables were created.

## Database Structure

This project uses a SQL database hosted on AWS to store the mental health survey results. For more information about the database structure used for this project, see [Database Structure](./docs/database.md).

## Starting the Flask App

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

4. Navigate to <http:localhost:5000> in Chrome (or whatever browser you prefer) to view the app.

## Using the pgAdmin app to view and query the database locally

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
