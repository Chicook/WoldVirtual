// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v4.4/contracts/token/ERC20/ERC20.sol";

contract WoldcoinVirtual is ERC20 {
    address public owner;
    address public internalPool;
    uint256 public internalPoolAmount = 15000000 * 10 ** 3;
    uint256 public liquidityPoolAmount = 5000000 * 10 ** 3;
    uint256 public price = 0.0005 ether;
    uint256 public maxTokensToSell = 10000000 * 10 ** 3;
    uint256 public soldTokens;
    uint256 public tokensToRelease = 1000000 * 10 ** 3;
    uint256 public releaseDate = block.timestamp + 365 days;

    constructor() ERC20("WoldcoinVirtual", "WLCV") {
        _mint(msg.sender, 30000000 * 10 ** 3);
        owner = msg.sender;
    }
    
    function buyTokens() external payable {
        require(soldTokens < maxTokensToSell, "All tokens sold");
        require(msg.value >= price, "Insufficient ether sent");
        
        uint256 amount = msg.value / price;
        
        if (soldTokens + amount > maxTokensToSell) {
            amount = maxTokensToSell - soldTokens;
        }
        
        soldTokens += amount;
        
        if (soldTokens == maxTokensToSell) {
            // Transfer tokens to liquidity pool
            _transfer(owner, internalPool, internalPoolAmount);
            _transfer(owner, address(this), liquidityPoolAmount);
            _approve(address(this), owner, liquidityPoolAmount);
            _transfer(owner, address(this), liquidityPoolAmount);
            // Set price to 0 to prevent further purchases
            price = 0;
        }
        
        _transfer(owner, msg.sender, amount);
    }

    function releaseTokens() external {
        require(block.timestamp >= releaseDate, "Release date not reached yet");
        require(tokensToRelease > 0, "All tokens released");
        
        _transfer(owner, internalPool, tokensToRelease);
        tokensToRelease = 0;
    }
    
    function setPrice(uint256 _price) external {
        require(msg.sender == owner, "Only the owner can set the price");
        price = _price;
    }
    
    function withdraw(uint256 _amount) external {
        require(msg.sender == owner, "Only the owner can withdraw funds");
        require(address(this).balance >= _amount, "Insufficient balance");
        payable(owner).transfer(_amount);
    }
    
    function setInternalPool(address _internalPool) external {
        require(msg.sender == owner, "Only the owner can set the internal pool address");
        internalPool = _internalPool;
    }
    
    function setInternalPoolAmount(uint256 _internalPoolAmount) external {
        require(msg.sender == owner, "Only the owner can set the internal pool amount");
        internalPoolAmount = _internalPoolAmount;
    }
    
    function setReleaseDate(uint256 _releaseDate) external {
        require(msg.sender == owner, "Only the owner can set the release date");
        require(_releaseDate > block.timestamp, "Release date must be in the future");
        releaseDate = _releaseDate;
    }
    
    function setTokensToRelease(uint256 _tokensToRelease) external {
        require(msg.sender == owner, "Only the owner can set the tokens to release");
        tokensToRelease = _tokensToRelease;
