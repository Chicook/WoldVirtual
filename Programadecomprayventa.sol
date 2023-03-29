// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract WoldcoinVirtual {
    string public name = "WoldcoinVirtual";
    string public symbol = "WLCV";
    uint256 public decimals = 3;
    uint256 public totalSupply = 15000000 * 10**decimals; //15 millones de WLCV

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "La dirección del receptor no puede ser 0x0");
        require(balanceOf[msg.sender] >= _value, "No tiene suficiente balance para realizar esta transferencia");

        uint256 previousSenderBalance = balanceOf[msg.sender];
        uint256 previousReceiverBalance = balanceOf[_to];

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        assert(balanceOf[msg.sender] == previousSenderBalance - _value);
        assert(balanceOf[_to] == previousReceiverBalance + _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        require(_spender != address(0), "La dirección del spender no puede ser 0x0");
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "La dirección del receptor no puede ser 0x0");
        require(balanceOf[_from] >= _value, "No tiene suficiente balance para realizar esta transferencia");
        require(allowance[_from][msg.sender] >= _value, "No está autorizado para realizar esta transferencia");

        uint256 previousSenderBalance = balanceOf[_from];
        uint256 previousReceiverBalance = balanceOf[_to];

        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        assert(balanceOf[_from] == previousSenderBalance - _value);
        assert(balanceOf[_to] == previousReceiverBalance + _value);
        return true;
    }
}

contract WLCVTrading {
    WoldcoinVirtual public token;
    uint256 public constant maxBuyAmount = 1000000 * 10**3; //1 millón de WLCV
    uint256 public constant maxSellAmount = 700000 * 10**3; //700,000 WLCV
    uint256 public constant buyPriceIncrease = 3; //3% de aumento máximo en el precio de compra
    uint256 public constant sellPriceDecrease = 7; //7% de disminución máxima en el precio de venta
    uint256 public buyPrice;
    uint256 public sellPrice;

    event Buy(address indexed buyer, uint256 amount, uint256 price);
    event Sell(address indexed seller, uint256 amount,
