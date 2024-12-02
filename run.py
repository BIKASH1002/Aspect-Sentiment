import pandas as pd
from src.data_loader import load_data
from src.db_handler import insert_data
from src.aspect_extraction import extract_aspects, filter_relevant_aspects, get_context_sentences, predict_aspect_sentiments
from src.model_training import train_sentiment_model
from src.visualization import plot_aspect_sentiments

data = load_data()

# Extracting aspects and context
aspect_data = []
for _, row in data.iterrows():
    raw_aspects = extract_aspects(row['Text'])

    relevant_aspects = filter_relevant_aspects(raw_aspects, row['Text'])

    if relevant_aspects:
        context = get_context_sentences(row['Text'], relevant_aspects)
        for aspect, context_sentence in context.items():
            aspect_data.append({'Aspect': aspect, 'Context': context_sentence, 'Sentiment': row['Sentiment']})

aspect_df = pd.DataFrame(aspect_data)

# Training sentiment model
if not aspect_df.empty:
    model, vectorizer = train_sentiment_model(aspect_df)

    # Sentiment prediction for aspects
    data['AspectSentiments'] = data['Text'].apply(
        lambda x: predict_aspect_sentiments(
            get_context_sentences(x, extract_aspects(x)), model, vectorizer
        )
    )

    insert_data(data)
    print("Pipeline complete!")
else:
    print("No aspects were extracted. Skipping model training.")