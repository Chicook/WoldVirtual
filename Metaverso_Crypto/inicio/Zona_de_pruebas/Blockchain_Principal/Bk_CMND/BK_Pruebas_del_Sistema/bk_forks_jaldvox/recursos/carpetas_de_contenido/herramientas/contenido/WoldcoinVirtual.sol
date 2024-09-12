// SPDX-License-Identifier: MIT

pragma solidity ^ 0.8.17 ;

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
    string public name = "My Token";
    string public symbol = "MYT";
    uint256 public totalSupply = 30000000; //30 millones de tokens
    uint8 public decimals = 3;
    address public liquidityAddress = address(0x123); //direccion de la cuenta
 de contrato inteligente que mantendra la liquidez //

    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;

    constructor() {
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 transferAmount = amount - (amount * 3 / 100); //deducir el 3% de comisiones
        require(transferAmount > 0, "La cantidad a transferir es demasiado pequeña.");
        require(recipient != address(0), "La dirección del destinatario es 0x0.");
        require(_balances[msg.sender] >= amount, "Saldo insuficiente.");
        _balances[msg.sender] -= amount;
        _balances[recipient] += transferAmount;
        _balances[liquidityAddress] += amount - transferAmount; //agregar las comisiones al saldo
   de la direccion de liquidez//
        emit Transfer(msg.sender, recipient, transferAmount);
        emit Transfer(msg.sender, liquidityAddress, amount - transferAmount);
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
        uint256 transferAmount = amount - (amount * 3 / 100); //deducir el 3% de comisiones
        require(transferAmount > 0, "La cantidad a transferir es demasiado pequeña.");
        require(recipient != address(0
