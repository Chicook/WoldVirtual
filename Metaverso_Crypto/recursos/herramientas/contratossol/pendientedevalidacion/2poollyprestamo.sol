// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

interface ERC20 {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address who) external view returns (uint256);
}

contract LiquidityPool {
    address public tokenAddress;
    ERC20 public token;
    uint256 public totalLiquidity;
    mapping(address => uint256) public liquidity;
    mapping(address => uint256) public debt;
    uint256 public feePercentage;
    address[] public investors;

    event AddLiquidity(address indexed investor, uint256 amount);
    event RemoveLiquidity(address indexed investor, uint256 amount);
    event Borrow(address indexed borrower, uint256 amount);
    event Repay(address indexed borrower, uint256 amount);
    event FeePaid(address indexed borrower, uint256 amount);

    constructor(address _tokenAddress, uint256 _feePercentage) {
        tokenAddress = _tokenAddress;
        token = ERC20(_tokenAddress);
        feePercentage = _feePercentage;
    }

    function addLiquidity(uint256 amount) external {
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        liquidity[msg.sender] += amount;
        totalLiquidity += amount;
        if (!isInvestor(msg.sender)) {
            investors.push(msg.sender);
        }
        emit AddLiquidity(msg.sender, amount);
    }

    function removeLiquidity(uint256 amount) external {
        require(liquidity[msg.sender] >= amount, "Insufficient liquidity");
        uint256 fee = calculateFee(amount);
        uint256 amountMinusFee = amount - fee;
        require(token.transfer(msg.sender, amountMinusFee), "Transfer failed");
        liquidity[msg.sender] -= amount;
        totalLiquidity -= amount;
        if (liquidity[msg.sender] == 0) {
            removeInvestor(msg.sender);
        }
        emit RemoveLiquidity(msg.sender, amount);
        emit FeePaid(address(this), fee);
    }

    function borrow(uint256 amount) external {
        require(amount <= availableLiquidity(), "Insufficient liquidity");
        uint256 fee = calculateFee(amount);
        uint256 amountMinusFee = amount - fee;
        require(token.transfer(msg.sender, amountMinusFee), "Transfer failed");
        debt[msg.sender] += amountMinusFee;
        emit Borrow(msg.sender, amountMinusFee);
        emit FeePaid(address(this), fee);
    }

    function repay(uint256 amount) external {
        require(debt[msg.sender] >= amount, "Insufficient debt");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        debt[msg.sender] -= amount;
        emit Repay(msg.sender, amount);
    }

    function availableLiquidity() public view returns (uint256) {
        return token.balanceOf(address(this)) - totalLiquidity;
    }

    function calculateFee(uint256 amount) public view returns (uint256) {
        return amount * feePercentage / 100;
    }

    function isInvestor(address investor) public view returns (bool) {
        for (uint256 i = 0; i < investors.length; i++) {
            if (investors[i] == investor) {
                return true;
            }
        }
        return false;
    }

    function removeInvestor(address investor) internal {
        for (uint256 i = 0; i < investors.length; i++) {
            if (investors[i] == investor) {
                investors[i] = investors[investors.length - 1];
                investors.pop();
                return;
            }
        }
   
