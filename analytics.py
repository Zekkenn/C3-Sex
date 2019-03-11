import os
import time
import gc
import math

class Analyze(object):


    def __openConnection(self):
        """__openConnection()

        """

        self.__conversation = []

        self.__currentLength = 0

        # Setting Topics
        time.sleep(5)
        topics = self.__driver.find_element_by_xpath("//input[contains(@class,'newtopicinput')]")
        topics.send_keys("games")
        self.__driver.find_element_by_xpath("//img[contains(@id, 'textbtn')]").click()
        time.sleep(5)
        first = True ; first_time = 0

    def calculate(self, time):
        return 2/(1 + math.exp( time / 10 ) )
