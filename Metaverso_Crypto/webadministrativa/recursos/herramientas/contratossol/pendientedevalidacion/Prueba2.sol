// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    address private constant _poolAddress = 0x123...; // Replace with the pool address
    uint256 private constant _lockRatio = 50; // Lock 50% of collected fees
    uint256 private _lockedBalance;
    uint256 private _lastLockedTimestamp;

    constructor() ERC20("MyToken", "MTK") {
        _mint(msg.sender, 100000000 * 10 ** decimals());
    }

    function collectFee(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        _lockedBalance += (amount * _lockRatio) / 100;
        uint256 transferAmount = amount - ((amount * _lockRatio) / 100);
        super.transferFrom(msg.sender, _poolAddress, transferAmount);
    }

    function unlockFee() external {
        require(_lockedBalance > 0, "No locked balance");
        require(block.timestamp - _lastLockedTimestamp >= 1 days, "Must wait at least one day");

        uint256 unlockAmount = (_lockedBalance * 100) / _lockRatio;
        _lockedBalance = 0;
        _lastLockedTimestamp = block.timestamp;
        super.transfer(_poolAddress, unlockAmount);
    }
}
