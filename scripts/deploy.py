from brownie import DataFeeds, config, network, MockV3Aggregator
from scripts.helpful_scripts import get_account
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    deploy_mocks,
)


def deploy():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    data_feeds = DataFeeds.deploy(price_feed_address, {"from": account})
    current_price = data_feeds.getLatestPrice()
    print(f"el prcio actual es {current_price}")


def main():
    deploy()
