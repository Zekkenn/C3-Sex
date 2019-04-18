# ===================== SEND AND SAVE EC PREDICTIONS ======================

import subprocess
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SEMEVAL_NEGEMOTS = ['anger','disgust','fear','sadness']

def ec_measure(replies_file):
    # Define command and R script location
    command = 'Rscript'
    path2script = ROOT_DIR + '\ec_predictor.R'

    # Set the arguments for the script, user replies file
    args = replies_file

    # Build subprocess command
    cmd = command + ' ' + path2script + ' ' + args
    print(cmd)

    # Run the subprocess command
    subprocess.call(cmd, shell=True)

    # Emotional analysis
    emots = list()
    with open(replies_file.replace(".txt","_EC.txt"), 'r') as resultFile:
        for row in resultFile.readlines():
            emot = row.strip("\n").split(",")[1]
            if (emot in SEMEVAL_NEGEMOTS):
                emots.append(0)
            else:
                emots.append(1)
    return emots
            
