
from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS=8
STARTING_PRICE=200000000000

LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENT=["mainnet-fork"]

def get_address():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENT):
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])

def get_Mocks():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
        if (len(MockV3Aggregator)<=0):
            mock_aggregator=MockV3Aggregator.deploy(DECIMALS , STARTING_PRICE , {"from":get_address()})

        mock_aggregator=MockV3Aggregator[-1]
        price_feed_address=mock_aggregator.address
    else:
        price_feed_address=config["networks"][network.show_active()]["eth_usd_price_feed"]
    return price_feed_address
