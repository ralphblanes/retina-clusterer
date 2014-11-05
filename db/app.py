from pymongo import MongoClient
from bson.objectid import ObjectId
import time
import hashlib
import md5
from datetime import datetime, timedelta

## ~~~FOR USE IN LOCALHOST ONLY~~~ :D ##
# client = MongoClient('mongodb://localhost:27017/')
# db = client['BigData']

client = MongoClient('mongodb://146.148.59.202:27017/')
db = client['big_data']

def getCluster(clusterName):
    cluster = db.clusters.find({ "clusterName": clusterName })

    if cluster.count() <= 0:
        return {
            "error": "Error: No " + clusterName + " cluster found."
        }

    articles = []
    for articleId in cluster[0][u'articles']:
        article = db.articles.find_one({ "_id": articleId })
        # There must be a more effective way to get all the articles
        # without making the cursor go over the db multiple times...
        articles.append(article)

    return {
        "clusterName": cluster[0][u'clusterName'],
        "articles": articles,
        "_id": cluster[0][u'_id'],
        "features": cluster[0][u'features'],
    }

def getPopulatedArticlesByTimeStamp(timeStamp, limit):
    #"download_date": {"$gte": timeStamp }
    articles = db.articles.find({'$and': [{"v": "0.0.6"}, {"text": {'$ne': ''}}, {"title": {'$ne': ''}}, {"categories": {'$ne': [], '$ne': None}}]}).limit(limit);
    returnObject = {"articleArray": []}
    for article in articles:
        returnObject['articleArray'].append(article)

    return returnObject

def getAllArticlesByTimeStamp(timeStamp):
    articles = db.articles.find({ "download_date": {"$gte": timeStamp }})
    returnObject = {"articleArray": []}

    for article in articles:
        returnObject['articleArray'].append(article)

    return returnObject

def getPopulatedArticlesCount(timeStamp):
    count = db.articles.find({'$and': [{"v": "0.0.6"}, {"text": {'$ne': ''}}, {"title": {'$ne': ''}}, {"categories": {'$ne': [], '$ne': None}}]}).count()
    return count

def getAllArticlesCount(timestamp):
    count = db.articles.count()
    return count

def getArticleClusterList():
    articles = db.clusters.distinct('clusterName')
    clusterNameArray = []

    for article in articles:
        clusterNameArray.append(article)

    return clusterNameArray

def createCluster(clusterName, objectID):
    # objectID is an array
    db.clusters.insert( { "clusterName": clusterName, "_id": hashlib.md5(clusterName).hexdigest(), "objectIDs": objectID } )

def deleteCluster(clusterName):
    db.clusters.remove( { "clusterName": clusterName })

def insertArticles(articleIDs, clusterName):
    # articleIDs is an array
    db.clusters.update( { "clusterName": clusterName }, { "$push": { "articles": articleIDs } } )
