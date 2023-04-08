pragma solidity ^0.8.0;

contract CryptoTrading {
    address owner;
    uint256 fee = 10; // fee en base 10000 (0.1%)
    mapping(address => mapping(string => uint256)) balances; // balances[tokenAddress][userAddress]
    mapping(string => address) tokenAddresses;
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }
    
    function setFee(uint256 newFee) public onlyOwner {
        require(newFee <= 1000, "Fee cannot exceed 10%");
        fee = newFee;
    }
    
    function addToken(string memory symbol, address tokenAddress) public onlyOwner {
        tokenAddresses[symbol] = tokenAddress;
    }
    
    function getBalance(string memory symbol, address user) public view returns (uint256) {
        address tokenAddress = tokenAddresses[symbol];
        require(tokenAddress != address(0), "Token not supported");
        return balances[user][symbol];
    }
    
    function deposit(string memory symbol, uint256 amount) public {
        address tokenAddress = tokenAddresses[symbol];
        require(tokenAddress != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        balances[msg.sender][symbol] += amount;
    }
    
    function withdraw(string memory symbol, uint256 amount) public {
        address tokenAddress = tokenAddresses[symbol];
        require(tokenAddress != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender][symbol] >= amount, "Insufficient balance");
        balances[msg.sender][symbol] -= amount;
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Token transfer failed");
    }
    
    function trade(string memory symbolSell, uint256 amountSell, string memory symbolBuy, uint256 amountBuy) public {
        address tokenAddressSell = tokenAddresses[symbolSell];
        address tokenAddressBuy = tokenAddresses[symbolBuy];
        require(tokenAddressSell != address(0) && tokenAddressBuy != address(0), "Tokens not supported");
        require(amountSell > 0 && amountBuy > 0, "Amounts must be greater than 0");
        require(balances[msg.sender][symbolSell] >= amountSell, "Insufficient balance");
        require(IERC20(tokenAddressSell).allowance(msg.sender, address(this)) >= amountSell, "Token allowance too low");
        uint256 feeAmount = amountSell * fee / 10000;
        uint256 amountSellMinusFee = amountSell - feeAmount;
        require(IERC20(tokenAddressSell).transferFrom(msg.sender, address(this), amountSell), "Token transfer failed");
        require(IERC20(tokenAddressBuy).transfer(msg.sender, amountBuy), "Token transfer failed");
        balances[msg.sender][symbolSell] -= amountSell;
        balances[msg.sender][symbolBuy] += amountBuy;
        balances[owner][symbolSell] += feeAmount;
    }
}

interface IERC20 {
    function transfer(address to, uint256 value) external returns (bool);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
