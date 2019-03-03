from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from collections import deque

import os
import time
import gc
import tensorflow as tf

from settings import PROJECT_ROOT
from ACA.chatbot.botpredictor import BotPredictor

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Extractor(object):


    def __openConnection(self):
        """__openConnection()

        """
        self.__driver = webdriver.Chrome('chromedriver')
        self.__driver.get("https://www.omegle.com")

        self.__conversation = []

        # Setting Topics
        time.sleep(5)
        topics = self.__driver.find_element_by_xpath("//input[contains(@class,'newtopicinput')]")
        topics.send_keys("isis, alkaeda")
        self.__driver.find_element_by_xpath("//img[contains(@id, 'textbtn')]").click()
        time.sleep(5)

        # Start Chatbot Session
        corp_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Corpus')
        knbs_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Variety')
        res_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Result')
        rules_dir = os.path.join(PROJECT_ROOT, 'ACA', 'Data', 'Rules')

        with tf.Session() as sess:
            self.__predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                                 result_dir=res_dir, aiml_dir=rules_dir,
                                 result_file='basic')
            self.__session_id = self.__predictor.session_data.add_session()

        userResponse = False
        while(True):
            try:
                self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg disabled')]")
                break
            except :
                self.response( userResponse )
                time.sleep(2)
        self.__driver.quit()
        
    def response(self, userResponse):
        inputs = self.__driver.find_elements(By.XPATH, "//div[contains(@class, 'logitem')]")
        words = ""
        for i in range( 0, len(inputs) ):
            if ( "Stranger" in inputs[ len(inputs) - i - 1 ] ):
                words = inputs[ len(inputs) - i - 1 ] + " " + words
            else:
                break
        if ( words != "" ):
            # Bot Response

            botResponse = self.__predictor.predict(self.__session_id, words)

            self.__conversation.append(words)
            self.__conversation.append(botResponse)
            textarea = self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg')]")
            textarea.send_keys(botResponse)
            self.__driver.find_element_by_xpath("//button[contains(@class, 'sendbtn')]").click()
        

    def moti(self):
        self.__openConnection()

    def getConversation(self):
        return self.__conversation
