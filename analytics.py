import os
import time
import gc
import math
import statistics 

def calculate(time, expected):
    return 2/(1 + math.exp( (-time) / (expected/2) ) )

def getTimeMetric(bot):
    medianTime = (statistics.median( bot.getTimeEachResponse() )/60)
    finalTime = (bot.getTimeOfConversation()/60)
    medianLen = statistics.median( bot.getLenEachPost() )/150
    return calculate( medianTime, medianLen ) * calculate( finalTime, 5 )

def timeConversationMetric(bots):
    metrics = []
    for bot in bots:
        metrics.append( getTimeMetric(bot) )
    return metrics

def rulesConversationMetric(bots):
    metrics = []
    for bot in bots:
        metrics.append( bot.getNumberRulesMatched() / bot.getNumberOfInteractions() )
    return metrics

#def recognizedSentiments(bots):
#    metrics = []
#    for bot in bots:
#        metrics.append( "" )
#    return metrics

def getMetrics(bots):
    timeByConversationMetric = timeConversationMetric(bots)
    rulesByConversationMetric = rulesConversationMetric(bots)
    #recognizedSentimentsMetric = recognizedSentiments(bots)
    return [ timeByConversationMetric, rulesByConversationMetric ]