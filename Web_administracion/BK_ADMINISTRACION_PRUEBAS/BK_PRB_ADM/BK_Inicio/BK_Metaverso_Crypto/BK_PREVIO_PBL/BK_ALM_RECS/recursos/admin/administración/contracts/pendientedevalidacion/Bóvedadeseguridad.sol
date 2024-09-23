pragma solidity ^0.8.0;

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract LiquidityPool {
    address public owner;
    address public tokenAddress;
    uint256 public lastSaleTime;
    uint256 public liquidityAmount;
    
    event LiquidityAdded(uint256 amount);
    event LiquidityRemoved(uint256 amount);
    
    constructor(address _tokenAddress) {
        owner = msg.sender;
        tokenAddress = _tokenAddress;
        lastSaleTime = block.timestamp;
        liquidityAmount = 0;
    }
    
    modifier onlyOwner {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }
    
    function addLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance.");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed.");
        liquidityAmount += amount;
        emit LiquidityAdded(amount);
    }
    
    function removeLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        require(liquidityAmount >= amount, "Insufficient liquidity.");
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed.");
        liquidityAmount -= amount;
        emit LiquidityRemoved(amount);
    }
    
    function transferToVault() external onlyOwner {
        require(block.timestamp - lastSaleTime > 3600, "Cannot transfer during sale.");
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, liquidityAmount), "Transfer failed.");
        liquidityAmount = 0;
    }
    
    function receiveTokens() external payable {
        revert("This contract does not accept ETH.");
    }
    
    fallback() external payable {
        revert("This contract does not accept ETH.");
    }
}
