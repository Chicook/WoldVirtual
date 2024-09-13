pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/utils/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/security/Pausable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol";

contract StakingContract is Ownable, Pausable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 startTimestamp;
        uint256 endTimestamp;
        bool isActive;
    }

    mapping (address => Stake) public stakes;

    IERC20 public token;
    uint256 public minimumStakeAmount;
    uint256 public stakingPeriod;

    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event StakingPeriodChanged(uint256 newStakingPeriod);

    constructor(address _token, uint256 _minimumStakeAmount, uint256 _stakingPeriod) {
        token = IERC20(_token);
        minimumStakeAmount = _minimumStakeAmount;
        stakingPeriod = _stakingPeriod;
    }

    function stake(uint256 _amount) external whenNotPaused {
        require(_amount >= minimumStakeAmount, "Amount is below the minimum stake amount");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= _amount, "Insufficient token allowance");

        // Only allow staking if user doesn't already have an active stake
        require(!stakes[msg.sender].isActive, "Already an active stake");

        // Add staked amount to user's stake
        stakes[msg.sender].amount = _amount;

        // Set start timestamp to current block timestamp
        stakes[msg.sender].startTimestamp = block.timestamp;

        // Set end timestamp to current block timestamp plus staking period
        stakes[msg.sender].endTimestamp = block.timestamp.add(stakingPeriod);

        // Mark stake as active
        stakes[msg.sender].isActive = true;

        // Transfer staked tokens from user to contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    function unstake() external whenNotPaused {
        require(stakes[msg.sender].isActive, "No active stake");

        // Check that staking period has ended
        require(block.timestamp >= stakes[msg.sender].endTimestamp, "Staking period has not ended");

        // Check that contract has enough tokens to fulfill unstake request
        require(token.balanceOf(address(this)) >= stakes[msg.sender].amount, "Insufficient contract balance");

        // Transfer staked tokens from contract to user
        token.safeTransfer(msg.sender, stakes[msg.sender].amount);

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTimestamp = 0;
        stakes[msg.sender].endTimestamp = 0;
        stakes[msg.sender].isActive = false;

        emit Unstaked(msg.sender, stakes[msg.sender].amount);
    }

    function setStakingPeriod(uint256 _stakingPeriod) external onlyOwner {
        stakingPeriod = _stakingPeriod;
        emit StakingPeriodChanged
