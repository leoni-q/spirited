#!/usr/bin/python3
import os

import pytest
from brownie import network, MockV3Aggregator, accounts, config


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass


@pytest.fixture
def get_btc_usd_price_feed_address():
    if network.show_active() == 'development':
        mock_price_feed = MockV3Aggregator.deploy(
            18, 2000, {'from': accounts[0]})
        return mock_price_feed.address
    if network.show_active() in config['networks']:
        return config['networks'][network.show_active()]['btc_usd_price_feed']
    else:
        pytest.skip('Invalid network specified ')
        return


@pytest.fixture(scope="module")
def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    if network.show_active() in config['networks']:
        dev_account = accounts.add(os.getenv(config['wallets']['from_key']))
        return dev_account
    else:
        pytest.skip('Invalid network/wallet specified ')


@pytest.fixture(scope="module")
def spirited(Spirited):
    return Spirited.deploy("btc_usd_price_feed_address", {'from': accounts[0]})
