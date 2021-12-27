# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentences = ["VCG is the best team", "Praveen is a bad man"] # positive sentence example
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    print(ss["neg"])
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
        
    print()
