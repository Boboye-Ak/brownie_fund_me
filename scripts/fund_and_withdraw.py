from brownie import FundMe
from scripts.helpful_scripts import get_address, get_Mocks

def fund():
    account=get_address()
    if (len(FundMe)<=0):
        fundMe=FundMe(get_Mocks(), {"from":account})
    else:
        fundMe=FundMe[-1]   
    entrance_fee=fundMe.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("funding...")
    fundMe.fund({"from":account, "value":entrance_fee})     
def withdraw():
    account=get_address()
    if (len(FundMe)<=0):
        fundMe=FundMe(get_Mocks(), {"from":account})
    else:
        fundMe=FundMe[-1]
    fundMe.withdraw({"from":account})
def main():
    fund()
    withdraw()
