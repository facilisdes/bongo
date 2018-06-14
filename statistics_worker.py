import nltk
import math
import operator
import six

def GetScores(keywords, lemmas, lemmasList, text, texts):
    words = __generateFullKeywords(keywords, lemmas)
    textsLen = sum([len(ll) for ll in lemmasList])
    tfidfScore = __tf_idf(words, lemmasList)
    rtfScore = __rtf(words, lemmas, textsLen)
    enthropyScore = __e(rtfScore)

    tfidfScore = sorted(six.iteritems(tfidfScore), key=operator.itemgetter(1), reverse=True)
    rtfScore = sorted(six.iteritems(rtfScore), key=operator.itemgetter(1), reverse=True)
    enthropyScore = sorted(six.iteritems(enthropyScore), key=operator.itemgetter(1), reverse=True)

    return tfidfScore, rtfScore, enthropyScore

def __generateFullKeywords(keywords, lemmas):
    tmpWords = set()
    words = set()
    for word in lemmas:
        tmpWords.add(word)

    stopWords = nltk.corpus.stopwords.words('russian')

    for word in tmpWords:
        if len(word) > 2 and not word in stopWords:
            words.add(word)
    del tmpWords

    words.update(keywords)
    return words

def __tf_idf(keywords, lemmasList):
    textsLengths = []
    textsLength = 0
    result = {}

    for i, text in enumerate(lemmasList):
        textLen = len(lemmasList[i])
        textsLengths.insert(i, textLen)
        textsLength = textsLength + textLen

    for keyword in keywords:
        textsResults = []
        keywordOccasions = 0
        for i, text in enumerate(lemmasList):
            countInText = text.count(keyword)
            if countInText>0: keywordOccasions = keywordOccasions+1
            textLen = textsLengths[i]
            textsResults.insert(i, {'len':textLen, 'count':countInText})

        rating = 0
        for tr in textsResults:
            if tr['len'] > 0 and keywordOccasions > 0:
                subrating = (tr['count']/tr['len']) * math.sqrt(textsLength / (keywordOccasions * tr['len']))
                rating = rating + subrating
        result[keyword] = rating

    return result

def __rtf(keywords, text, textsLen):
    result = {}
    for keyword in keywords:
        rating = text.count(keyword) / textsLen
        result[keyword] = rating
    return result

def __e(rtfs):
    result = {}
    for keyword, rtf in rtfs.items():
        rating = 0
        if rtf>0:
            rating =-rtf * math.log2(rtf)
        result[keyword] = rating
    return result

