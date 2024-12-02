import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "Reviews_small.csv")

#MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "aspect_sentiment"
COLLECTION_NAME = "reviews"