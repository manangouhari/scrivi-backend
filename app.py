# Counter to count the word frequency
from collections import Counter

from flask import Flask, jsonify, request
# CORS - https://en.wikipedia.org/wiki/Cross-origin_resource_sharing
from flask_cors import CORS


import nltk
from nltk.corpus import stopwords

from textblob import TextBlob

from utils.cleanup import filter_words, clean_sentence
from utils.infer_sentiment import infer_sentiment
from utils.summary import get_tfidf



app = Flask(__name__)
CORS(app)

@app.before_first_request
def before_first_req():
  nltk.download('stopwords')

@app.route('/')
def index():
  return jsonify({'message': 'hello from the scrivi backend.'})


@app.route('/analyse', methods=['POST'])
def analyse():
  
  STOPWORDS = stopwords.words('english')
  try: 
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
  except Exception as e:
    return jsonify({'error': str(e)}), 400
  


if __name__ == '__main__':
  app.run(debug = True)