//SPDX-License-Identifier: MIT

pragma solidity >=0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Micontrato {
    
string public name = "WoldcoinVirtual";
 string public symbol = "WCV";
 uint8 public decimals = 3;
uint256 public totalSupply = 30000000  ;
mapping(address => uint256) public balanceOf;

 // Nuevo mapping para el pool de liquidez
    mapping(address => uint256) public liquidityPool;

    event LiquidityAdded(address indexed provider, uint256 amount);
    event LiquidityRemoved(address indexed provider, uint256 amount);

    // FunciÃ³n para que los usuarios aÃ±adan liquidez al pool
    function addLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfiere los tokens al contrato y actualiza el balance del pool
        balanceOf[msg.sender] -= amount;
        totalSupply += amount;
        liquidityPool[msg.sender] += amount;

        emit LiquidityAdded(msg.sender, amount);
    }

    // FunciÃ³n para que los usuarios retiren liquidez del pool
    function removeLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(liquidityPool[msg.sender] >= amount, "Insufficient liquidity");

        // Transfiere los tokens del pool al usuario y actualiza los saldos
        balanceOf[msg.sender] += amount;
        totalSupply -= amount;
        liquidityPool[msg.sender] -= amount;

        emit LiquidityRemoved(msg.sender, amount);
    }

    // DirecciÃ³n del contrato BTCB en Binance Smart Chain
    address public btcbAddress = 0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c; // Sustituye con la direcciÃ³n real de BTCB

    // Evento para notificar cuando se aÃ±ade liquidez con BTCB
    event LiquidityAddedWithBTCB(address indexed provider, uint256 amount);

    // FunciÃ³n para que los usuarios aÃ±adan liquidez con BTCB al pool
    function addLiquidityWithBTCB(uint256 btcbAmount) external {
        require(btcbAmount > 0, "BTCB amount must be greater than 0");

        // Transfiere los BTCB al contrato y actualiza el balance del pool
        IERC20(0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c).transferFrom(msg.sender, address(this), btcbAmount);
        balanceOf[msg.sender] -= btcbAmount; // Ajusta segÃºn tu lÃ³gica
        totalSupply += btcbAmount; // Ajusta segÃºn tu lÃ³gica
        liquidityPool[msg.sender] += btcbAmount;

        emit LiquidityAddedWithBTCB(msg.sender, btcbAmount);
    }

    // FunciÃ³n para consultar el precio de tu token
    function getTokenPrice() external view returns (uint256) {
        // Implementa la lÃ³gica para calcular el precio de tu token
        // Puedes utilizar orÃ¡culos o fuentes de precios externas aquÃ­
        // Devuelve el precio calculado
    }
}
