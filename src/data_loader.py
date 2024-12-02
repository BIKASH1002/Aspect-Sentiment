import pandas as pd
from config.config import DATA_PATH

def load_data():
    data = pd.read_csv(DATA_PATH)
    data = data[['Text', 'Score']].dropna()
    data['Sentiment'] = data['Score'].apply(lambda x: 'positive' if x > 3 else 'negative')
    return data