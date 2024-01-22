// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract WoldcoinVirtual {
    string public name = "WoldcoinVirtual";
    string public symbol = "WCV";
    uint256 public totalSupply = 30000000 * 10 ** 3; // 30,000,000 tokens with 3 decimals
    uint8 public decimals = 3;
    
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    
    uint256 public constant transferFee = 1; // 1% fee
    
    uint256 public releaseTime; // Timestamp when tokens can be released
    address public lockContract; // Address of the lock contract
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    constructor() {
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
        
        releaseTime = block.timestamp + 365 days; // Release time set to 365 days from contract deployment
        lockContract = address(0x1234567890123456789012345678901234567890); // Example address of lock contract
    }
    
    function transfer(address _to, uint256 _value) external returns (bool success) {
        uint256 fee = (_value * transferFee) / 1000;
        uint256 valueAfterFee = _value - fee;
        
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += valueAfterFee;
        balanceOf[lockContract] += fee; // Transfer fee to lock contract
        
        emit Transfer(msg.sender, _to, valueAfterFee);
        emit Transfer(msg.sender, lockContract, fee);
        
        return true;
    }
    
    function approve(address _spender, uint256 _value) external returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        
        emit Approval(msg.sender, _spender, _value);
        
        return true;
    }
    
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        uint256 fee = (_value * transferFee) / 1000;
        uint256 valueAfterFee = _value - fee;
        
        balanceOf[_from] -= _value;
        balanceOf[_to] += valueAfterFee;
        balanceOf[lockContract] += fee; // Transfer fee to lock contract
        
        allowance[_from][msg.sender] -= _value;
        
        emit Transfer(_from, _to, valueAfterFee);
        emit Transfer(_from, lockContract, fee);
        
        return true;
    }
    
    // Function to transfer tokens to the lock contract after a certain time has elapsed
    function transferToLockContract() external returns (bool success) {
        require(block.timestamp >= releaseTime, "Tokens cannot be transferred yet");
        uint256 amountToTransfer = (totalSupply * 50) / 100; // 50% of total supply to be transferred to lock contract
        
        balanceOf[msg.sender] -= amountToTransfer;
        balanceOf[lockContract] += amountToTransfer
