import LOWESS, DatabasePlugs
from sklearn import linear_model
from sklearn import tree
from sklearn import svm
from sklearn.datasets import load_iris

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
    	Y.append([anime.score])
    	X.append([anime.episodes])

    #iris = load_iris()

    #print len(iris.data)
    #print len(iris.target)
    #print iris.target

    #decisionTree = tree.DecisionTreeClassifier()
    #decisionTree = decisionTree.fit(iris.data,iris.target)
    #print decisionTree.predict([5.9,  3.,   5.1,  1.8])

    decisionTree = tree.DecisionTreeClassifier()
    decisionTree = decisionTree.fit(X,Y)
    print decisionTree.predict([200])

    #goodluck = svm.SVC()

    #goodluck.fit(X,Y)
    #LOWESS.lowess(ratingList, episodeList)
	#clf = linear_model.LinearRegression()
	#clf.fit(ratingList, episodeList)