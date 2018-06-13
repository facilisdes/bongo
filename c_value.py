import operator
import six
import math
import constants

def GetScore(analytics, text, maxLengthInWords=constants.C_VALUE_MAX_LENGTH_IN_WORDS):
    keywords = __getKeywords(analytics)
    scores = __getScore(keywords, text, maxLengthInWords)
    return scores

def __getScore(keywords, text, maxLengthInWords):
    result = {}
    for keyword in keywords:
        wordsCount = len(keyword.split())
        if wordsCount > maxLengthInWords: continue
        countInText = text.count(keyword)
        countInKeywords = 0
        countOfEmbedingKeywords = 0
        for altKeyWord in keywords:
            if altKeyWord==keyword: continue
            if keyword in altKeyWord:
                countInKeyword = altKeyWord.count(keyword)
                countOfEmbedingKeywords = countOfEmbedingKeywords + 1
                countInKeywords = countInKeywords + countInKeyword

        rating = 0
        if countInKeywords==0:
            rating = math.log10(wordsCount) * countInText
        else:
            rating = math.log10(wordsCount) * (countInText - countInKeywords/countOfEmbedingKeywords)
        result[keyword] = rating
    result = sorted(six.iteritems(result), key=operator.itemgetter(1), reverse=True)
    return result


def __getKeywords(analytics):
    keywords = {}
    for i, w in enumerate(analytics):
        kws = set()
        kws.update(__checkForNNPattern(analytics, i))
        kws.update(__checkForANPattern(analytics, i))
        for kw in kws:
            if kw in keywords:
                keywords[kw] = keywords[kw] + 1
            else: keywords[kw] = 1
    return keywords


# Noun*Noun pattern
def __checkForNNPattern(sequence, index):
    start = 0
    relIndex = 0
    results = []
    while(index + relIndex < len(sequence)):
        w = sequence[index + relIndex]
        if w['pos'] != 'S': break
        else: relIndex = relIndex + 1
    if relIndex>0:
        result = ""
        for i in range(index, index+relIndex):
            result = result + sequence[i]['word'] + " "
            results.append(result.strip())
    return results


# (Adj|Noun)+Noun pattern
def __checkForANPattern(sequence, index):
    start = 0
    relIndex = 0
    results = []
    while(index + relIndex < len(sequence)):
        w = sequence[index + relIndex]
        if w['pos'] != 'A' and w['pos'] != 'S':
            # nothing to save
            break
        else:
            if(w['pos'] == 'S'):
                #(A|N)+ seq., ends with N
                if(relIndex>1):
                    result = ""
                    for i in range(index, index + relIndex + 1):
                        result = result + sequence[i]['word'] + " "
                    results.append(result.strip())
            relIndex = relIndex + 1
    return results

