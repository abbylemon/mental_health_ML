# Mental Health in Tech and Machine Learning

## Getting Started

### Set up AWS and Google Drive

This project uses AWS to store the data files in a S3 bucket and uses Google Colab notebooks to extract, transform, load, and analyze that data.

To set up AWS and Google Drive for this project, run through the cells in the [cloud_setup.ipynb](./cloud_setup.ipynb) notebook.

### Load csv files from S3 bucket into Spark dataframes

After setting up AWS and Google Drive, run through the cells in the [cloud_etl.ipynb](./cloud_etl.ipynb) notebook to load the csv files from the S3 bucket into Spark dataframes.

### Create schema and tables

Run through the cells in the [schema.ipynb](./schema.ipynb) file to create the schema for the database tables and connect to the database to verify that the tables were created.

## Database Structure

This project uses a SQL database to store the mental health survey results. For more information about the database structure used for this project, see [Database Structure](./docs/database.md).
