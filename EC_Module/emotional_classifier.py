# ===================== SEND AND SAVE EC PREDICTIONS ======================

import subprocess
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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
