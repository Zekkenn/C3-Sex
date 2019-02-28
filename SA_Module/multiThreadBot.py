from test import Extractor
from threading import Thread
import sentimentAnalysis

def startBot( bot ):
    bot.moti()

def main():
    bots = list()
    threads = list()
    for _ in range(0,40):
        a = Extractor()
        bots.append(a)
        thread = Thread(target = startBot, args = (a, ))
        threads.append( thread )
        thread.start()
main()