import nltk
import lib.RAKE.rake as rake
import constants
import math

def GetScore(text, cutoffPercent=constants.RAKE_CUTOFF_PERCENTAGE):

    scores = __getScore(text)
    scores = __cutoff(scores, cutoffPercent)
    return scores

def __getScore(text):
    rakeObj = rake.Rake(stop_words_list=nltk.corpus.stopwords.words('russian'), min_char_length=4, max_words_length=3,
                        min_keyword_frequency=2, long_phrases_score_correction='default')
    result = rakeObj.run(text)
    return result

def __cutoff(arr, cutoffPercent):
    if(cutoffPercent < 1):
        #in case if passed value = 0.8 instead of 80
        cutoffPercent = cutoffPercent * 100

    rightBoundary = cutoffPercent * len(arr) / 100
    result = arr[0:math.ceil(rightBoundary)]
    return result