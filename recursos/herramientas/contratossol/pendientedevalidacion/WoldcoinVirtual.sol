// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

interface IUniswapV2Router02 {
    function swapExactTokensForETHSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;
}

interface IUniswapV2Factory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}

interface IUniswapV2Pair {
    function token0() external view returns (address);
    function token1() external view returns (address);
    function balanceOf(address owner) external view returns (uint);
    function transfer(address to, uint value) external returns (bool);
    function approve(address spender, uint value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint);
    function transferFrom(address from, address to, uint value) external returns (bool);
    function sync() external;
}

contract MyToken {
    string public constant name = "My Token";
    string public constant symbol = "MYT";
    uint8 public constant decimals = 18;
    uint256 public constant initialSupply = 1000000000 * 10**18; // 1 billion tokens

    address public immutable uniswapV2Pair;
    address public immutable uniswapV2Router;
    address private constant bnb = 0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c;
    address private constant usdt = 0x55d398326f99059fF775485246999027B3197955;
    address private constant deadAddress = 0x000000000000000000000000000000000000dEaD;
    address payable public owner;
    mapping (address => uint256) private balances;
    mapping (address => mapping (address => uint256)) private allowances;
    mapping (address => bool) private isExcludedFromFee;

    uint256 private constant MAX = ~uint256(0);
    uint256 private constant _tTotal = initialSupply;
    uint256 private _rTotal = (MAX - (MAX % _tTotal));
    uint256 private _tFeeTotal;
    uint256 public rewardThreshold = _tTotal / 2;

    uint256 public reflectionFee = 3;
    uint256 public liquidityFee = 3;
    uint256 public marketingFee = 3;
    uint256 public burnFee = 1;
    uint256 public totalFees = reflectionFee + liquidityFee + marketingFee + burnFee;

    IUniswapV2Router02 public uniswapV2Router;
    address public uniswapV2Pair;
    bool inSwapAndLiquify;
    bool public swapAndLiquifyEnabled = true;
    uint256 public minTokensToSwap = 50000 * 10**18;
    uint256 public maxTransactionAmount = _tTotal / 100; // 1% of total supply
    uint256 public numTokensSellToAddToLiquidity = _tTotal / 200; // 0.5% of total supply

    event Transfer(address indexed sender, address indexed recipient, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);
    event SwapAndLiquifyEnabledUpdated(bool enabled);
    event SwapAndLiquify(
        uint256 tokensSwapped,
        uint256 ethReceived,
        uint256
