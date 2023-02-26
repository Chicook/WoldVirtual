pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    uint256 public constant FEE_PERCENTAGE = 3;
    uint256 public totalFees;

    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    function transfer(address to, uint256 amount) public override returns (bool) {
        uint256 fee = amount.mul(FEE_PERCENTAGE).div(100);
        uint256 amountAfterFee = amount.sub(fee);
        totalFees = totalFees.add(fee);
        _transfer(_msgSender(), to, amountAfterFee);
        _transfer(_msgSender(), address(this), fee);
        return true;
    }

    function getFees() public view returns (uint256) {
        return totalFees;
    }
}
