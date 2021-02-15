def infer_sentiment(sentiment):
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