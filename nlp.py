import re
import html
import spacy
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

from db import get_articles
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nlp = spacy.load('en_core_web_sm')

def clean_text(text):

    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = html.unescape(text)
    return text


def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)

def analyze_article(title, summary):
    text = title + ' ' + summary
    c_text = clean_text(text)
    sentiment = analyze_sentiment(c_text)
    ent = extract_entities(c_text)
    sent_ent_d = {"sentiment": sentiment,"entities" :ent}
    return sent_ent_d

def extract_entities(text):
    entities = []
    doc = nlp(text)
    for ent in doc.ents:
        entities.append(ent.text)
    return entities

def get_tfidf_keywords(texts, n=10):
    my_stop_words = list(text.ENGLISH_STOP_WORDS.union(["diplomat", "reuters", "asia", "says"]))

    vectorizer = TfidfVectorizer(stop_words= my_stop_words )
    tfidf_matrix = vectorizer.fit_transform(texts)
    sorted = np.argsort(tfidf_matrix.toarray().sum(axis = 0))[::-1]
    indexes = sorted[:n]
    feature_names = vectorizer.get_feature_names_out()
    return feature_names[indexes]

if __name__ == "__main__":
    articles = get_articles()
    text = [art[0] + ' ' + art[1] for art in articles]

    print(get_tfidf_keywords(text))