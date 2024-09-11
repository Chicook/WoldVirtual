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

contract MyToken is IBEP20 {
    string public constant name = "My Token";
    string public constant symbol = "MTK";
    uint8 public constant decimals = 3;
    uint256 private constant _totalSupply = 1000000 * 10 ** decimals;
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;
    uint256 public constant feePercentage = 3; // 3% fee on transfers
    address public owner;

    constructor() {
        _balances[msg.sender] = _totalSupply;
        owner = msg.sender;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = (amount * feePercentage) / 100;
        _balances[msg.sender] -= amount;
        _balances[recipient] += (amount - fee);
        _balances[owner] += fee;
        emit Transfer(msg.sender, recipient, amount);
        emit Transfer(msg.sender, owner, fee);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = (amount * feePercentage) / 100;
        _balances[sender] -= amount;
        _balances[recipient] += (amount - fee);
        _balances[owner] += fee;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        emit Transfer(sender, owner, fee);
        return true;
    }
}
