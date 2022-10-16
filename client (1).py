import json
from web3 import Web3
import asyncio
import time
#connecting to ganache
url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url))

address = web3.toChecksumAddress("0x28db6CdEea735aFe2E6503c205902BB92E5be3EE")



abi = json.loads('''
	[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "ipfsId",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "encrypted_key",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "public_key",
				"type": "string"
			}
		],
		"name": "notify_grant",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "ipfsId",
				"type": "string"
			}
		],
		"name": "add_information",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "companies",
		"outputs": [
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "public_key",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "set",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "public_key",
				"type": "string"
			}
		],
		"name": "create_company",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			}
		],
		"name": "create_user",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "company_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "encrypted_key",
				"type": "string"
			}
		],
		"name": "grant_access",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "list_companies",
		"outputs": [
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "public_key",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "set",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"name": "list_data_index_based",
		"outputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "ipfsId",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "list_data_ipfs_based",
		"outputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "ipfsId",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "my_emit",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "number_of_authentication_data",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "users",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "owner",
						"type": "address"
					},
					{
						"internalType": "string",
						"name": "ipfsId",
						"type": "string"
					}
				],
				"internalType": "struct VDSIG.authentication_data",
				"name": "data",
				"type": "tuple"
			},
			{
				"internalType": "string",
				"name": "email",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "password",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "set",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]''')

# def handle_event(event):
#     print(Web3.toJSON(event))
# async def log_loop(event_filter, poll_interval):
#     while True:
#         for PairCreated in event_filter.get_all_entries():
#             handle_event(PairCreated)
#         await asyncio.sleep(poll_interval)

contract = web3.eth.contract(address=address, abi=abi)

# Create user function
web3.eth.default_account = web3.eth.accounts[0]
tx_hash = contract.functions.create_user("kasra.research@gmail.com","12345").transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

#Create company function
web3.eth.default_account = web3.eth.accounts[1]
tx_hash = contract.functions.create_company("comany@gmail.com","company a","123","my_public_key").transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

#Add data to IPFS 
web3.eth.default_account = web3.eth.accounts[0]
tx_hash = contract.functions.add_information("IPFS DATA").transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

#Grant ACCESS
web3.eth.default_account = web3.eth.accounts[0]
tx_hash = contract.functions.grant_access("company a","Encrypted key").transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

#Listen for "notify_grant" event
# loop = asyncio.get_event_loop()

# event_filter = contract.events.notify_grant().createFilter(fromBlock='latest')
# # print(event_filter.get_all_entries())
# try:
#     loop.run_until_complete(
#         asyncio.gather(
#             log_loop(event_filter, 2)))
#             # log_loop(block_filter, 2),
#             # log_loop(tx_filter, 2)))
# finally:
#     # close loop to free up system resources
#     loop.close()

# print(web3.get_balance(me))
# print(contract)