import DatabasePlugs
import numpy as np
import random
from sklearn import linear_model
from enum import Enum

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

    testType = TestType.episodes

    graphLabel = ""

    sampleYList = []
    sampleXList = []
    testYList = []
    testXList = []

    for anime in animeList:
        if (anime.score < 2):
            continue
        num = random.random()
        y = anime.score
        x = []

        if(testType == TestType.episodes):
        if (anime.score < 2 or anime.episodes <= 0 
            or anime.episodes >= 100 or anime.duration <= 0):
                continue
            x = [anime.episodes]
            graphLabel = 'rating/episodes'
        elif (testType == TestType.startMonth):
            x = [anime.getMonth()]
            graphLabel = 'rating/start month'
        elif (testType == TestType.startYear):
            x = [anime.getYear()]
            graphLabel = 'rating/start year'
        elif (testType == TestType.ratingCount):
            x = [anime.ratingCount]
            graphLabel = 'rating/user rating count'
        elif (testType == TestType.duration):
            if anime.duration <= 0:
                continue
            x = [anime.duration]
            graphLabel = 'rating/duration'
        elif (testType == TestType.ageRating):
            x = [anime.ageRating]
            graphLabel = 'rating/age rating'

        if (num <= .25):
            testYList.append(y)
            testXList.append(x)
        else:
            sampleYList.append(y)
            sampleXList.append(x)

    sampleX = np.array(sampleXList)
    sampleY = np.array(sampleYList)

    testX = np.array(testXList)
    testY = np.array(testYList)

    from matplotlib import pyplot as pl

    testX, testY = zip(*sorted(zip(testX, testY)))

    errorArray = []

    lr = linear_model.LogisticRegression()
    lr.fit(sampleX,sampleY)

    for i in range(0, len(testX)-1):
        pre = lr.predict(testX[i])
        diff = abs(pre - testY[i])
        errorArray.append((diff/testY[i])*100)

    print np.mean(errorArray)

    pl.scatter(testX, testY, label=graphLabel, color='red')
    pl.plot(testX, lr.predict(testX), label='rating prediction')
    pl.legend()
    pl.show()