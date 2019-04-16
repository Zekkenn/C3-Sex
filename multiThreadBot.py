from test import Extractor as omegleExtractor
from telegram import Extractor as telegramExtractor
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
                for i in response:
                    try:
                        file.write(i)
                    except:
                        print("fail")
                file.write("\n")
    return(files)
        
def saveMetrics( emotions, sentiments, timeMetric, rulesMetric, files ):
    fileName = PROJECT_ROOT + "\\UsersReplies\\" + str(datetime.datetime.now()).replace(":","_").replace("-","_").replace(" ","_").replace(".","_") + "_ALLMETRICS" + ".txt"
    with open(fileName + "_Metrics.txt", 'w+') as file:
        file.write("Negative Sentiments; Positive Sentiments; Neutral Sentiments; Time Metric; Rules Triggered Metric\n")
        for i in range( len(files) ):
            suma = emotions[i][0] + emotions[i][1] + emotions[i][2]
            suma = 1 if suma == 0 else suma
            file.write( str(emotions[i][0]/suma) + ";" + str(emotions[i][1]/suma) + ";" + str(emotions[i][2]/suma) + ";" + str( timeMetric[i] ) + ";" + str( rulesMetric[i] ) + "\n")
            

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
        a = omegleExtractor()
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
    omegle = omegleExtractor()
    telegram = telegramExtractor()
    telegram.moti()
    while (True):
        omegle.moti()
        # TELEGRAM NOTIFICATION
        # omegle.getTradeAccomplish() # Trade Accomplish to notify telegram
        # End of telegram conversation
        # Get telegram user replies
        repFiles = saveReplies([omegle,telegram]) # Save omegle and telegram replies
        emotionsAndSentiments = analyze(repFiles)
        timeMetric, rulesMetric = analytics.getMetrics( [omegle,telegram] )
        saveMetrics( emotionsAndSentiments[0], emotionsAndSentiments[1], timeMetric, rulesMetric, repFiles )
        # OMEGLE NOTIFICATION
        omegle.reset()
