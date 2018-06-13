import re
import nltk

def GetScores(keywords, lemmas, lemmasList, text, texts):
    tmpWords = set()
    words = set()
    for word in lemmas:
        tmpWords.add(word)

    alphabet = re.compile(u'[a-zA-Zа-яА-ЯёЁ ]+')
    stopWords = nltk.corpus.stopwords.words('russian')

    for word in tmpWords:
        if len(word) > 2 and not word in stopWords:
            if alphabet.fullmatch(word):
                words.add(word)
    del tmpWords

    words.update(keywords)

    tfidfScore = __tf_idf(words, lemmasList, texts)

def __tf_idf(keywords, lemmasList, texts):
    for keyword in keywords:
        textsResults = []
        for i, text in enumerate(texts):
            countInText = text.count(keyword)
            textLen = len(lemmasList[i])
    return 0

def __rtf(keywords, text):
    return 0

def __e(keywords, text):
    return 0

