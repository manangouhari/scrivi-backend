def infer_sentiment(sentiment):
  """
    Returns a label based on sentiment polarity score.
    Parameters:
      sentiment (float): represents the sentiment polarity score for the text.
    Returns
      result ([sentiment, label]): a list of size 2. First item being the sentiment score, second being the label.
  """
  label = ''
  if sentiment < -0.5:
    label = 'SUPER NEGATIVE'
  elif sentiment < 0:
    label = 'NEGATIVE'
  elif sentiment == 0:
    label = 'NEUTRAL'
  elif sentiment < .5:
    label = 'POSITIVE'
  else:
    label = 'SUPER POSITIVE'
  
  return [sentiment, label]