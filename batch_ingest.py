import s3fs
from s3fs.core import S3FileSystem
import pickle
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd


def ingest_data():
    api = KaggleApi()
    api.authenticate()

    # downloading the kaggle data set as a zip file
    api.dataset_download_files('bharatnatrayn/movies-dataset-for-feature-extracion-prediction')

    # extracting the csv file from the zipped file
    with ZipFile("movies-dataset-for-feature-extracion-prediction.zip", 'r') as zipObject:
        zipObject.extract("movies.csv")
    zipObject.close()

    # turn csv file into a pandas data frame
    data = pd.read_csv('movies.csv')

    s3 = S3FileSystem()
    # S3 bucket directory
    DIR = 's3://ece5984-bucket-timj90/HW1/'  # insert here
    # Push data to S3 bucket as a pickle file
    with s3.open('{}/{}'.format(DIR, 'kaggle_data.pkl'), 'wb') as f:
        f.write(pickle.dumps(data))
