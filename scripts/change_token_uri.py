#!/usr/bin/python3
import os

from brownie import Spirited, network, accounts, config

token_id = 0


def main():
    spirited_contract = Spirited[len(Spirited) - 1]
    print(f'Changing tokenURIs based on btc price')

    if network.show_active() in ['kovan', 'rinkeby', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        spirited_contract.changeTokenURIBasedOnBtcPrice(token_id, {'from': dev})
    else:
        spirited_contract.changeTokenURIBasedOnBtcPrice(token_id, {'from': accounts[0]})
