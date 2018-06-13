from pymystem3 import Mystem
import re

def PrepareText(texts):
    # regex = re.compile('[^a-zA-Zа-яА-ЯёЁ0-9\(\)]')
    # First parameter is the replacement, second parameter is your input string
    # regex.sub('', 'ab3d*E')

    mystem = Mystem()

    origText = ""
    lemmatizedText = ""
    lemmatizedTexts = []
    analytics = []
    originals = []
    lemmas = []
    analyticsForTexts = []
    originalsForTexts = []
    lemmasForTexts = []
    for text in texts:
        analytic = mystem.analyze(text)

        original = []
        lemma = []
        for el in analytic:
            original.append(el['text'])
            if('analysis' in el and len(el['analysis']) > 0 and 'lex' in el['analysis'][0]):
                lemma.append(el['analysis'][0]['lex'])
            else:
                lemma.append(el['text'])

        origText = origText + text
        lemmasText = ''.join(lemma)
        lemmatizedText = lemmatizedText + lemmasText
        lemmatizedTexts.append(lemmasText)
        analytics.extend(analytic)
        originals.extend(original)
        lemmas.extend(lemma)
        analyticsForTexts.append(analytic)
        originalsForTexts.append(original)
        lemmasForTexts.append(lemma)

    result = {
        'texts':{'joined':origText, 'list':texts},                              #оригинальные тексты
        'lemmatizedTexts': {'joined': lemmatizedText, 'list': lemmatizedTexts}, #лемматизированные тексты
        'lemmas':{'joined':lemmas, 'list':lemmasForTexts},                      #списки лемм
        'originals':{'joined':originals, 'list':originalsForTexts},             #списки оригиналов слов
        'analytics':{'joined':analytics, 'list':analyticsForTexts},             #данные по анализу
    }

    return result