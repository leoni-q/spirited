#!/usr/bin/python3

from brownie import Spirited


def test_initialize_with_two_token_uris(get_btc_usd_price_feed_address, get_account, utils):
    # given
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, {'from': get_account})

    # when
    for i, uri in enumerate(utils.get_default_token_uris(2)):
        spirited.addInitialTokenURI(0, i, uri)

    # then
    for n in range(1):
        assert spirited.getInitialTokenURIs(0, n) == f'uri{n}'


def test_initialize_with_seven_token_uris(get_btc_usd_price_feed_address, get_account, utils):
    # given
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, {'from': get_account})

    # when
    for i, uri in enumerate(utils.get_default_token_uris(7)):
        spirited.addInitialTokenURI(0, i, uri)

    # then
    for n in range(7):
        assert spirited.getInitialTokenURIs(0, n) == f'uri{n}'


def test_initialize_with_seven_token_uris_for_second_token(get_btc_usd_price_feed_address, get_account, utils):
    # given
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, {'from': get_account})

    # when
    for i, uri in enumerate(utils.get_default_token_uris(7)):
        spirited.addInitialTokenURI(0, i, uri)
        spirited.addInitialTokenURI(1, i, uri)

    # then
    for n in range(7):
        assert spirited.getInitialTokenURIs(0, n) == f'uri{n}'
    for n in range(7):
        assert spirited.getInitialTokenURIs(1, n) == f'uri{n}'
