import rake_worker
import c_value_worker
import statistics_worker
import keyword_calculator

def GetConcepts(textsData):

    rakeScores = rake_worker.GetScore(textsData['lemmatizedTexts']['joined'])
    cvalueScores = c_value_worker.GetScores(textsData['analytics']['joined'], textsData['lemmas']['joined'])

    currentKeywords = set()
    for score in rakeScores:
        currentKeywords.add(score[0])
    for score in cvalueScores:
        currentKeywords.add(score[0])

    tridfScores, rdfScores, enthropyScores = statistics_worker.GetScores(currentKeywords,
                                             textsData['lemmas']['joined'],
                                             textsData['lemmas']['list'],
                                             textsData['lemmatizedTexts']['joined'],
                                             textsData['lemmatizedTexts']['list'])

    keywords = keyword_calculator.GetKeywords(rakeScores, cvalueScores, tridfScores, rdfScores, enthropyScores,
                                   scoresMatrix = [0.3, 1, 0.5, 0.05, 0.01])

    return keywords

