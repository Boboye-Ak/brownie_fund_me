from brownie import FundMe,MockV3Aggregator, accounts, network, config
from scripts.helpful_scripts import get_address, get_Mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3



def deploy_fund_me():
    account=get_address()
    price_feed_address=get_Mocks()

    fund_me=FundMe.deploy(price_feed_address,{"from":account}, publish_source=config["networks"][network.show_active()]["verify"])
    print(f"contract deployed successfully to {fund_me.address}")

def main():
    deploy_fund_me()
