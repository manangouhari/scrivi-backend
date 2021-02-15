import re

# def cleanup(sent):
#     filter_arr = []
#     words = sent.words
#     tokens = []
#     for word in words:

#         if not (word.is_stop or word.is_punct or word.is_space or word.text == '=' or word.lemma_ == '-PRON-'):
#             tokens.append(re.sub(r'[\t\n\r=]', '', word.lemma_.lower()))

#     return ' '.join(tokens)


# def sanitize_for_model(sents):
#     clean_func = np.vectorize(cleanup)
#     return clean_func(sents)



# def sanitize_original(sent):
#     return re.sub(r'[\t\n\r]', '', sent)


def contains_digit(word):
  for ch in word:
    if ch.isdigit(): return True
  return False

def clean_word(word):
  return re.sub(r'\'\"' ,'', word.singularize().lower())

def filter_words(words, stopwords):
  return list(map(clean_word ,filter(lambda x: x not in stopwords and not contains_digit(x) and '\'' not in x, words)))

def clean_sentence(sentence):
  return re.sub(r'[\t\n\r=]', '', sentence)