from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from collections import deque

import os
import time
import gc
import tensorflow as tf
import SA_Module.sentimentAnalysis as sentimentModule
import analytics as analize

from settings import PROJECT_ROOT
from ACA.chatbot.botpredictor import BotPredictor

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Extractor(object):


    def __openConnection(self):
        """__openConnection()

        """

        # Start Chatbot Session
        corp_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Corpus')
        knbs_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Variety')
        res_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Result')
        rules_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Rules')

        self.__driver = webdriver.Chrome('chromedriver')
        self.__driver.get("https://www.omegle.com")

        self.__conversation = []
        self.__lenConversation = []
        self.__timeResponse = []
        self.__currentLength = 0
        self.__timeOfConversation = 0

        # Setting Topics
        time.sleep(5)
        topics = self.__driver.find_element_by_xpath("//input[contains(@class,'newtopicinput')]")
        topics.send_keys("games")
        self.__driver.find_element_by_xpath("//img[contains(@id, 'textbtn')]").click()
        time.sleep(5)
        first = True ; first_time = 0
        self.__sess = tf.Session()
        self.__predictor = BotPredictor(self.__sess, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                                 result_dir=res_dir, aiml_dir=rules_dir,
                                 result_file='basic')
        self.__session_id = self.__predictor.session_data.add_session()
        self.__initTimeUserResponse = 0
        userResponse = False
        while(True):
            try:
                self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg disabled')]")
                # Analize Data - Conversation Ended
                self.__timeOfConversation = time.clock() - first_time
                print("=================================================SALIO==============================================")
                break
            except :
                self.response( userResponse )
                if (first):
                    first_time = time.clock()
                    first = False
            time.sleep(2)
        #self.__driver.quit()
        
    def response(self, userResponse):
        inputs = self.__driver.find_elements(By.XPATH, "//div[contains(@class, 'logitem')]/p[contains(@class, 'msg')]")
        words = ""
        if ( self.__currentLength < len(inputs) ):
            self.__currentLength = len(inputs)

            for i in range( 0, len(inputs) ):
                if ( "Stranger" in inputs[ len(inputs) - i - 1 ].text ):
                    words = inputs[ len(inputs) - i - 1 ].text[9:] + " " + words
                else:
                    break

            self.__initTimeUserResponse = 0

        if ( words != "" ):
            # Bot Response
            self.__finalTimeUserResponse = time.clock()
            botResponse = self.__predictor.predict(self.__session_id, words.lower(), len(self.__conversation))
            if ( botResponse.strip() != "" and botResponse != None ): 
                self.__currentLength += 1
                self.__conversation.append(words)
                self.__lenConversation.append( len(words) )
                self.__timeResponse.append( self.__finalTimeUserResponse - self.__initTimeUserResponse )
                textarea = self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg')]")
                textarea.send_keys(botResponse)
                self.__driver.find_element_by_xpath("//button[contains(@class, 'sendbtn')]").click()
            
        elif ( self.__currentLength == 0 ): 
            textarea = self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg')]")
            textarea.send_keys("Hi")
            self.__driver.find_element_by_xpath("//button[contains(@class, 'sendbtn')]").click()
            self.__currentLength += 1
            self.__finalTimeUserResponse = time.clock()

    def moti(self):
        self.__openConnection()

    def getConversation(self):
        return self.__conversation

    def getTimeOfConversation(self):
        return self.__timeOfConversation

    def getTimeEachResponse(self):
        return self.__timeResponse 

    def getNumberRulesMatched(self):
        return self.__predictor.getNumberMatchedRules()

    def getLenEachPost(self):
        return self.__lenConversation

    def getNumberOfInteractions(self):
        return len(self.__conversation)