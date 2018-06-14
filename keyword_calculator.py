import constants
import operator
import six

def GetKeywords(*scores, **options):
    if options.get('scoresMatrix') != None:
        scoresRatingsMatrix = options.get('scoresMatrix')
    else:
        scoresRatingsMatrix = [1] * len(scores)

    if options.get('keywordsCount') != None:
        keywordsCount = options.get('keywordsCount')
    else:
        keywordsCount = 20

    resultScores = __getKeywords(scores, scoresRatingsMatrix)

    resultScores = __reshuffle(resultScores)
    resultScores = __cutoff(resultScores, keywordsCount)
    return resultScores

def __getKeywords(scores, ratings):
    __scores = {}
    for i, score in enumerate(scores):
        __score = __transform(score)
        __score = __normalize(__score)

        for kw in __score:
            if kw in __scores:
                __scores[kw] = __scores[kw]  + __score[kw] * ratings[i]
            else:
                __scores[kw] = __score[kw] * ratings[i]


    scoresCount = len(scores)
    for key in __scores:
        __scores[key] = __scores[key] / scoresCount
    return __scores

def __transform(tup):
    d = {}

    for el in tup:
        d[el[0]] = el[1]

    return d

def __normalize(arr):
    maxScore = max(*[el[1] for el in arr.items()])
    for kw in arr:
        arr[kw] = arr[kw] / maxScore

    return arr

def __reshuffle(arr):
    result = sorted(six.iteritems(arr), key=operator.itemgetter(1), reverse=True)
    return result

def __cutoff(arr, length):
    result = arr[:length]
    return result
