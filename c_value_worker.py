import c_value
import operator
import six
import re
import nltk

def GetScores(analytics, lemmatizedText):
    c_value_input = __prepare(analytics)
    result = c_value.GetScore(c_value_input, lemmatizedText)
    result = __sort(result)
    return result

def __prepare(analytics):
    c_value_input = []
    sentence_delimiters = re.compile(u'[\[\]\n.!?,;:\t\\"()“”„«»‘’\'_]')
    stopWords = nltk.corpus.stopwords.words('russian')

    for a in analytics:
        if 'analysis' in a and len(a['analysis']) > 0 and 'lex' in a['analysis'][0]:
            r = {'pos': a['analysis'][0]['gr'].split(',')[0].split('=')[0], 'word': a['analysis'][0]['lex']}
        else:
            if sentence_delimiters.match(a['text']):
                r = {'pos': 'DIVIDER', 'word': a['text']}
            else: continue
        if r['word'] in stopWords: continue
        c_value_input.append(r)

    return c_value_input

def __sort(data):
    result = sorted(six.iteritems(data), key=operator.itemgetter(1), reverse=True)
    return result

