// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract HackProofLiquidityPool is ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public immutable WLCV;
    IUniswapV2Router public immutable uniswapRouter;
    uint public totalInvestment;

    mapping(address => uint) public investments;

    event InvestmentAdded(address investor, uint amount);
    event InvestmentRemoved(address investor, uint amount);

    constructor(IERC20 _WLCV, IUniswapV2Router _uniswapRouter) {
        WLCV = _WLCV;
        uniswapRouter = _uniswapRouter;
    }

    function addInvestment(address investor, uint amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        investments[investor] += amount;
        totalInvestment += amount;
        emit InvestmentAdded(investor, amount);
    }

    function removeInvestment(address investor, uint amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(investments[investor] >= amount, "Insufficient balance");
        investments[investor] -= amount;
        totalInvestment -= amount;
        emit InvestmentRemoved(investor, amount);
    }

    function recoverFunds() external nonReentrant {
        uint balance = address(this).balance;
        require(balance > 0, "No funds to recover");
        (bool success,) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    function recoverTokens(address token) external nonReentrant {
        uint balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No tokens to recover");
        IERC20(token).safeTransfer(msg.sender, balance);
    }

    function swapTokens() external nonReentrant {
        require(totalInvestment > 0, "No funds to invest");
        uint WLCVBalanceBefore = WLCV.balanceOf(address(this));
        address[] memory path = new address[](2);
        path[0] = IERC20(address(0)).address(); // BNB
        path[1] = address(WLCV);
        uint deadline = block.timestamp + 1800; // 30 minutes
        IERC20(IERC20(address(0)).address()).approve(address(uniswapRouter), totalInvestment);
        uniswapRouter.swapExactTokensForTokens(totalInvestment, 0, path, address(this), deadline);
        uint WLCVBalanceAfter = WLCV.balanceOf(address(this));
        uint WLCVReceived = WLCVBalanceAfter - WLCVBalanceBefore;
        for (uint i = 0; i < path.length - 1; i++) {
           
