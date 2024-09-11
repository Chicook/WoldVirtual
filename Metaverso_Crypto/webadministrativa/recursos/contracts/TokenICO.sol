pragma solidity ^0.8.24;

contract TokenICO {
    address public owner;
    uint public totalTokens;
    uint public tokensSold;
    mapping(address => uint) public balances;

    event TokenPurchased(address buyer, uint amount, uint totalTokensSold);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    constructor(uint _totalTokens) {
        owner = msg.sender;
        totalTokens = _totalTokens;
    }

    function purchaseTokens(uint _amount) external payable {
        require(tokensSold + _amount <= totalTokens, "Not enough tokens available");
        require(msg.value == _amount * 1 ether, "Incorrect Ether amount");

        balances[msg.sender] += _amount;
        tokensSold += _amount;

        emit TokenPurchased(msg.sender, _amount, tokensSold);
    }

    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
