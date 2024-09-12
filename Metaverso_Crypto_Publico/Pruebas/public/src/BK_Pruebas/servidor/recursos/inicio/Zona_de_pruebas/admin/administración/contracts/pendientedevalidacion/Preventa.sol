// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC20 {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

contract WoldcoinVirtual {
    string public constant name = "WoldcoinVirtual";
    string public constant symbol = "WLCV";
    uint8 public constant decimals = 3;
    uint256 public constant initialSupply = 30_000_000 * 10 ** uint256(decimals);
    uint256 public totalSupply;
    uint256 public soldTokens;
    uint256 public constant poolPercent = 50; // 50% of totalSupply
    uint256 public constant transferPercent = 25; // 25% of received tokens to be automatically sold and added to liquidity pool
    uint256 public constant poolWithdrawalPeriod = 365 days;
    uint256 public poolWithdrawalStartTime;
    uint256 public poolWithdrawalLastTimeWithdrawn;

    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowed;

    address payable public owner;

    address public liquidityPool;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor() {
        owner = payable(msg.sender);
        totalSupply = initialSupply;
        balances[owner] = totalSupply / 2;
        soldTokens = totalSupply / 2;
        liquidityPool = address(this);
    }

    function() external payable {
        require(msg.value > 0, "Invalid ETH amount");
        uint256 tokensToTransfer = calculateTokens(msg.value);
        require(soldTokens + tokensToTransfer <= totalSupply, "Not enough tokens left to sell");
        balances[msg.sender] += tokensToTransfer;
        soldTokens += tokensToTransfer;
        owner.transfer(msg.value);
        emit Transfer(address(0), msg.sender, tokensToTransfer);
    }

    function calculateTokens(uint256 weiAmount) private pure returns (uint256) {
        return weiAmount * 1000; // 1 BTCB = 1000 WLCV
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);

        // Automatically sell and add 25% of received tokens to liquidity pool
        uint256 transferAmount = _value * transferPercent / 100;
        if (transferAmount > 0) {
            require(IERC20(liquidityPool).balanceOf(address(this)) >= transferAmount, "Insufficient liquidity pool balance");
            IERC20(liquidityPool).transfer(msg.sender, transferAmount);
            uint256 liquidityPoolAmount = transferAmount / 2;
            IERC20(liquidityPool).transfer(owner, liquidityPoolAmount);
            IERC20(liquidityPool).transfer(address(this), liquidityPoolAmount);
        }

        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool) {
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256) {
        return allowed[_owner][_spender];
   
