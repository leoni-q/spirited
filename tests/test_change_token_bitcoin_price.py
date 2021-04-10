#!/usr/bin/python3

import csv

import pytest
from brownie import Spirited, MockV3Aggregator


def get_testdata():
    with open('tests/parametrize_data/change_token_uri_test_data.csv', newline='') as f:
        return [tuple(row) for row in csv.reader(f)]


@pytest.mark.parametrize('btc_price, token_uri_hash', get_testdata())
def test_change_token_uri_depending_on_btc_price(utils, get_account, btc_price, token_uri_hash):
    # given
    mock_price_feed = MockV3Aggregator.deploy(18, btc_price, {'from': get_account})
    spirited = Spirited.deploy(mock_price_feed, {'from': get_account})
    for i, uri_hash in enumerate(utils.get_default_token_uri_hashes(7)):
        spirited.addInitialTokenURIHash(0, i, uri_hash)
    spirited.mintToken(str.encode("token"))

    # when
    spirited.changeTokenURIBasedOnBtcPrice(0)

    # then
    result = spirited.tokenURI(0)
    assert result == utils.ipfs_url + token_uri_hash
