
import requests
import json
import pandas as pd
import numpy as np

import config

def getWKLevel():
    response = requests.request("GET", config.WK_URL.format('user'), headers={**config.WKAUTHHEAD} , data = {})
    wklevel=json.loads(response.text)['data']['level']
    return wklevel

def getWKData(wklevel):
    
    #create string of 1 to wanikani level
    lvlString=str([i for i in range(1,wklevel+1)]).strip('[]').replace(' ', '')
    wkData= pd.DataFrame()
    nexturl=config.WK_URL.format('subjects')
    while(nexturl):
        response=requests.request("GET",url=nexturl,headers = {**config.WKAUTHHEAD}, 
                          params={'types':'vocabulary',
                                  'levels':lvlString})
        resp=json.loads(response.text)

        wkData=wkData.append(
            pd.DataFrame(
                [i['data']['slug'] for i in resp['data'] 
                 if resp['data'][0]['data']['spaced_repetition_system_id']>0]
            )
        )
        nexturl=resp['pages']['next_url']
    wkData.set_index(0,inplace=True)
    return wkData   