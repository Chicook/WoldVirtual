pragma solidity ^0.8.0;

contract Bridge {
    address public owner;
    uint256 public fee = 10; // 0.001%

    mapping(address => bool) public allowedTokens;

    event Transfer(address indexed token, address indexed fromChain, address indexed toChain, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Bridge: Only the owner can perform this action");
        _;
    }

    function setFee(uint256 _fee) external onlyOwner {
        require(_fee <= 100, "Bridge: Fee cannot exceed 10%");
        fee = _fee;
    }

    function allowToken(address token) external onlyOwner {
        allowedTokens[token] = true;
    }

    function revokeToken(address token) external onlyOwner {
        allowedTokens[token] = false;
    }

    function transfer(address token, address toChain, uint256 amount) external {
        require(allowedTokens[token], "Bridge: Token not allowed");
        require(amount > 0, "Bridge: Amount must be greater than zero");

        uint256 totalFee = (amount * fee) / 10000;
        uint256 transferAmount = amount - totalFee;

        // Transfer tokens to the destination chain
        // (omitted for brevity)

        emit Transfer(token, msg.sender, toChain, transferAmount);
    }
}
