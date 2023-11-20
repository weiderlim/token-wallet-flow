# Function tracking ERC20 token flow from a wallet address

Anyone who wants to do some on-chain anaylsis of an ERC20 token (typically before choosing to invest) can use this function to better identify historical token flow. 

This function takes the wallet address, contract address (ERC20), and returns the destination wallets of which all the tokens that have been received (including their sum). 

This functions is part of the analysis of the wallets of investors and team members, to see how much has been vested so far, and whether the tokens have been sold or not. 

How to read Covalent API ERC20 Transaction Logs : 
1. Each item in 'items' is a unique transaction hash that the address has been involved in. 
2. Each log in item is a transfer that has occurred. An item (transaction hash) can contain multiple transfers. 
3. Logic flow : 
3.1 For each log in each item, check "sender_address" if it matches contract address that is being looked for.  
3.2 If yes, for each log, under decoded : params : value to get from address, to address, and value. 


Miscellaneous : 
For further analysis, might be able to categories the Methods (under 'log_events' : 'decoded' : 'name') of each Transaction better, to read through less transactions. For example, for bulk transactions, each item usually involves just one type of token. 
