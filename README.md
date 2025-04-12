# Simple ERC-20 Token

## Overview

This project contains a simple implementation of an **ERC-20 token** on the Ethereum blockchain. The token is named `SimpleToken` with the symbol `STK`, and it includes all essential features of an ERC-20 token, such as:

- `transfer`: Sending tokens to another address.
- `approve` and `transferFrom`: Delegated transfers using the allowance mechanism.
- `totalSupply` and `balanceOf`: Keeping track of the total supply and user balances.

Additionally, this project includes a Python script (`deploy.py`) for deploying the ERC-20 contract to the Ethereum blockchain using Web3.py.

## Requirements

- Python 3.x
- Web3.py library:
  ```bash
  pip install web3
