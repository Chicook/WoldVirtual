// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v4.5/contracts/token/ERC20/IERC20.sol";

contract Staking {
    // Token being staked
    IERC20 private token;
    // Address of staker
    address public staker;
    // Total amount staked
    uint256 public totalStaked;
    // Mapping of user staked amounts
    mapping(address => uint256) public stakedBalance;
    // Staking period
    uint256 public stakingPeriod;
    // Start of staking period
    uint256 public stakingStart;
    // End of staking period
    uint256 public stakingEnd;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);

    constructor(address _token, uint256 _stakingPeriod) {
        token = IERC20(_token);
        staker = msg.sender;
        stakingPeriod = _stakingPeriod;
    }

    // Stake tokens
    function stakeTokens(uint256 _amount) external {
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        stakedBalance[msg.sender] += _amount;
        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    // Withdraw staked tokens
    function withdrawStake() external {
        require(block.timestamp > stakingEnd, "Staking period has not ended yet");
        uint256 amount = stakedBalance[msg.sender];
        stakedBalance[msg.sender] = 0;
        totalStaked -= amount;
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    // Start staking period
    function startStakingPeriod() external {
        require(msg.sender == staker, "Only staker can start staking period");
        stakingStart = block.timestamp;
        stakingEnd = block.timestamp + stakingPeriod;
    }
}
