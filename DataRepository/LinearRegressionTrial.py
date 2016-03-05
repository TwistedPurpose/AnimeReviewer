import DatabasePlugs
import numpy as np
import random
from sklearn import linear_model
from enum import Enum

class TestType(Enum):
    episodes = 1
    startMonth = 2
    startYear = 3

if __name__=='__main__':
    plugs = DatabasePlugs.DatabasePlugs()
    animeList = plugs.getAllAnime()

    sampleRatingList = []
    sampleEpisodeList = []
    testRatingList = []
    testEpisodeList = []

    for anime in animeList:
        if (anime.score < 5 or anime.episodes < 0):
            continue
        num = random.random()
        if (num <= .25):
            testRatingList.append(anime.score)
            testEpisodeList.append([anime.episodes])
        else:
            sampleRatingList.append(anime.score)
            sampleEpisodeList.append([anime.episodes])

    episodeSample = np.array(sampleEpisodeList)
    ratingSample = np.array(sampleRatingList)

    episodeTest = np.array(testEpisodeList)
    ratingTest = np.array(testRatingList)

    from matplotlib import pyplot as pl

    lr = linear_model.LinearRegression()
    lr.fit(episodeSample,ratingSample)

    pl.scatter(episodeTest, ratingTest, label='episodes/rating', color='red')
    pl.plot(episodeTest, lr.predict(episodeTest), label='rating prediction')
    #pl.xticks(())
    #pl.yticks(())
    pl.show()