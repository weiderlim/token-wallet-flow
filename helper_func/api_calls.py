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
    if response.status_code != 200:
        return {"error": response.status_code}
    
    json_object = json.loads(response.text) 

    data = json_object['data']

    if data['links']['next'] == None : 
        end_trig = 1
    else : 
        end_trig = 0

    # json_formatted = json.dumps(json_object, indent=2)

    # with open ("sample.json", "w") as output : 
    #     output.write(json_formatted)

    return data, end_trig


def get_all_token_txns (chain_name, contract_add, wallet_add) : 
    load_dotenv() 

    end_trig = 0
    curr_page = 0
    df_index = 0 

    columns = ['tx_hash', 'from', 'to', 'value']
    df = pd.DataFrame(columns=columns)

    while end_trig == 0 :
        data, end_trig = call_token_txns(chain_name, wallet_add, curr_page)

        for item in data['items'] : 
            for log in item['log_events'] :
                # standardising all to lower case for comparison 
                if log['sender_address'].lower() == contract_add.lower() : 
                    df.loc[df_index, 'tx_hash'] = log['tx_hash']
                    for param in log['decoded']['params'] :                         
                        if param['name'] == 'from' : 
                            df.loc[df_index, 'from'] = param['value']
                        elif param['name'] == 'to' : 
                            df.loc[df_index, 'to'] = param['value']
                        elif param['name'] == 'value' : 
                            df.loc[df_index, 'value'] = int(param['value']) / (10 ** 18) 
                    
                    df_index += 1
        
        curr_page += 1 
        end_trig = 1

    df.to_csv('output.csv')

    return df



    



