from web3 import Web3
from solcx import compile_source
import json
import os

# Web3 setup (use your Infura endpoint or other Ethereum node provider)
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection
if not w3.isConnected():
    print("Error: Failed to connect to Ethereum network.")
    exit()

# Load your wallet private key (never share this key)
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
account = w3.eth.account.privateKeyToAccount(PRIVATE_KEY)

# Load Solidity source code
with open("ERC20Token.sol", "r") as file:
    contract_source_code = file.read()

# Compile the contract
compiled_sol = compile_source(contract_source_code)
contract_id, contract_interface = compiled_sol.popitem()

# Contract ABI and Bytecode
contract_abi = contract_interface['abi']
contract_bytecode = contract_interface['bin']

# Prepare the contract deployment
ERC20Token = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

# Set up transaction details
nonce = w3.eth.getTransactionCount(account.address)
gas_price = w3.eth.gas_price

# Deploy contract with an initial supply of 1,000,000 tokens (adjust to your needs)
initial_supply = 1000000
transaction = ERC20Token.constructor(initial_supply).buildTransaction({
    'chainId': 1,  # Mainnet
    'gas': 2000000,
    'gasPrice': gas_price,
    'nonce': nonce,
})

# Sign the transaction
signed_tx = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

# Send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(f"Contract deployment transaction sent. Hash: {tx_hash.hex()}")

# Wait for the transaction to be mined
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print(f"Contract deployed at address: {tx_receipt.contractAddress}")
