#!/usr/bin/python3

from brownie import Spirited


def test_mint_token_when_initial_token_uri_provided(get_btc_usd_price_feed_address, get_account, utils):
    # given
    token_uri = 'Qmd9MCGtdVz2miNumBHDbvj8bigSgTww'
    spirited = Spirited.deploy(get_btc_usd_price_feed_address, {'from': get_account})
    spirited.addInitialTokenURI(0, 0, token_uri)

    # when
    spirited.mintToken(str.encode("token"))

    # then
    result = spirited.tokenURI(0)
    assert result == token_uri
