#!/usr/bin/python3
import os

from brownie import Spirited, MockV3Aggregator, network, accounts, config


def main():
    if network.show_active() in ['kovan', 'rinkeby', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        return Spirited.deploy(config['networks'][network.show_active()]['btc_usd_price_feed'], {'from': dev})
    else:
        mock_price_feed = MockV3Aggregator.deploy(18, 50_000_000_000_00, {'from': accounts[0]})
        return Spirited.deploy(mock_price_feed.address, {'from': accounts[0]})
