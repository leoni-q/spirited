#!/usr/bin/python3

from brownie import Spirited


def test_initialize_with_two_pictures(get_btc_usd_price_feed_address, get_account, utils):
    # given
    token_uris = utils.get_token_uris(2)

    # when
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, token_uris, {'from': get_account})

    # then
    result = spirited.getInitialTokenURIs(0)
    for n in range(1):
        assert bytes.decode(result[n]).replace('\x00', '') == f'uri{n}'


def test_initialize_with_twelve_pictures(get_btc_usd_price_feed_address, get_account, utils):
    # given
    token_uris = utils.get_token_uris(12)

    # when
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, token_uris, {'from': get_account})

    # then
    result = spirited.getInitialTokenURIs(0)
    for n in range(12):
        assert bytes.decode(result[n]).replace('\x00', '') == f'uri{n}'


def test_initialize_with_twenty_four_pictures(get_btc_usd_price_feed_address, get_account, utils):
    # given
    token_uris = utils.get_token_uris(24)

    # when
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, token_uris, {'from': get_account})

    # then
    result_first_array = spirited.getInitialTokenURIs(0)
    for n in range(12):
        assert bytes.decode(result_first_array[n]).replace('\x00', '') == f'uri{n}'

    result_second_array = spirited.getInitialTokenURIs(1)
    for n in range(12):
        assert bytes.decode(result_second_array[n]).replace('\x00', '') == f'uri{n + 12}'
