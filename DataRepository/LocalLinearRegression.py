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

    sampleX = np.array(sampleXList)
    sampleY = np.array(sampleYList)

    from matplotlib import pyplot as pl

    yest = LOWESS.lowess(sampleX, sampleY, iter=10)

    import pylab as pl
    pl.clf()
    pl.title("")
    pl.scatter(sampleX, sampleY, label=graphLabel)
    pl.plot(sampleX, yest, label='rating prediction', color='red')
    pl.xlabel(xLabel)
    pl.ylabel(yLabel)
    pl.legend()
    pl.show()