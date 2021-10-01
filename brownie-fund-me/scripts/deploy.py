from brownie import accounts, config, FundMe
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from":account})
    print(fund_me)

def main():
    deploy_fund_me()
