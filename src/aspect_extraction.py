import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_aspects(text):
    doc = nlp(text)
    aspects = []

    for chunk in doc.noun_chunks:
        # Excluding entities such as proper nouns, locations or irrelevant terms
        if chunk.root.ent_type_ in ['PERSON', 'GPE', 'ORG', 'WORK_OF_ART']:
            continue  
        if chunk.root.tag_ not in ['PRP', 'PRP$', 'DT'] and not chunk.root.is_stop:
            # Focusing on meaningful dependency relations
            if chunk.root.dep_ in ['dobj', 'nsubj', 'pobj', 'attr', 'appos']:
                aspects.append(chunk.text)

    filtered_aspects = []
    for aspect in aspects:
        blob = TextBlob(aspect)
        if -0.2 <= blob.sentiment.polarity <= 0.2: 
            filtered_aspects.append(aspect)

    return filtered_aspects

def filter_relevant_aspects(aspects, text):
    if not aspects:
        return []

    aspect_embeddings = model.encode(aspects)
    review_embedding = model.encode([text])

    relevance_scores = cosine_similarity(aspect_embeddings, review_embedding).flatten()

    relevant_aspects = [aspect for aspect, score in zip(aspects, relevance_scores) if score > 0.6]

    return relevant_aspects

def get_context_sentences(text, aspects):
    doc = nlp(text)
    context = {}
    for aspect in aspects:
        sentences = [sent.text for sent in doc.sents if aspect in sent.text]
        if sentences:
            context[aspect] = " ".join(sentences)
    return context

def train_model(X, y):
    model = SGDClassifier(loss='log_loss', max_iter=1000, tol=1e-3, random_state=42)
    model.fit(X, y)
    return model

def predict_aspect_sentiments(aspects, model, vectorizer):
    aspect_sentiments = {}
    for aspect, context in aspects.items():
        vectorized = vectorizer.transform([context])
        sentiment = model.predict(vectorized)
        aspect_sentiments[aspect] = sentiment[0]
    return aspect_sentiments

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    return accuracy

