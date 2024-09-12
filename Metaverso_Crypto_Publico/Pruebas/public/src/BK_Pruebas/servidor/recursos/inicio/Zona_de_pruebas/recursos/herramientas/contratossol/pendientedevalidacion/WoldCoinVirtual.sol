// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WoldcoinVirtual is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 30000000 * 10**3;
    uint8 private constant DECIMALS = 3;
    uint256 private constant MAX_HOLD_AMOUNT = 15000000 * 10**3;
    
    uint256 private _liquidityPoolBalance;
    uint256 private _rewardsPoolBalance;
    
    uint256 private _totalLiquidityPoolFee;
    uint256 private _totalRewardsPoolFee;
    
    uint256 private _ownerFee;
    
    mapping (address => uint256) private _holdBalances;
    
    constructor() ERC20("WoldcoinVirtual", "WLCV") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }
    
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        _deductFees(amount);
        return true;
    }
    
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        _deductFees(amount);
        return true;
    }
    
    function setLiquidityPoolFee(uint256 liquidityPoolFee) external onlyOwner {
        require(liquidityPoolFee <= 100, "Liquidity pool fee should not exceed 100%");
        _totalLiquidityPoolFee = liquidityPoolFee;
    }
    
    function setRewardsPoolFee(uint256 rewardsPoolFee) external onlyOwner {
        require(rewardsPoolFee <= 100, "Rewards pool fee should not exceed 100%");
        _totalRewardsPoolFee = rewardsPoolFee;
    }
    
    function setOwnerFee(uint256 ownerFee) external onlyOwner {
        require(ownerFee <= 100, "Owner fee should not exceed 100%");
        _ownerFee = ownerFee;
    }
    
    function addToLiquidityPool(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Not enough tokens to add to liquidity pool");
        _liquidityPoolBalance += amount;
        _transfer(msg.sender, address(this), amount);
    }
    
    function addToRewardsPool(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Not enough tokens to add to rewards pool");
        _rewardsPoolBalance += amount;
        _transfer(msg.sender, address(this), amount);
    }
    
    function removeFromLiquidityPool(uint256 amount) external {
        require(_liquidityPoolBalance >= amount, "Not enough tokens in liquidity pool");
        _liquidityPoolBalance -= amount;
        _transfer(address(this), msg.sender, amount);
    }
    
    function removeFromRewardsPool(uint256 amount) external {
        require(_rewardsPoolBalance >= amount, "Not enough tokens in rewards pool");
        _rewardsPoolBalance -= amount;
        _transfer(address(this), msg.sender, amount);
    }
    
    function claimOwnerFee() external onlyOwner {
        uint256 ownerFeeAmount = (address(this).balance * _ownerFee) / 100;
        payable(owner()).transfer(ownerFeeAmount);
    }
    
    function addToHold() external {
       
