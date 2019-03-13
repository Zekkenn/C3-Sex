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
        
def analyze( repFiles ):
    for file in repFiles:
        # Sentiment Analysis
        sentimentModule.sa_measure(file)
        emotionalModule.ec_measure(file)

def main():
    bots = list()
    threads = list()
    for i in range(0,BOTS_N):
        a = Extractor()
        bots.append(a)
        thread = Thread(target = startBot, args = (a, ))
        threads.append( thread )
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    repFiles = saveReplies(bots)
    analyze(repFiles)
    print(analytics.getMetrics( bots ))
main()
