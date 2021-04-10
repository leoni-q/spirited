#!/usr/bin/python3

from brownie import Spirited


def test_initialize_with_two_token_uri_hashes(get_btc_usd_price_feed_address, get_account, utils):
    # given
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, {'from': get_account})

    # when
    for i, uri_hash in enumerate(utils.get_default_token_uri_hashes(2)):
        spirited.addInitialTokenURIHash(0, i, uri_hash)

    # then
    for n in range(1):
        assert spirited.getInitialTokenURIHash(0, n) == f'uri_hash{n}'


def test_initialize_with_seven_token_uri_hashes(get_btc_usd_price_feed_address, get_account, utils):
    # given
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, {'from': get_account})

    # when
    for i, uri_hash in enumerate(utils.get_default_token_uri_hashes(7)):
        spirited.addInitialTokenURIHash(0, i, uri_hash)

    # then
    for n in range(7):
        assert spirited.getInitialTokenURIHash(0, n) == f'uri_hash{n}'


def test_initialize_with_seven_token_uri_hashes_for_second_token(get_btc_usd_price_feed_address, get_account, utils):
    # given
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, {'from': get_account})

    # when
    for i, uri_hash in enumerate(utils.get_default_token_uri_hashes(7)):
        spirited.addInitialTokenURIHash(0, i, uri_hash)
        spirited.addInitialTokenURIHash(1, i, uri_hash)

    # then
    for n in range(7):
        assert spirited.getInitialTokenURIHash(0, n) == f'uri_hash{n}'
    for n in range(7):
        assert spirited.getInitialTokenURIHash(1, n) == f'uri_hash{n}'
