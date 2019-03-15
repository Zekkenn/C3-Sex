from test import Extractor
from settings import PROJECT_ROOT
from threading import Thread

import SA_Module.sentimentAnalysis as sentimentModule
import EC_Module.emotional_classifier as emotionalModule
import analytics
import Slangs.slangExtractor as slangs

import datetime

BOTS_N = 1

def startBot( bot ):
    bot.moti()

def saveReplies( bots ):
    files = list()
    for bot in bots:
        userResponses = bot.getConversation()
        fileName = PROJECT_ROOT + "\\UsersReplies\\" + str(datetime.datetime.now()).replace(":","_").replace("-","_").replace(" ","_").replace(".","_") + ".txt"
        files.append(fileName)        
        with open(fileName, 'w+') as file:
            for response in userResponses:
                newResponse = response
                for key, value in slangs.getSlangs().items():
                    newResponse = newResponse.replace(" " + key + " ", " " + value + " ")
                file.write(newResponse)
    return(files)
        
def saveMetrics( emotions, sentiments, timeMetric, rulesMetric, files ):
    fileName = PROJECT_ROOT + "\\UsersReplies\\" + str(datetime.datetime.now()).replace(":","_").replace("-","_").replace(" ","_").replace(".","_") + "_ALLMETRICS" + ".txt"
    with open(fileName + "_Metrics.txt", 'w+') as file:
        file.write("Negative Sentiments; Positive Sentiments; Neutral Sentiments; Time Metric; Rules Triggered Metric\n")
        for i in range( len(files) ):
            suma = emotions[i][0] + emotions[i][1] + emotions[i][2]
            suma = 1 if suma == 0 else suma
            file.write( str(emotions[i][0]/suma) + ";" + str(emotions[i][1]/suma) + ";" + str(emotions[i][2]/suma) + ";" + str( timeMetric[i] ) + ";" + str( rulesMetric[i] ) )
            

def analyze( repFiles ):
    sentiments = []
    emotions = []
    for file in repFiles:
        # Sentiment Analysis
        sentiments.append( sentimentModule.sa_measure(file) )
        emotionalModule.ec_measure(file)
    return sentiments, emotions

def firstImplementation():
    bots = list()
    threads = list()
    for i in range(0,BOTS_N):
        a = Extractor()
        bots.append(a)
        thread = Thread(target = startBot, args = (a, ))
        threads.append( thread )
    for t in threads:
        t.start()
        t.join()
    for t in threads:
        t.join()
    print("==============================================================================================================")
    repFiles = saveReplies(bots)
    emotionsAndSentiments = analyze(repFiles)
    metrics = analytics.getMetrics( bots )
    #saveMetrics( emotionsAndSentiments[0], emotionsAndSentiments[1], metrics, repFiles )

if __name__ == '__main__':
    a = Extractor()
    while (True):
        a.moti()
        repFiles = saveReplies([a])
        emotionsAndSentiments = analyze(repFiles)
        timeMetric, rulesMetric = analytics.getMetrics( [a] )
        saveMetrics( emotionsAndSentiments[0], emotionsAndSentiments[1], timeMetric, rulesMetric, repFiles )
        a.reset()