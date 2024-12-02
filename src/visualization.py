import matplotlib.pyplot as plt

def plot_aspect_sentiments(data, aspect):
    aspect_data = data['AspectSentiments'].apply(lambda x: x.get(aspect, None)).dropna()
    aspect_data.value_counts().plot(kind = 'bar', color = ['green', 'red'])
    plt.title(f"Sentiment Distribution for Aspect: {aspect}")
    plt.xlabel("Sentiment")
    plt.ylabel("Frequency")
    plt.show()