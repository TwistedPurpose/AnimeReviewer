import LOWESS, DatabasePlugs
from sklearn import linear_model
from sklearn import tree
from sklearn import svm

if __name__=='__main__':
    plugs = DatabasePlugs.DatabasePlugs()
    animeList = plugs.getAllAnime()

    ratingList = []
    episodeList = []
    X = []
    Y = []

    for anime in animeList:
        ratingList.append(anime.score)
        episodeList.append(anime.episodes)

    for anime in animeList:
    	Y.append([anime.episodes])
    	X.append([anime.episodes, anime.score])


    
    decisionTree = tree.DecisionTreeClassifier()
    decisionTree = decisionTree.fit(X,Y)
    print Y
    print decisionTree.predict_proba([12,6])

    goodluck = svm.SVC()

    goodluck.fit(X,Y)
    #LOWESS.lowess(ratingList, episodeList)
	#clf = linear_model.LinearRegression()
	#clf.fit(ratingList, episodeList)