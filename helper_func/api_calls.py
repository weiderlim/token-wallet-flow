import requests 
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os
import json
import pandas as pd 

def call_token_txns (chain_name, wallet_add, page_num) : 
    
    url = "https://api.covalenthq.com/v1/{}/address/{}/transactions_v3/page/{}/?".format(chain_name, wallet_add, page_num)

    headers = {
        "accept": "application/json"
    }
    
    basic = HTTPBasicAuth(os.environ.get('COVALENT_API_KEY'), '')

    response = requests.get(url, headers=headers, auth=basic)

    # Handle the response and return data as needed.
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code}
    
    # convert (usually response is in non JSON form) to json object first 
    json_object = json.loads(response.text) 


    print(json_object, end_trig)
    
    if json_object['links']['next'] == None : 
        end_trig = 1
    else : 
        end_trig = 0

     

    return json_object, end_trig


def get_all_token_txns (chain_name, contract_add, wallet_add) : 
    load_dotenv() 

    end_trig = 0
    curr_page = 0

    columns = ['from', 'to', 'value']
    df = pd.DataFrame(columns=columns)

    while end_trig == 0 :
        json_object, end_trig = call_token_txns(chain_name, wallet_add, curr_page)

        for item in json_object['items'] : 
            for log in item['log_events'] :
                if log['sender_address'] == contract_add : 
                    for param in log['decoded']['params'] : 
                        if param['name'] == 'from' : 
                            df.loc[len(df), 'from'] = param['value']
                        elif param['name'] == 'to' : 
                            df.loc[len(df), 'to'] = param['value']
                        elif param['name'] == 'value' : 
                            df.loc[len(df), 'value'] = int(param['value']) 
        
        curr_page += 1 

    return df



    



