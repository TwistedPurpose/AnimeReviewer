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
        if (anime.score < 2):
            continue
        num = random.random()
        x = anime.score
        y = []

        if(testType == TestType.episodes):
            if anime.episodes <= 0 or anime.episodes >= 100:
                continue
            y = anime.episodes
            graphLabel = 'rating/episodes'
        elif (testType == TestType.startMonth):
            y = anime.getMonth()
            graphLabel = 'rating/start month'
        elif (testType == TestType.startYear):
            if anime.getYear() < 1990:
                continue
            y = anime.getYear()
            graphLabel = 'rating/start year'
        elif (testType == TestType.ratingCount):
            y = anime.ratingCount
            graphLabel = 'rating/user rating count'
        elif (testType == TestType.duration):
            if anime.duration <= 0:
                continue
            y = anime.duration
            graphLabel = 'rating/duration'
        elif (testType == TestType.ageRating):
            y = anime.ageRating
            graphLabel = 'rating/age rating'

        sampleYList.append(x)
        sampleXList.append(y)

    sampleXList, sampleYList = zip(*sorted(zip(sampleXList, sampleYList)))

    sampleX = np.array(sampleXList)
    sampleY = np.array(sampleYList)

    from matplotlib import pyplot as pl

    yest = LOWESS.lowess(sampleX, sampleY)

    import pylab as pl
    pl.clf()
    pl.scatter(sampleX, sampleY, label=graphLabel)
    pl.plot(sampleX, yest, label='rating prediction', color='red')
    pl.legend()
    pl.show()