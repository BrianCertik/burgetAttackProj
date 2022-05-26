#!/usr/bin/python3

from brownie import BrokenToken, NormalToken, accounts


def main():
    bkt = BrokenToken.deploy(1e21, {'from': accounts[0]});
    print("===broken token===");
    print(bkt);
    nmt = NormalToken.deploy(1e21, {'from': accounts[0]});
    print("===normal token===");
    print(nmt);
    return;
