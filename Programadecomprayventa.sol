// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WoldcoinVirtual is ERC20, Ownable {
    uint256 private constant MAX_SUPPLY = 15000000 * 10 ** 3; // max supply is 15 million tokens
    uint256 private constant INITIAL_POOL_SUPPLY = 2000000 * 10 ** 3; // initial pool supply is 2 million tokens
    
    address private constant PANCAKE_ROUTER_ADDRESS = 0x10ED43C718714eb63d5aA57B78B54704E256024E;
    address private constant DEAD_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    address private constant AUTO_LIQUIDITY_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    
    bool private inSwapAndLiquify;
    bool private swapAndLiquifyEnabled = true;
    
    uint256 private constant maxBuyTranscationAmount = 1000000 * 10 ** 3; // 1 million tokens
    uint256 private constant maxSellTransactionAmount = 700000 * 10 ** 3; // 700,000 tokens
    uint256 private constant numTokensSellToAddToLiquidity = 50000 * 10 ** 3; // 50,000 tokens
    
    uint256 private _liquidityFee = 3;
    uint256 private _previousLiquidityFee = _liquidityFee;
    
    uint256 private _poolFee = 50;
    uint256 private _previousPoolFee = _poolFee;
    
    uint256 private _bnbPoolFee = 25;
    uint256 private _usdtPoolFee = 25;
    uint256 private _previousBnbPoolFee = _bnbPoolFee;
    uint256 private _previousUsdtPoolFee = _usdtPoolFee;
    
    IUniswapV2Router02 public immutable uniswapV2Router;
    address public immutable uniswapV2Pair;
    
    mapping (address => bool) private _isExcludedFromFees;
    mapping (address => bool) private _liquidityHolders;
    
    constructor () ERC20("WoldcoinVirtual", "WLCV") {
        _mint(_msgSender(), MAX_SUPPLY);
        
        // exclude system contracts
        _isExcludedFromFees[owner()] = true;
        _isExcludedFromFees[address(this)] = true;
        
        // setup Uniswap router
        IUniswapV2Router02 _uniswapV2Router = IUniswapV2Router02(PANCAKE_ROUTER_ADDRESS);
        uniswapV2Pair = IUniswapV2Factory(_uniswapV2Router.factory()).createPair(address(this), _uniswapV2Router.WETH());
        uniswapV2Router = _uniswapV2Router;
        _liquidityHolders[uniswapV2Pair] = true;
        _isExcludedFromFees[uniswapV2Pair] = true;
        
        // transfer initial pool supply to contract
        _transfer(_msgSender(), address(this), INITIAL_POOL_SUPPLY);
    }
    
    function decimals() public pure override returns (uint8) {
        return 3;
    }
    
    function totalSupply() public view override
