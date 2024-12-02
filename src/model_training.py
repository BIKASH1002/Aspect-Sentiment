from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.aspect_extraction import train_model, evaluate_model

def train_sentiment_model(data):
    vectorizer = CountVectorizer(max_features=5000, stop_words='english')
    X = vectorizer.fit_transform(data['Context']) 
    y = data['Sentiment']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = train_model(X_train, y_train)
    
    evaluate_model(model, X_test, y_test)
    
    return model, vectorizer
