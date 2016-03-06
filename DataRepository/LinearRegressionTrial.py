import DatabasePlugs
import numpy as np
import random
from sklearn import linear_model
from enum import Enum

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

    graphLabel = ""

    sampleYList = []
    sampleXList = []
    testYList = []
    testXList = []

    for anime in animeList:
        if (anime.score < 2):
            continue
        num = random.random()
        x = anime.score
        y = []

        if(testType == TestType.episodes):
            y = [anime.episodes]
            graphLabel = 'rating/episodes'
        elif (testType == TestType.startMonth):
            y = [anime.getMonth()]
            graphLabel = 'rating/start month'
        elif (testType == TestType.startYear):
            y = [anime.getYear()]
            graphLabel = 'rating/start year'
        elif (testType == TestType.ratingCount):
            y = [anime.ratingCount]
            graphLabel = 'rating/user rating count'
        elif (testType == TestType.duration):
            y = [anime.duration]
            graphLabel = 'rating/duration'
        elif (testType == TestType.ageRating):
            y = [anime.ageRating]
            graphLabel = 'rating/age rating'

        if (num <= .25):
            testYList.append(x)
            testXList.append(y)
        else:
            sampleYList.append(x)
            sampleXList.append(y)

    sampleX = np.array(sampleXList)
    sampleY = np.array(sampleYList)

    testX = np.array(testXList)
    testY = np.array(testYList)

    from matplotlib import pyplot as pl

    testX, testY = zip(*sorted(zip(testX, testY)))

    lr = linear_model.LogisticRegression()
    lr.fit(sampleX,sampleY)

    pl.scatter(testX, testY, label=graphLabel, color='red')
    pl.plot(testX, lr.predict(testX), label='rating prediction')
    pl.legend()
    pl.show()