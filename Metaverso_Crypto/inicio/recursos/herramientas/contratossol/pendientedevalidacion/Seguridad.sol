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

abstract contract Ownable {
    address private _owner;
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    constructor () {
        _transferOwnership(msg.sender);
    }

    function owner() public view virtual returns (address) {
        return _owner;
    }

    modifier onlyOwner() {
        require(_owner == msg.sender, "Ownable: caller is not the owner");
        _;
    }

    function renounceOwnership() public virtual onlyOwner {
        emit OwnershipTransferred(_owner, address(0));
        _owner = address(0);
    }

    function transferOwnership(address newOwner) public virtual onlyOwner {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }

    function _transferOwnership(address newOwner) internal virtual {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }
}

contract WoldcoinVirtual is IBEP20, Ownable {
    string private constant _name = "WoldcoinVirtual";
    string private constant _symbol = "WLCV";
    uint8 private constant _decimals = 3;
    uint256 private constant _totalSupply = 30000000 * 10 ** uint256(_decimals);
    uint256 private _maxTxAmount = _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    mapping(address => bool) private _isExcludedFromMaxTxAmount;
    mapping(address => bool) private _isExcludedFromFee;
    bool private _inSwapAndLiquify;
    bool private _swapAndLiquifyEnabled = true;
    uint256 private _liquidityFee = 5;
    uint256 private _totalLiquidityFee;
    uint256 private _maxTxAmountPercent = 50;
    uint256 private _lastTransferTimestamp;
    uint256 private _timeBetweenTransfers = 1 days;
    uint256 private _timeToUnlock = 365 days;
    uint256 private _poolInternal;
    uint256 private _totalSentToPool;
    uint256 private _totalRemovedFromPool;
    uint256 private _liquidityAddedToPool;
    address private _poolAddress;
    address private _pancakePairAddress;
    address private _marketingAddress = 0x8b99F3660622e21f2910ECCA7fBe51d654a1517D;
    address private _deadAddress = 0x000000000000000000000000000000000000dEaD;

    event LiquidityAdded(uint256 tokenAmount, uint256 bnbAmount);

    constructor()
