// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    address private constant _poolAddress = 0x123...; // Replace with the pool address
    uint256 private constant _lockRatio = 50; // Lock 50% of collected fees
    uint256 private _lockedBalance;
    uint256 private _lastLockedTimestamp;
    uint256 private _totalStaked;
    mapping(address => uint256) private _stakes;
    mapping(address => uint256) private _lastRewardClaim;

    uint256 private constant _rewardRate = 100; // 100 tokens per day
    uint256 private constant _rewardInterval = 1 days;

    function collectFee(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        _lockedBalance += (amount * _lockRatio) / 100;
        uint256 transferAmount = amount - ((amount * _lockRatio) / 100);
        super.transferFrom(msg.sender, _poolAddress, transferAmount);

        // Update user stake
        _stakes[msg.sender] += transferAmount;
        _totalStaked += transferAmount;
        _lastRewardClaim[msg.sender] = block.timestamp;
    }

    function unlockFee() external {
        require(_lockedBalance > 0, "No locked balance");
        require(block.timestamp - _lastLockedTimestamp >= 1 days, "Must wait at least one day");

        uint256 unlockAmount = (_lockedBalance * 100) / _lockRatio;
        _lockedBalance = 0;
        _lastLockedTimestamp = block.timestamp;
        super.transfer(_poolAddress, unlockAmount);
    }

    function claimReward() external {
        require(_stakes[msg.sender] > 0, "No stake to claim reward");
        require(block.timestamp - _lastRewardClaim[msg.sender] >= _rewardInterval, "Must wait for reward interval");

        uint256 reward = (_stakes[msg.sender] * (_rewardRate * _rewardInterval)) / _totalStaked;
        _lastRewardClaim[msg.sender] = block.timestamp;
        super.transfer(msg.sender, reward);
    }

    function getPoolBalance() external view returns (uint256) {
        return balanceOf(_poolAddress);
    }

    function checkMinimumRewards() external view returns (bool) {
        uint256 totalRewards = (_totalStaked * (_rewardRate * _rewardInterval)) / _totalStaked;
        uint256 poolBalance = balanceOf(_poolAddress);
        return (poolBalance >= (totalRewards * 2)); // Check if the pool balance is at least twice the total rewards
    }
}
