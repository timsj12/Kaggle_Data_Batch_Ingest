import pandas as pd
from zipfile import ZipFile

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

api.dataset_download_files('bharatnatrayn/movies-dataset-for-feature-extracion-prediction')

# loading the temp.zip and creating a zip object
with ZipFile("movies-dataset-for-feature-extracion-prediction.zip", 'r') as zObject:
    # Extracting specific file in the zip
    # into a specific location.
    zObject.extract("movies.csv")
zObject.close()

df = pd.read_csv('movies.csv')
print(df.head)

#data = os.system('kaggle datasets download -d  borismarjanovic/price-volume-data-for-all-us-stocks-etfs/')
# url = "https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs/download"
