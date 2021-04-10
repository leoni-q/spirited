#!/usr/bin/python3

import csv

import pytest
from brownie import Spirited, MockV3Aggregator


def get_testdata():
    with open('tests/parametrize_data/change_token_uri_test_data.csv', newline='') as f:
        return [tuple(row) for row in csv.reader(f)]


@pytest.mark.parametrize('btc_price, token_uri', get_testdata())
def test_change_token_uri_depending_on_btc_price(utils, get_account, btc_price, token_uri):
    # given
    mock_price_feed = MockV3Aggregator.deploy(18, btc_price, {'from': get_account})
    spirited = Spirited.deploy(mock_price_feed, utils.get_token_uris(12), {'from': get_account})

    spirited.mintToken(str.encode("token"))

    # when
    spirited.changeTokenURIBasedOnBtcPrice(0)

    # then
    result = spirited.getTokenURI(0)
    assert result.replace('\x00', '') == token_uri
