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

interface IPancakeSwapV2Router02 {
    function swapExactTokensForTokensSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
}

contract MyToken is IBEP20 {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1000000000000000000000000; // 1,000,000 tokens
    uint256 public maxTransactionAmount = 1000000000000000000000; // 1,000 tokens
    uint256 public numTokensSellToAddToLiquidity = 50000000000000000000; // 50,000 tokens
    uint256 public reflectionFee = 3;
    uint256 public liquidityFee = 3;
    uint256 public constant MAX_INT_VALUE = type(uint256).max;

    mapping (address => uint256) public balanceOf;
    mapping (address => mapping (address => uint256)) public allowance;
    mapping (address => bool) public isExcludedFromFee;

    address public pancakeSwapV2Pair;
    address public pancakeSwapV2Router;

    bool public inSwapAndLiquify;
    bool public swapAndLiquifyEnabled = true;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event SwapAndLiquify(uint256 tokensSwapped, uint256 ethReceived, uint256 tokensIntoLiquidity);

    constructor() {
        balanceOf[msg.sender] = totalSupply;
        isExcludedFromFee[owner()] = true;
        isExcludedFromFee[address(this)] = true;

        // Testnet Router
        pancakeSwapV2Router = 0xD99D1c33F9fC3444f8101754aBC46c52416550D1;
        // Mainnet Router
        // pancakeSwapV2Router = 0x10ED43C718714eb63d5aA57B78B54704E256024E;

        address[] memory path = new address[](2);
        path[
