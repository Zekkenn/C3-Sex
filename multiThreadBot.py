from test import Extractor
from threading import Thread
import sentimentAnalysis

def startBot( bot ):
    bot.moti()

def main():
    bots = list();
    threads = list();
    for i in range(0,1):
        a = Extractor()
        bots.append(a)
        thread = Thread(target = startBot, args = (a, ))
        threads.append( thread )
        thread.start()
main()