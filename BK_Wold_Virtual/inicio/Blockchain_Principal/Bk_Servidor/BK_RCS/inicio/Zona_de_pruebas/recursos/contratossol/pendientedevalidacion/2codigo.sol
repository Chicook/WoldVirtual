// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MyToken is ERC20 {
    using SafeMath for uint256;

    uint256 private constant MAX_TRANSACTION_AMOUNT = 1000 * (10**uint256(decimals()));
    uint256 private constant TRANSACTION_LOCK_TIME = 5 minutes;

    address private _owner;

    constructor() ERC20("My Token", "MYT") {
        _owner = msg.sender;
        _mint(msg.sender, 1000000 * (10**uint256(decimals())));
    }

    modifier onlyOwner() {
        require(msg.sender == _owner, "Ownable: caller is not the owner");
        _;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(amount <= MAX_TRANSACTION_AMOUNT, "Transfer amount exceeds the max limit");
        _lockTransfer();
        _burn(msg.sender, amount.mul(3).div(100));
        _burn(recipient, amount.mul(3).div(100));
        _transfer(msg.sender, recipient, amount.sub(amount.mul(3).div(100).mul(2)));
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(amount <= MAX_TRANSACTION_AMOUNT, "Transfer amount exceeds the max limit");
        _lockTransfer();
        _burn(sender, amount.mul(3).div(100));
        _burn(recipient, amount.mul(3).div(100));
        _transfer(sender, recipient, amount.sub(amount.mul(3).div(100).mul(2)));
        _approve(sender, msg.sender, allowance(sender, msg.sender).sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    function _lockTransfer() private {
        uint256 previousBalance = balanceOf(msg.sender);
        uint256 previousBlock = block.timestamp;
        _;
        uint256 newBalance = balanceOf(msg.sender);
        uint256 newBlock = block.timestamp;
        require(newBalance >= previousBalance.sub(previousBalance.div(10)), "Possible price manipulation detected");
        require(newBlock >= previousBlock.add(TRANSACTION_LOCK_TIME), "Transfer is locked temporarily");
    }

    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    function burnFrom(address account, uint256 amount) public onlyOwner {
        _burn(account, amount);
        _approve(account, msg.sender, allowance(account, msg.sender).sub(amount, "ERC20: burn amount exceeds allowance"));
    }
}

contract LiquidityLock {
    using SafeMath for uint256;

    address private _owner;

    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        bool claimed;
    }

