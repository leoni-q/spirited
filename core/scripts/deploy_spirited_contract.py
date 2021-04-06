#!/usr/bin/python3
import os
from brownie import Spirited, network, accounts, config


def main():
    if network.show_active() in ['kovan', 'mainnet']:
        dev = accounts.add(os.getenv(config['wallets']['from_key']))
        return Spirited.deploy(config['networks'][network.show_active()]['btc_usd_price_feed'], {'from': dev})
    else:
        return Spirited.deploy("", {'from': accounts[0]})
