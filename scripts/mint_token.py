#!/usr/bin/python3
import os

from brownie import Spirited, network, accounts, config


def main():
    spirited_contract = Spirited[len(Spirited) - 1]
    print(f'Minting initial Dynamic Token')

    if network.show_active() in ['kovan', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        spirited_contract.mintToken(str.encode('Dynamic Token'), {'from': dev})
    else:
        spirited_contract.mintToken(str.encode('Dynamic Token'), {'from': accounts[0]})
