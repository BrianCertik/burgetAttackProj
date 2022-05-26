#!/usr/bin/python3

from brownie import BrokenToken, NormalToken, PancakePair, config, network, interface, accounts

def main():
    bktAddr = BrokenToken[len(BrokenToken)-1]; # the latest one
    nmtAddr = NormalToken[len(NormalToken)-1]; # the latest one

    pancakeFactory = interface.IPancakeFactory(config["networks"][network.show_active()]["pancake_factory"])
    tx = pancakeFactory.createPair(bktAddr, nmtAddr, {"from": accounts[0]});
    pairAddr = pancakeFactory.getPair(bktAddr, nmtAddr);
    testPancakePair = interface.IPancakePair(pairAddr);

    print(testPancakePair.name());
    print(testPancakePair.symbol());
    print(testPancakePair.totalSupply());

    # pancakePair = interface.IPancakePair(config["networks"][network.show_active()]["pancake_pair"]);

    return;