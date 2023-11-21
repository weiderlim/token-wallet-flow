from helper_func.api_calls import get_all_token_txns
import json 

if __name__ == '__main__' : 
    json_object = get_all_token_txns('eth-mainnet', '0xb23d80f5FefcDDaa212212F028021B41DEd428CF', '0x1c0a684a45C8AEc7C6Bd6Da94bfaED044EC2Fd88')
    
    # json_formatted = json.dumps(json_object, indent=2)

    # with open ("sample.json", "w") as output : 
    #     output.write(json_formatted)


