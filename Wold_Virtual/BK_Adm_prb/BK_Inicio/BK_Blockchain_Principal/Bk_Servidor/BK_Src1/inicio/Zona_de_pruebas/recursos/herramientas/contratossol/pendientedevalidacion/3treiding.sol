pragma solidity ^0.8.0;

import "./ERC20.sol";
import "./UniswapV2Pair.sol";

contract TradingContract {
    
    address public btcToken;
    address public wlcToken;
    address public uniswapPair;
    
    uint256 public btcBalance;
    uint256 public wlcBalance;
    
    uint256 public desiredProfit;
    
    constructor(address _btcToken, address _wlcToken, address _uniswapPair, uint256 _desiredProfit) {
        btcToken = _btcToken;
        wlcToken = _wlcToken;
        uniswapPair = _uniswapPair;
        desiredProfit = _desiredProfit;
    }
    
    function buyWLC() public {
        require(btcBalance > 0, "Insufficient BTC balance");
        
        uint256 currentPrice = getCurrentPrice();
        uint256 targetPrice = (currentPrice * (100 - desiredProfit)) / 100;
        
        require(currentPrice <= targetPrice, "WLC price is not low enough");
        
        ERC20(wlcToken).transfer(msg.sender, (btcBalance * 10**18) / currentPrice);
        btcBalance = 0;
        wlcBalance = ERC20(wlcToken).balanceOf(address(this));
    }
    
    function sellWLC() public {
        require(wlcBalance > 0, "Insufficient WLC balance");
        
        uint256 currentPrice = getCurrentPrice();
        uint256 targetPrice = (currentPrice * 102) / 100;
        
        require(currentPrice >= targetPrice, "WLC price is not high enough");
        
        ERC20(wlcToken).transfer(uniswapPair, wlcBalance);
        uint256 amountOut = UniswapV2Pair(uniswapPair).getAmountOut(btcBalance, wlcBalance);
        ERC20(btcToken).transfer(msg.sender, amountOut);
        btcBalance = ERC20(btcToken).balanceOf(address(this));
        wlcBalance = 0;
    }
    
    function getCurrentPrice() public view returns (uint256) {
        (uint256 btcReserves, uint256 wlcReserves,) = UniswapV2Pair(uniswapPair).getReserves();
        return (wlcReserves * 10**18) / btcReserves;
    }
    
    function updatePrice() public {
        (,,uint256 lastPrice) = UniswapV2Pair(uniswapPair).getReserves();
        uint256 wlcDecimals = ERC20(wlcToken).decimals();
        uint256 btcDecimals = ERC20(btcToken).decimals();
        uint256 wlcPrice = (lastPrice * 10**(wlcDecimals + 18)) / (10**btcDecimals);
    }
}
