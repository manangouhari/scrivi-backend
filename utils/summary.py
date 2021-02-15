from collections import defaultdict
from math import log
from .cleanup import filter_words


def get_tf_words(words, words_count, words_len):
    """
    Returns the tf value of all words.
    tf[word] = total appearances of the word / total words
    """
    tf = defaultdict(float)
    for word in words_count:
        tf[word] = words_count[word] / words_len
    return tf

def get_tf_sentences(sentences, tf_words, stopwords):
    """
    Returns the tf value of each sentence.
    tf[sentence] = sum(tf of words in s) / total words in s
    """
    tf = defaultdict(float)
    for sentence in sentences:
        words_in_s = filter_words(sentence.words, stopwords)
        tf[sentence] = sum(tf_words[word] for word in words_in_s)/len(words_in_s)
    return tf

def get_idf_words(words, words_count, words_len, len_sentences):
  """
  Returns idf value of each word.
  idf[word] = log(total sentences / number of times the word appears)
  """
  idf = defaultdict(float)
  for word in words_count:
      idf[word] = log(len_sentences/words_count[word], 10)
  return idf

def get_idf_sentences(sentences, idf_words, stopwords):
    """
    Returns idf of each sentence.
    idf[sentence] = sum(idf of each word in sentence) / total words in sentence
    """
    idf = defaultdict(float)
    for sentence in sentences:
        words_in_s = filter_words(sentence.words, stopwords)
        idf[sentence] = sum(idf_words[word] for word in words_in_s)/len(words_in_s)
    return idf


def get_tfidf(sentences, sent_len, words, words_len, words_freq, stopwords):
  tf_words = get_tf_words(words, words_freq, words_len)
  tf_sentences = get_tf_sentences(sentences, tf_words, stopwords)

  idf_words = get_idf_words(words, words_freq, words_len, sent_len)
  idf_sentences = get_idf_sentences(sentences, idf_words, stopwords)

  tfidf = {s:(tf_sentences[s]*idf_sentences[s]) for s in sentences}
  
  return tfidf, tf_words