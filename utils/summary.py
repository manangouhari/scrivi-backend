from collections import defaultdict
from math import log
from .cleanup import filter_words


def get_tf_words(words, words_count, words_len):
    """
    Returns the tf value of all words.
    tf[word] = total appearances of the word / total words
    Parameters:
        words (list[str]): list of words for which term-frequency scores will be calculated.
        words_count ({str: int}): a frequency dictionary containing the data for how many times a word appears in the text.
        words_len (int): total number of words in the text.
    Returns:
        tf ({str: float}): dictionary containing tf scores for each word.
    """
    tf = defaultdict(float)
    for word in words_count:
        tf[word] = words_count[word] / words_len
    return tf

def get_tf_sentences(sentences, tf_words, stopwords):
    """
    Returns the tf value of each sentence.
    tf[sentence] = sum(tf of words in s) / total words in s
    Parameters:
        sentences (list[str]): the list of sentences for which tf scores need to be calculated.
        tf_words ({str: float}): dictionary containing the tf score for each word.
    Returns:
        tf ({str: float}): dictionary containing tf scores for each sentence.
    """
    tf = defaultdict(float)
    for sentence in sentences:
        words_in_s = filter_words(sentence.words, stopwords)
        tf[sentence] = sum(tf_words[word] for word in words_in_s)/len(words_in_s)
    return tf

def get_idf_words(words, words_count, words_len, len_sentences):
    """
    Returns inverse document frequency(idf) value of each word.
    idf[word] = log(total sentences / number of times the word appears)
    Parameters:
        words (list[str]): list of words for which idf scores will be calculated.
        words_count ({str: int}): a frequency dictionary containing the data for how many times a word appears in the text.
        words_len (int): total number of words in the text.
        len_sentences (int): total number of sentences in the text.
    Returns:
        idf ({str: float}): idf scores for each sentence.  
    """
    idf = defaultdict(float)
    for word in words_count:
        idf[word] = log(len_sentences/words_count[word], 10)
    return idf

def get_idf_sentences(sentences, idf_words, stopwords):
    """
    Returns idf of each sentence.
    idf[sentence] = sum(idf of each word in sentence) / total words in sentence
    Parameters:
        sentences (list[str]): the list of sentences for which idf scores need to be calculated.
        idf_words ({str: float}): dictionary containing the idf score for each word.
        stopwords (list[str]): list of stopwords.
    Returns:
        tf ({str: float}): dictionary containing tf scores for each sentence.
    
    """
    idf = defaultdict(float)
    for sentence in sentences:
        words_in_s = filter_words(sentence.words, stopwords)
        idf[sentence] = sum(idf_words[word] for word in words_in_s)/len(words_in_s)
    return idf


def get_tfidf(sentences, sent_len, words, words_len, words_freq, stopwords):
    """
    Returns the tfidf score for each sentences, and the tf score for each word.
    Parameters:
        sentences (list[str]): list of sentences in the text.
        sent_len (int): total number of sentences in the text.
        words (list[str]): list of words in the text.
        words_len (int): total number of words in the text.
        words_freq ({str: int}): count of how many times a word appears in the text.
        stopwords (list[str]): list of stopwords.
    """
    tf_words = get_tf_words(words, words_freq, words_len)
    tf_sentences = get_tf_sentences(sentences, tf_words, stopwords)

    idf_words = get_idf_words(words, words_freq, words_len, sent_len)
    idf_sentences = get_idf_sentences(sentences, idf_words, stopwords)

    tfidf = {s:(tf_sentences[s]*idf_sentences[s]) for s in sentences}
    
    return tfidf, tf_words