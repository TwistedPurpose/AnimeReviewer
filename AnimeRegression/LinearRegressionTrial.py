import DatabasePlugs
import numpy as np
import random
from sklearn import linear_model
from enum import Enum
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
import sys

import LOWESS

class TestType(Enum):
    episodes = 1
    startMonth = 2
    startYear = 3
    ratingCount = 4
    duration = 5
    ageRating = 6

if __name__=='__main__':
    plugs = DatabasePlugs.DatabasePlugs()
    animeList = plugs.getAllAnime()
    
    testType = TestType.duration
    #Allow changing parameter without editing code
    if (len(sys.argv) > 1 ):
        if(sys.argv[1] == '1'):
            testType = TestType.episodes
        elif (sys.argv[1] == '2'):
            testType = TestType.startMonth
        elif (sys.argv[1] == '3'):
            testType = TestType.startYear
        elif (sys.argv[1] == '4'):
            testType = TestType.ratingCount
        elif (sys.argv[1] == '5'):
            testType = TestType.duration

    graphLabel = ""

    sampleYList = []
    sampleXList = []
    testYList = []
    testXList = []

    for anime in animeList:
        if (anime.score < 2 or anime.episodes <= 0 
            or anime.episodes >= 100 or anime.duration <= 0):
            continue
        num = random.random()
        y = anime.score
        x = []

        yLabel = "User Rating"
        xLabel = ""
        if(testType == TestType.episodes):
            x = [anime.episodes]
            graphLabel = 'rating/episodes'
            xLabel = "Episode Count"
        elif (testType == TestType.startMonth):
            x = [anime.getMonth()]
            graphLabel = 'rating/start month'
            xLabel = "Start Month"
        elif (testType == TestType.startYear):
            x = [anime.getYear()]
            graphLabel = 'rating/start year'
            xLabel = "Start Year"
        elif (testType == TestType.ratingCount):
            x = [anime.ratingCount]
            graphLabel = 'rating/user rating count'
            xLabel = "Number of Users Rating"
        elif (testType == TestType.duration):
            x = [anime.duration]
            graphLabel = 'rating/duration'
            xLabel = "Episode Duration"
        elif (testType == TestType.ageRating):
            x = [anime.ageRating]
            graphLabel = 'rating/age rating'
            xLabel = "Age Rating"

        if (num <= .1):
            testYList.append(y)
            testXList.append(x)
        else:
            sampleYList.append(y)
            sampleXList.append(x)

    sampleXList, sampleYList = zip(*sorted(zip(sampleXList, sampleYList)))
    testXList, testYList = zip(*sorted(zip(testXList, testYList)))

    sampleX = np.array(sampleXList)
    sampleY = np.array(sampleYList)

    testX = np.array(testXList)
    testY = np.array(testYList)

    from matplotlib import pyplot as pl

    lr = linear_model.LogisticRegression()
    lr.fit(sampleX,sampleY)

    meanSquaredError = mean_squared_error(testY,lr.predict(testX))
    meanAbsoluteErrorScore = mean_absolute_error(testY,lr.predict(testX))
    medianAbsoluteErrorScore = median_absolute_error(testY,lr.predict(testX))
    r2Score = r2_score(testY,lr.predict(testX))
    print "mean squared error", meanSquaredError
    print "mean absolute error", meanAbsoluteErrorScore
    print "median absolute error", medianAbsoluteErrorScore
    print "R^2 score", r2Score

    pl.scatter(sampleX, sampleY, label=graphLabel, color='red')
    pl.plot(testX, lr.predict(testX), label='rating prediction')
    pl.legend()
    pl.show()