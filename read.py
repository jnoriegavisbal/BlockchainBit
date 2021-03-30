# -- coding: utf-8 --

from eth_typing.ethpm import ContractName
from web3 import Web3
import sys 
url = 'https://rinkeby.infura.io/v3/76af675f594e445d8319e35ec983aad7'

abi_contract = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_hash",
				"type": "string"
			}
		],
		"name": "addElement",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_id",
				"type": "uint256"
			}
		],
		"name": "getById",
		"outputs": [
			{
				"internalType": "string",
				"name": "date",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "hash",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

bytecode_contract= "608060405234801561001057600080fd5b5061063e806100206000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063b4fc6d601461003b578063f4f4d23714610057575b600080fd5b61005560048036038101906100509190610372565b610088565b005b610071600480360381019061006c9190610349565b6100e1565b60405161007f92919061042a565b60405180910390f35b8160008085815260200190815260200160002060000190805190602001906100b1929190610229565b508060008085815260200190815260200160002060010190805190602001906100db929190610229565b50505050565b60608060008084815260200190815260200160002060000180546101049061051f565b80601f01602080910402602001604051908101604052809291908181526020018280546101309061051f565b801561017d5780601f106101525761010080835404028352916020019161017d565b820191906000526020600020905b81548152906001019060200180831161016057829003601f168201915b5050505050915060008084815260200190815260200160002060010180546101a49061051f565b80601f01602080910402602001604051908101604052809291908181526020018280546101d09061051f565b801561021d5780601f106101f25761010080835404028352916020019161021d565b820191906000526020600020905b81548152906001019060200180831161020057829003601f168201915b50505050509050915091565b8280546102359061051f565b90600052602060002090601f016020900481019282610257576000855561029e565b82601f1061027057805160ff191683800117855561029e565b8280016001018555821561029e579182015b8281111561029d578251825591602001919060010190610282565b5b5090506102ab91906102af565b5090565b5b808211156102c85760008160009055506001016102b0565b5090565b60006102df6102da84610486565b610461565b9050828152602081018484840111156102f757600080fd5b6103028482856104dd565b509392505050565b600082601f83011261031b57600080fd5b813561032b8482602086016102cc565b91505092915050565b600081359050610343816105f1565b92915050565b60006020828403121561035b57600080fd5b600061036984828501610334565b91505092915050565b60008060006060848603121561038757600080fd5b600061039586828701610334565b935050602084013567ffffffffffffffff8111156103b257600080fd5b6103be8682870161030a565b925050604084013567ffffffffffffffff8111156103db57600080fd5b6103e78682870161030a565b9150509250925092565b60006103fc826104b7565b61040681856104c2565b93506104168185602086016104ec565b61041f816105e0565b840191505092915050565b6000604082019050818103600083015261044481856103f1565b9050818103602083015261045881846103f1565b90509392505050565b600061046b61047c565b90506104778282610551565b919050565b6000604051905090565b600067ffffffffffffffff8211156104a1576104a06105b1565b5b6104aa826105e0565b9050602081019050919050565b600081519050919050565b600082825260208201905092915050565b6000819050919050565b82818337600083830152505050565b60005b8381101561050a5780820151818401526020810190506104ef565b83811115610519576000848401525b50505050565b6000600282049050600182168061053757607f821691505b6020821081141561054b5761054a610582565b5b50919050565b61055a826105e0565b810181811067ffffffffffffffff82111715610579576105786105b1565b5b80604052505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6000601f19601f8301169050919050565b6105fa816104d3565b811461060557600080fd5b5056fea2646970667358221220c0883ba0154af31302aeea2c8c8fca213f3c45f292fbba243f79083170fe2b0264736f6c63430008010033"

account_a = "0xD667e6efC8CefA7e9874708608Ca79d0f33852Ee"
key_a = "040d6a0303227e4a64afed3b4f93f3580aef85f4a1f1d264ff292dd80050f438"
constract_addres= "0x59b65a71bdc2b26c53284287e3a82d1e614db289"

id=sys.argv[1]

web3 = Web3(Web3.HTTPProvider(url))

def read():
    

    address = web3.toChecksumAddress(constract_addres)
    contract = web3.eth.contract(address=address, abi= abi_contract)
    data = contract.functions.getById(int(id)).call()
   
    print(data)

read()