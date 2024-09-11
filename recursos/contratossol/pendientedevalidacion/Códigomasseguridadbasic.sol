// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IBEP20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract Token is IBEP20 {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 3;
    uint256 public override totalSupply;
    uint256 public tokensLocked;
    uint256 private _totalSupply;
    uint256 private _tokensLocked;
    address public owner;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    struct Stake {
        uint256 amount;
        uint256 unlockTime;
    }

    mapping(address => Stake[]) public stakes;
    mapping(address => uint256) public stakingBalance;
    mapping(address => uint256) public lastClaim;

    uint256 public stakingRewards = 0;
    uint256 public stakingRewardsPaid = 0;
    uint256 public rewardsDuration = 365 days;
    uint256 public lastRewardTime = block.timestamp;

    uint256 public salesProgramPercentage = 25;
    address public salesProgramWallet;

    address public internalPool;

    constructor(uint256 initialSupply, address _salesProgramWallet) {
        totalSupply = initialSupply * 10 ** decimals;
        _balances[msg.sender] = totalSupply;
        owner = msg.sender;
        salesProgramWallet = _salesProgramWallet;
        internalPool = address(this);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function setInternalPool(address pool) external onlyOwner {
        internalPool = pool;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender
