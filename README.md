# Multipurporse ERC20 token flow tracking

This script is useful to do on-chain anaylsis of an ERC20 token (typically before choosing to invest) to identify historical token flow. 

The functions available in this script : 
1. *dest_flow* - Destination Flow : Takes a wallet address, contract address (ERC20), and returns the destination wallets of which all the tokens that have been received (including their sum). 
- Useful to identify wallets of investors and team members, to see how much has been vested so far, and whether the tokens have been sold (sent to CEX's / DEX's) or not. 

2. *recent_moves* - Recent Movements : Takes one (or many) wallet address(es), contract address (ERC20), number of days before, and returns any transactions that has happened in those wallets in the time period. 
- Useful to identify if there has been recent transactions, due to recent news, token unlocks, etc. 


### Notes on reading Covalent API ERC20 Transaction Logs : 
1. Each item in 'items' is a unique transaction hash that the address has been involved in. 
2. Each log in item is a transfer that has occurred. An item (transaction hash) can contain multiple transfers. 
3. Logic flow : 
3.1 For each log in each item, check "sender_address" if it matches contract address that is being looked for.  
3.2 If yes, for each log, under decoded : params : value to get from address, to address, and value. 


Miscellaneous : 
For further analysis, might be able to categories the Methods (under 'log_events' : 'decoded' : 'name') of each Transaction better, to read through less transactions. For example, for bulk transactions, each item usually involves just one type of token. 
