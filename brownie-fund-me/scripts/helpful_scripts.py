from brownie import accounts, network, config
def get_account():
    if network.active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])