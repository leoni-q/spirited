#!/usr/bin/python3
import os

from brownie import Spirited, network, accounts, config


def main():
    spirited_contract = Spirited[len(Spirited) - 1]
    print(f'Changing tokenURIs based on btc price')

    if network.show_active() in ['kovan', 'rinkeby', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        spirited_contract.changeTokenURIBasedOnBtcPrice(0, {'from': dev})
    else:
        spirited_contract.changeTokenURIBasedOnBtcPrice(0, {'from': accounts[0]})
