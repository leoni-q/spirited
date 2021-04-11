#!/usr/bin/python3
import os

from brownie import Spirited, network, accounts, config

token_id = 0
token_uri_hashes_filename = 'token_uri_hashes_0.txt'


def get_token_uri_hashes():
    with open(f'token_uri_hashes/{token_uri_hashes_filename}') as f:
        return [x.strip() for x in f.readlines()]


def main():
    spirited_contract = Spirited[len(Spirited) - 1]
    print(f'Uploading tokenURIs to {spirited_contract.address}')
    token_uri_hashes = get_token_uri_hashes()
    print(f'got tokenURI hashes {token_uri_hashes}')

    if network.show_active() in ['kovan', 'rinkeby', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        for i, uri_hash in enumerate(token_uri_hashes):
            spirited_contract.addInitialTokenURIHash(token_id, i, uri_hash, {'from': dev})
    else:
        for i, uri_hash in enumerate(token_uri_hashes):
            spirited_contract.addInitialTokenURIHash(token_id, i, uri_hash, {'from': accounts[0]})
