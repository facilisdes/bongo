import c_value
import re

def GetScores(analytics, lemmatizedText):
    c_value_input = []

    sentence_delimiters = re.compile(u'[\[\]\n.!?,;:—\t\-\"()“”„«»‘’\'\u2013]')
    for a in analytics:
        if 'analysis' in a and len(a['analysis']) > 0 and 'lex' in a['analysis'][0]:
            r = {'pos': a['analysis'][0]['gr'].split(',')[0].split('=')[0], 'word': a['analysis'][0]['lex']}
            c_value_input.append(r)
        else:
            if sentence_delimiters.match(a['text']):
                r = {'pos': 'DIVIDER', 'word': a['text']}
                c_value_input.append(r)

    result = c_value.GetScore(c_value_input, lemmatizedText)
    return result