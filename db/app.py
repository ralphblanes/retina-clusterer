from pymongo import MongoClient
from bson.objectid import ObjectId
import time
import hashlib

#client = MongoClient('mongodb://localhost:27017/') # for use in localhost
#db = client['BigData'] # for use in localhost
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