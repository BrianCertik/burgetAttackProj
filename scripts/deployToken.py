#!/usr/bin/python3

from brownie import BrokenToken, NormalToken, PancakePair, accounts


def main():
    bkt = BrokenToken.deploy(1e21, {'from': accounts[0]});
    nmt = NormalToken.deploy(1e21, {'from': accounts[0]});
    return;
