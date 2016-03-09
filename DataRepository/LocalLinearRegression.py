import DatabasePlugs
import numpy as np
import random
from enum import Enum
import sys
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score

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
            x = anime.episodes
            graphLabel = 'rating/episodes'
            xLabel = "Episode Count"
        elif (testType == TestType.startMonth):
            x = anime.getMonth()
            graphLabel = 'rating/start month'
            xLabel = "Start Month"
        elif (testType == TestType.startYear):
            x = anime.getYear()
            graphLabel = 'rating/start year'
            xLabel = "Start Year"
        elif (testType == TestType.ratingCount):
            x = anime.ratingCount
            graphLabel = 'rating/user rating count'
            xLabel = "Number of Users Rating"
        elif (testType == TestType.duration):
            x = anime.duration
            graphLabel = 'rating/duration'
            xLabel = "Episode Duration"
        elif (testType == TestType.ageRating):
            x = anime.ageRating
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

    yest = LOWESS.lowess(sampleX, sampleY, iter=10)

    test = np.interp(testX, sampleX, yest)

    #Calculating Statistics
    meanSquaredError = mean_squared_error(testY,test)
    meanAbsoluteErrorScore = mean_absolute_error(testY,test)
    medianAbsoluteErrorScore = median_absolute_error(testY,test)
    r2Score = r2_score(testY,test)
    print "mean squared error", meanSquaredError
    print "mean absolute error", meanAbsoluteErrorScore
    print "median absolute error", medianAbsoluteErrorScore
    print "R^2 score", r2Score

    import matplotlib.pylab as pl
    pl.clf()
    pl.title("")
    pl.scatter(sampleX, sampleY, label=graphLabel)
    pl.plot(sampleX, yest, label='rating prediction', color='red')
    #pl.plot(testX, test, label='test', color='green')
    pl.xlabel(xLabel)
    pl.ylabel(yLabel)
    pl.legend()
    pl.show()
