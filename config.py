import os
import sys


import json
import numpy as np
import pandas as pd
import requests



APIKEY='a39c68f1-81cd-44c6-8a0c-09c4b226f005'
WKAUTHHEAD={f'Authorization': f'Bearer {APIKEY}'}

WK_URL=r"https://api.wanikani.com/v2/{0}"
JISHO_URL='https://jisho.org/api/v1/search/words?keyword={0}'
DBDIR=r'C:\Users\WS\AppData\Roaming\Anki2\main\dbs\{0}'


class ProgressBar:
    def __init__(self, high, size=50):
        self.high = high
        self.value = 0
        self.size = size

    def __str__(self):
        s = "|"
        s += ((20 * self.value) // self.high) * "█"
        s += ((20 * (self.high - self.value)) // self.high) * " "
        s += "|"
        s += " {}%".format(round(100 * self.value / self.high, 2))

        return s

    def increment(self):
        self.value += 1
        sys.stdout.write("\r{}".format(str(self)))
        sys.stdout.flush()