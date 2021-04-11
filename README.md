## About
Dynamic NFT Application, that allows users to convert pieces of art into dynamic tokens stored on chain

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already. Here is a simple way to install brownie.

```bash
pip install eth-brownie
```

2. [Install ganache-cli](https://www.npmjs.com/package/ganache-cli)

```bash
npm install -g ganache-cli
```

1. Set your `WEB3_INFURA_PROJECT_ID`, and `PRIVATE_KEY` [environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). You can get this by getting a free trial of [Infura](https://infura.io/). At the moment, it does need to be infura. You can find your `PRIVATE_KEY` from your ethereum wallet like [metamask](https://metamask.io/). 

Otherwise, you can build, test, and deploy on your local environment.

## Deploy a contract
```bash
brownie run scripts/deploy-spirited_contract.py --network rinkeby
```

## TokenURI hashes
The project stores available hashes of the art-works deployed to ipfs in a directory `token_uri_hashes`
For example, this is an url indicating a picture from ipfs: "https://ipfs.io/ipfs/QmaSED9ZSbdGts5UZqueFJjrJ4oHH3GnmGJdSDrkzpYqRS".
The last part after "/" is the hash which needs to be stored on the contract. Right now contract supports dynamic changes
of pictures based on btc price in the following order:
```
btcPrice < 50_000 = 1 hash
btcPrice >= 50_000 && btcPrice < 60_000 = 2 hash
btcPrice >= 60_000 && btcPrice < 70_000 = 3 hash
btcPrice >= 70_000 && btcPrice < 80_000 = 4 hash
btcPrice >= 80_000 && btcPrice < 90_000 = 5 hash
btcPrice >= 90_000 && btcPrice < 100_000 = 6 hash
btcPrice >= 100_000 = 7 hash
```
Therefore each file in `token_uri_hashes`  directory should contain 7 hashes.

## Upload tokenURI hashes to contract
In order to upload tokenURI hashes you can use script:
```bash
brownie run scripts/upload_token_uri_hashes.py --network rinkeby
```
Script contains two variables which you may want to change:<br/> 
`token_id` - identifier of a token, which will be linked with provided tokenURIs<br/>
`token_uri_hashes_filename` - file containing hashes<br/>

## Mint a token
```bash
brownie run scripts/mint_token.py --network rinkeby
```
After minting token is linked to the first tokenURI hash, no matter what the Bitcoin is.

## Change tokenURI
```bash
brownie run scripts/change_token_uri.py --network rinkeby
```
script variable:<br/>
`token_id` - identifier of a token which tokenURI will be changed depend on a Bitcoin price at the moment 

## License

This project is licensed under the [MIT license](LICENSE).
