
import subprocess
import json


class PDF:

    def __init__(self):
        pass

    def get_text(self):
        import os
        print(os.getcwd())
        args = ['python2', './lib/miner.py']
        subprocess.call(args)

        with open('./lib/output.json', 'r') as f:
            text = json.load(f)
            return text