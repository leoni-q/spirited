#!/usr/bin/python3
import os

from brownie import Spirited, network, accounts, config


def main():
    spirited_contract = Spirited[len(Spirited) - 1]
    print(f'Reading actual token uri set to token')

    if network.show_active() in ['kovan', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        print(spirited_contract.tokenURI(0, {'from': dev}))
    else:
        print(spirited_contract.tokenURI(0, {'from': accounts[0]}))
