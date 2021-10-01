from brownie import accounts, SimpleStorage


def test_deploy():
    account = accounts[0]

    simple_storage = SimpleStorage.deploy({"from": account})
    storage_value = simple_storage.retrieve()
    expected = 0

    assert expected == storage_value


def test_store():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    expected = 15
    transaction = simple_storage.store(expected, {"from": account})

    assert expected == simple_storage.retrieve()
