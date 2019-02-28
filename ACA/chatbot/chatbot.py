#!/usr/bin/python3
import os
import aiml
import threading
import time

from queue import Queue
from main import *

BRAIN_FILE="brain.dump"

def retrieval_model():
    # This code checks if a dump exists and
    # otherwise loads the aiml from the xml files
    # and saves the brain dump.
    k = aiml.Kernel()
    if os.path.exists(BRAIN_FILE):
        print("Loading from brain file: " + BRAIN_FILE)
        k.loadBrain(BRAIN_FILE)
    else:
        print("Parsing aiml files")
        k.bootstrap(learnFiles=os.path.abspath("rules/tot-startup.aiml"), commands="load aiml b")
        print("Saving brain file: " + BRAIN_FILE)
        k.saveBrain(BRAIN_FILE)
    return(k)

def generative_model(cv, inf_inputs):
    # This code loads the seq2seq model
    run_generative(cv, inf_inputs)

def inference_input():
    # Endless loop which passes the input to the bot and prints
    # its response
    k = retrieval_model()
    condition = threading.Condition()
    inputs_queue = Queue()
    generative_session = threading.Thread(target=generative_model, args=(condition,inputs_queue,))
    generative_session.start()
    time.sleep(15)
    
    while True:
        input_text = input("> ")
        # TRY RETRIEVAL RESPONSE
        response = k.respond(input_text)
        used_model = "(retrieval_response)"
        if (response == "Sorry. I didn't quite get that."):
            # POST CAN BE ANSWER BY RETRIVAL MODEL
            # GENERATIVE RESPONSE
            used_model = "(generative_response)"
            inputs_queue.put(input_text)
            try:
                with condition:
                    condition.notifyAll()
                    condition.wait()
                    response = ' '.join(inputs_queue.get())
            except KeyError:
                response = "Unknown token. Please try again!"
        print(" >>", response, used_model)

def main():
    inference_input()

if __name__ == '__main__':
    main()
    
    



