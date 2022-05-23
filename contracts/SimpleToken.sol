pragma solidity ^0.6.0;

import "OpenZeppelin/openzeppelin-contracts@3.0.0/contracts/token/ERC20/ERC20Burnable.sol";

contract SimpleToken is ERC20Burnable {
    constructor(uint256 initialSupply) ERC20 ("Simple Token", "SPT") public {
        _mint(msg.sender, initialSupply);
    }
}