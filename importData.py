import json

import numpy as np
import pandas as pd
import requests

from preferences import p

#https://docs.python.org/2.5/whatsnew/pep-343.html
#write a wanikani context manager?
WKAUTHHEAD={f'Authorization' : f'Bearer {p["DEFAULT"]["wk_api_key"]}'}
WK_URL=r"https://api.wanikani.com/v2/{0}"


def processWKResponse(response):
    # 200 	Success 	n/a
    # 401 	Unauthorized 	“Unauthorized. Nice try.”
    # 403 	Forbidden 	
    # 404 	Not Found 	
    # 422 	Unprocessable Entity 	Description of how the request was malformed.
    # 429 	Too Many Requests 	
    # 500 	Internal Server Error 	n/a
    # 503 	Service Unavailable 	n/a
    
    # https://stackoverflow.com/questions/2052390/manually-raising-throwing-an-exception-in-python
    rc=response.status()
    rc=200
    if rc is 200:
        return response
    elif rc == 401: #key error
        return response.raise_for_status()
    return

def getWKLevel():
    
    response = requests.request("GET", WK_URL.format('user'), headers={**WKAUTHHEAD} , data = {})
    try:
        response.raise_for_status()
    except Exception as e:
        print(e)
        return
    wklevel=json.loads(response.text)['data']['level']
    return wklevel

def getWKData(wklevel):
    #TODO implement caching 
    #  conditional requests, which lets us quickly tell you that a record hasn't changed since you got it last.
    #  The second is to give you tools to get only the updated or new records after any point in time,
    #  letting you easily refresh your local data caches and stores without having to parse all the records. 
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
    # wkData.set_index(0,inplace=True)
    # print(wkData)
    # wkData.to_csv(DBDIR.format('wanikaniVocab.txt'))
    return wkData   
    
# ********************************
# **** duolingo stuff
# ********************************
def importFromDuolingo():
    pass
    #TODO import words from duolingo
