def sentence_prob_with_next_word(next_word):
  outputProb = 1
  new_bigram = (input.split()[-1], next_word)
  if new_bigram in bigramAddOne:
    outputProb *= bigramAddOne[new_bigram]
  else:
    if new_bigram[0] not in unigramCounts:
      unigramCounts[new_bigram[0]] = 1
    prob = (1) / (unigramCounts[new_bigram[0]] + len(unigramCounts))
    outputProb *= prob
  return outputProb