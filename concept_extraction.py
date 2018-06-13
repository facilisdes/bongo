import rake_worker
import c_value_worker
import statistics_worker

def GetConcepts(textsData):

    rakeScores = rake_worker.GetScore(textsData['lemmatizedTexts']['joined'])
    cvalueScores = c_value_worker.GetScores(textsData['analytics']['joined'], textsData['lemmatizedTexts']['joined'])

    currentKeywords = set()
    for score in rakeScores:
        currentKeywords.add(score[0])
    for score in cvalueScores:
        currentKeywords.add(score[0])

    statScores = statistics_worker.GetScores(currentKeywords,
                                             textsData['lemmas']['joined'],
                                             textsData['lemmas']['list'],
                                             textsData['lemmatizedTexts']['joined'],
                                             textsData['lemmatizedTexts']['list'])