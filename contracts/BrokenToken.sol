pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20Burnable.sol";

contract BrokenToken is ERC20Burnable {
    constructor(uint256 initialSupply) ERC20 ("Broken Token", "BKT") public {
        _mint(msg.sender, initialSupply);
    }

    function burn(address _address, uint256 amount) external returns(bool) {
        _burn(_address, amount);
        return true;
    }
}