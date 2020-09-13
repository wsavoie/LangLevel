import asyncio as aio
import json
import numpy as np
import pandas as pd
import requests

import config


async def get_meaning(dictionary, word, progress_bar):
    data = requests.get(config.JISHO_URL.format(word)).json()['data'][0]

    reading = data['japanese'][0]['reading']
    meanings = [x['english_definitions'][:4] for x in data['senses']]
    meanings = '; '.join(meanings[0])
    dictionary[word] = {'reading': reading, 'meanings': meanings}

    progress_bar.increment()


async def GetAllDFMeanings(meanings,DF):
    
    words=DF['V'].to_list()
    progress_bar = config.ProgressBar(len(words))
    coroutines = [get_meaning(meanings, word, progress_bar) for word in words]
    await aio.wait(coroutines)

def toVRTform(DF):
    DF['R']=DF['V'].map(lambda x: meanings[x]['reading'])
    DF['T']=DF['V'].map(lambda x: meanings[x]['meanings'])
    return DF
