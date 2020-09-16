

import requests
import json
import pandas as pd
import numpy as np
from preferences import p

WKAUTHHEAD={'Authorization': f'Bearer {p["wk_api_key"]}'}
WK_URL=r"https://api.wanikani.com/v2/{0}"


def getWKLevel():
    
    response = requests.request("GET", WK_URL.format('user'), headers={**WKAUTHHEAD} , data = {})
    print('sc=',response.status_code)
    rc = response.status_code
    wklevel=json.loads(response.text)['data']['level']
    if(rc is not 200): #200 is correct code,  will return 401 is problematic APIKEY
        pass
        #TODO error action here
    return wklevel

def getWKData(wklevel):
    
    #create string of 1 to wanikani level
    lvlString=str([i for i in range(1,wklevel+1)]).strip('[]').replace(' ', '')
    wkData= pd.DataFrame()
    nexturl=WK_URL.format('subjects')
    while(nexturl):
        response=requests.request("GET",url=nexturl,headers = {**WKAUTHHEAD}, 
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

# ********************************
# **** duolingo stuff
# ********************************
def importFromDuolingo():
    pass
    #TODO import words from duolingo


