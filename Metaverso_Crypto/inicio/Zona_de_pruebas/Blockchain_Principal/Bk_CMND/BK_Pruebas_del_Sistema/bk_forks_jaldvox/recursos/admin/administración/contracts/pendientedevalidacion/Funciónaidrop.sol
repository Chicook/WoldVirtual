// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

interface IBEP20 {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address who) external view returns (uint256);
    function decimals() external view returns (uint8);
}

contract WoldcoinVirtualPreSale {
    address public tokenAddress;
    address public owner;
    uint256 public totalTokens;
    uint256 public tokensSold;
    uint256 public price;
    uint256 public startDate;
    uint256 public endDate;
    uint256 public minPurchase;
    uint256 public maxPurchase;
    bool public isPresaleOpen;

    mapping(address => uint256) public balances;

    event Buy(address indexed buyer, uint256 tokens);

    constructor(address _tokenAddress, uint256 _totalTokens, uint256 _price, uint256 _startDate, uint256 _endDate, uint256 _minPurchase, uint256 _maxPurchase) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalTokens > 0, "Invalid total tokens");
        require(_price > 0, "Invalid price");
        require(_startDate > 0 && _startDate < _endDate, "Invalid dates");
        require(_minPurchase > 0 && _maxPurchase > 0 && _minPurchase <= _maxPurchase, "Invalid purchase limits");

        tokenAddress = _tokenAddress;
        owner = msg.sender;
        totalTokens = _totalTokens;
        price = _price;
        startDate = _startDate;
        endDate = _endDate;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        isPresaleOpen = false;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    function startPresale() public onlyOwner {
        require(!isPresaleOpen, "Presale is already open.");
        require(IBEP20(tokenAddress).balanceOf(address(this)) >= totalTokens, "Insufficient token balance for presale.");

        isPresaleOpen = true;
    }

    function endPresale() public onlyOwner {
        require(isPresaleOpen, "Presale is not open.");

        isPresaleOpen = false;

        // Calculate remaining tokens in contract after deducting the aidrop
        uint256 remainingTokens = IBEP20(tokenAddress).balanceOf(address(this)) - 2000000 * 10**3;

        // If any remaining tokens, transfer to owner
        if (remainingTokens > 0) {
            IBEP20(tokenAddress).transfer(owner, remainingTokens);
        }
    }

    function buyTokens() public payable {
        require(isPresaleOpen, "Presale is not open.");
        require(block.timestamp >= startDate && block.timestamp <= endDate, "Invalid purchase time.");
        require(msg.value >= minPurchase && msg.value <= maxPurchase, "Invalid purchase amount.");

        uint256 tokensToBuy = msg.value * price;

        require(tokensToBuy <= (totalTokens - tokensSold), "Insufficient tokens for sale.");

        balances[msg.sender] += tokensToBuy;
        tokensSold += tokensToBuy;

        emit Buy(msg.sender, tokensToBuy);
    }

    function claimAidrop() public {
        require(!isPresaleOpen, "Presale is still open.");
        require(balances[msg.sender] > 0, "No tokens to claim.");

        uint256 tokensToClaim = balances[msg.sender] * 2 / 100; // 2% of tokens bought in presale
        balances[msg.sender] =
