import spacy
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np

from db import get_articles, get_connection
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nlp = spacy.load('en_core_web_sm')


def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)

def analyze_article(title, summary):
    text = title + ' ' + summary
    sentiment = analyze_sentiment(text)
    ent = extract_entities(text)
    sent_ent_d = {"sentiment": sentiment,"entities" :ent}
    return sent_ent_d


def extract_entities(text):
    entities = []
    doc = nlp(text)
    for ent in doc.ents:
        entities.append(ent.text)
    return entities

def get_tfidf_keywords(texts, n=10):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    sorted = np.argsort(tfidf_matrix.toarray().sum(axis = 0))[::-1]
    indexes = sorted[:n]
    feature_names = vectorizer.get_feature_names_out()
    return feature_names[indexes]



if __name__ == "__main__":
    articles = get_articles()
    text = [art[0] + ' ' + art[1] for art in articles]

    print(get_tfidf_keywords(text))