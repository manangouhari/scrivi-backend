import re

def contains_digit(word):
  """
    Checks whether a word contains a digit or not.
      Parameters:
        word (str): string that needs to be checked.
      Returns:
        boolean: True is word contains a digit, else False.
  """
  for ch in word:
    if ch.isdigit(): return True
  return False

def clean_word(word):
  """
    Cleans up a word. 
    It does the following three thing -
      1. Convert to lowercase.
      2. Singularise the word.
      3. Removes single and double quotes.

      Parameters:
        word (str): word that needs to be cleaned up.
      Reurns:
        word (str): cleaned up version of the word.
  """
  return re.sub(r'\'\"' ,'', word.singularize().lower())

def filter_words(words, stopwords):
  """
    Removes words that don't match the criteria. 
    Then cleans up the words.
    Returns a list that contains the cleaned up form of words that match the criteria.
    Criteria to include a word -
      1. Should not be a stopword. 
        - Stopwords: https://en.wikipedia.org/wiki/Stop_word
      2. Should not contain digits. 
      3, Should not contain single quotes. Basically to get rid of contractions - shouldn't, wouldn't, etc.
    
      Parameters:
        words (list[str]): list of words in the text.
        stopwords (list[str]): list of stopwords. 

      Returns:
        wordlist (list[str]): list of cleaned up words that match the criteria.
  """
  return list(map(clean_word ,filter(lambda x: x not in stopwords and not contains_digit(x) and '\'' not in x, words)))

def clean_sentence(sentence):
  return re.sub(r'[\t\n\r=]', '', sentence)