from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import gc
from collections import deque

class Extractor(object):


    def __openConnection(self):
        """__openConnection()

        """
        self.__driver = webdriver.Chrome('chromedriver')
        self.__driver.get("https://www.omegle.com")

        self.__conversation = []

        time.sleep(5)
        topics = self.__driver.find_element_by_xpath("//input[contains(@class,'newtopicinput')]")
        topics.send_keys("isis, alkaeda")
        self.__driver.find_element_by_xpath("//img[contains(@id, 'textbtn')]").click()
        time.sleep(5)

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
            print("lol - Aca le pedimos las respuesta al bot :v")

            self.__conversation.append(words)
            self.__conversation.append("Respuesta del bot")
            textarea = self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg')]")
            textarea.send_keys("Esta es la respuesta del bot")
            self.__driver.find_element_by_xpath("//button[contains(@class, 'sendbtn')]").click()
        

    def moti(self):
        self.__openConnection()

    def getConversation(self):
        return self.__conversation
