from collections import Counter

from flask import Flask, jsonify, request
from flask_cors import CORS
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

from utils.infer_sentiment import infer_sentiment
from utils.cleanup import filter_words, clean_sentence
from utils.summary import get_tfidf

nltk.download('stopwords')


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return jsonify({'message': 'hello from the scrivi backend.'})


@app.route('/analyse', methods=['POST'])
def analyse():

  '''
    1. Clean up text ✅
    2. Stats ✅
      1. Number of words ✅
      2. Number of sentences ✅
      3. Frequency of words ✅
    3. Sentiment ✅
    4. Summary
  '''
  STOPWORDS = stopwords.words('english')
  data = request.json
  text = data['text']
  
  blob = TextBlob(text)

  sentences = blob.sentences
  
  len_sentences = len(sentences)
  
  filtered_words = filter_words(blob.words, STOPWORDS)
  word_freq = Counter(filtered_words)
  stopword_count = len(blob.words) - len(filtered_words)
  tfidf, tf_words = get_tfidf(blob.sentences, len(blob.sentences), filtered_words, len(filtered_words), word_freq, STOPWORDS)
  
  
  return jsonify({
    'stats': {
      'sentences': len_sentences,
      'words': len(blob.words),
      'word_count': word_freq,
      'stopword_count': stopword_count
    },
    'sentiment': infer_sentiment(blob.sentiment.polarity),
    'tfidf': {clean_sentence(k.string): v for k, v in tfidf.items()},
    'tf_words': tf_words
  })

if __name__ == '__main__':
  app.run(debug = True)