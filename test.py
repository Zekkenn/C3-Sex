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
        self.__driver = webdriver.Chrome('C:/Users/2106457/Documents/omegleBot/chromedriver')
        self.__driver.get("https://www.omegle.com")
        time.sleep(5)
        topics = self.__driver.find_element_by_xpath("//input[contains(@class,'newtopicinput')]")
        topics.send_keys("anime, games")
        self.__driver.find_element_by_xpath("//img[contains(@id, 'textbtn')]").click()
        time.sleep(5)
        while(True):
            try:
                man = self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg disabled')]")
                break
            except :
                self.TareaDePrimi()
                textarea = self.__driver.find_element_by_xpath("//textarea[contains(@class,'chatmsg')]")
                textarea.send_keys("Hello")
                self.__driver.find_element_by_xpath("//button[contains(@class, 'sendbtn')]").click()
                time.sleep(2)
        print("salio")
        #self.__driver.quit()
        
    def TareaDePrimi(self):
        inputs = self.__driver.find_elements(By.XPATH, "//div[contains(@class, 'logitem')]/p[contains(@class, 'strangermsg')]")
        for i in inputs:
            print(i.text)
        

    def moti(self):
        self.__openConnection()

a = Extractor()
a.moti()