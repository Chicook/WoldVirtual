pragma solidity ^0.8.0;

import "./IERC20.sol";

contract PoolFarming {
    address public owner;
    IERC20 public token;
    IERC20 public bnbToken;
    uint256 public totalLPTokens;
    uint256 public totalRewards;
    uint256 public bnbSellThreshold;
    uint256 public lpSellPercentage;
    uint256 public lpSellFeePercentage;
    uint256 public rewardsPercentage;
    uint256 public rewardsFeePercentage;

    mapping(address => uint256) public lpBalances;
    mapping(address => uint256) public rewardsBalances;

    event LPTokensAdded(address indexed user, uint256 amount);
    event LPTokensRemoved(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _token, IERC20 _bnbToken) {
        owner = msg.sender;
        token = _token;
        bnbToken = _bnbToken;
        totalLPTokens = 0;
        totalRewards = 0;
        bnbSellThreshold = 1000000000000000000; // 1 BNB
        lpSellPercentage = 25; // 25%
        lpSellFeePercentage = 3; // 3%
        rewardsPercentage = 75; // 75%
        rewardsFeePercentage = 25; // 2.5%
    }

    function addLPTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(token.allowance(msg.sender, address(this)) >= amount, "Must approve LP tokens first");

        token.transferFrom(msg.sender, address(this), amount);
        lpBalances[msg.sender] += amount;
        totalLPTokens += amount;

        emit LPTokensAdded(msg.sender, amount);
    }

    function removeLPTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(lpBalances[msg.sender] >= amount, "Insufficient LP tokens");

        lpBalances[msg.sender] -= amount;
        totalLPTokens -= amount;

        token.transfer(msg.sender, amount);

        emit LPTokensRemoved(msg.sender, amount);
    }

    function claimRewards() public {
        uint256 rewards = rewardsBalances[msg.sender];
        require(rewards > 0, "No rewards to claim");

        rewardsBalances[msg.sender] = 0;
        totalRewards -= rewards;

        token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    function deposit() public {
        require(lpBalances[msg.sender] > 0, "No LP tokens to deposit");

        uint256 bnbBalance = bnbToken.balanceOf(address(this));

        if (bnbBalance >= bnbSellThreshold) {
            uint256 sellAmount = (bnbBalance * lpSellPercentage) / 100;

            bnbToken.transfer(owner, sellAmount);

            uint256 feeAmount = (sellAmount * lpSellFeePercentage) / 100;

            totalLPTokens -= feeAmount;

            uint256 rewardsAmount = (sellAmount * rewardsPercentage) / 100;
            uint256 rewardsFee = (rewardsAmount * rewardsFeePercentage) / 100;

            rewardsBalances[owner] += rewardsFee;
            totalRewards += rewardsAmount - rewardsFee;

            emit LPTokensRemoved(owner, feeAmount);
        }
    }
}
