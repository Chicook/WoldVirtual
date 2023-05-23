// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract WoldcoinVirtual is Ownable {
    using SafeMath for uint256;

        string public name = "WoldcoinVirtual";
        string public symbol = "WLCV";
        uint8 public decimals = 3;
        uint256 public totalSupply = 300000000 * 10**uint256(decimals);

                        
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

     constructor() {
         balanceOf[msg.sender] = totalSupply;
                                           }

         function transfer(address _to, uint256 _value) public returns (bool) {
         require(balanceOf[msg.sender] >= _value, "Insufficient balance");

         balanceOf[msg.sender] = balanceOf[msg.sender].sub(_value);
         balanceOf[_to] = balanceOf[_to].add(_value);

         emit Transfer(msg.sender, _to, _value);

         return true;
                    }

         function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
         require(balanceOf[_from] >= _value, "Insufficient balance");
         require(allowance[_from][msg.sender] >= _value, "Insufficient allowance");

         balanceOf[_from] = balanceOf[_from].sub(_value);
         balanceOf[_to] = balanceOf[_to].add(_value);
         allowance[_from][msg.sender] = allowance[_from][msg.sender].sub(_value);

         emit Transfer(_from, _to, _value);

         return true;
                    }

         function approve(address _spender, uint256 _value) public returns (bool) {
         allowance[msg.sender][_spender] = _value;

         emit Approval(msg.sender, _spender, _value);

         return true; }
}



contract LiquidityPool {
    IERC20 public token1;
    IERC20 public token2;
    uint public totalSupply;
    mapping(address => uint) public balances;
    uint public minTimeBetweenTransactions = 300; // 5 minutes
    uint public lastTransactionTime;

    constructor(IERC20 _token1, IERC20 _token2) {
        token1 = _token1;
        token2 = _token2;
        lastTransactionTime = block.timestamp;
    }

    function addLiquidity(uint amount1, uint amount2) external {
        require(amount1 > 0 && amount2 > 0, "Amounts must be greater than zero");
        uint balance1Before = token1.balanceOf(address(this));
        uint balance2Before = token2.balanceOf(address(this));
        token1.transferFrom(msg.sender, address(this), amount1);
        token2.transferFrom(msg.sender, address(this), amount2);
        uint balance1After = token1.balanceOf(address(this));
        uint balance2After = token2.balanceOf(address(this));
        uint liquidityAmount = (balance1After - balance1Before) < (balance2After - balance2Before) ?
                                (balance1After - balance1Before) : (balance2After - balance2Before);
        require(liquidityAmount > 0, "Insufficient liquidity");
        totalSupply += liquidityAmount;
        balances[msg.sender] += liquidityAmount;
        lastTransactionTime = block.timestamp;
    }

    function removeLiquidity(uint liquidity) external {
        require(liquidity > 0, "Liquidity must be greater than zero");
        require(balances[msg.sender] >= liquidity, "Insufficient liquidity balance");
        uint balance1 = token1.balanceOf(address(this));
        uint balance2 = token2.balanceOf(address(this));
        uint amount1 = (liquidity * balance1) / totalSupply;
        uint amount2 = (liquidity * balance2) / totalSupply;
        require(amount1 > 0 && amount2 > 0, "Amounts must be greater than zero");
        totalSupply -= liquidity;
        balances[msg.sender] -= liquidity;
        token1.transfer(msg.sender, amount1);
        token2.transfer(msg.sender, amount2);
        lastTransactionTime = block.timestamp;
    }

    function buyTokens(uint amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token1.balanceOf(address(this)) >= amount, "Insufficient liquidity for this transaction");
        token1.transferFrom(msg.sender, address(this), amount);
        uint tokensBought = (amount * token2.balanceOf(address(this))) / token1.balanceOf(address(this));
        require(tokensBought > 0, "Insufficient liquidity");
        token2.transfer(msg.sender, tokensBought);
        lastTransactionTime = block.timestamp;
    }

    function sellTokens(uint tokens) external {
        require(tokens > 0, "Tokens must be greater than zero");
        require(token2.balanceOf(address(this)) >= tokens, "Insufficient liquidity for this transaction");
        token2.transferFrom(msg.sender, address(this), tokens);
        uint tokensSold = (tokens * token1.balanceOf(address(this))) / token2.balanceOf(address(this));
        require(tokensSold > 0, "Insufficient liquidity");
        token1.transfer(msg.sender, tokensSold);
        lastTransactionTime = block.timestamp;
    }
    
    

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
    

interface ERC20 {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address who) external view returns (uint256);
}

contract LiquidityPool {
    address public tokenAddress;
    ERC20 public token;
    uint256 public totalLiquidity;
    mapping(address => uint256) public liquidity;
    mapping(address => uint256) public debt;
    uint256 public feePercentage;
    address[] public investors;

    event AddLiquidity(address indexed investor, uint256 amount);
    event RemoveLiquidity(address indexed investor, uint256 amount);
    event Borrow(address indexed borrower, uint256 amount);
    event Repay(address indexed borrower, uint256 amount);
    event FeePaid(address indexed borrower, uint256 amount);

    constructor(address _tokenAddress, uint256 _feePercentage) {
        tokenAddress = _tokenAddress;
        token = ERC20(_tokenAddress);
        feePercentage = _feePercentage;
    }

    function addLiquidity(uint256 amount) external {
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        liquidity[msg.sender] += amount;
        totalLiquidity += amount;
        if (!isInvestor(msg.sender)) {
            investors.push(msg.sender);
        }
        emit AddLiquidity(msg.sender, amount);
    }

    function removeLiquidity(uint256 amount) external {
        require(liquidity[msg.sender] >= amount, "Insufficient liquidity");
        uint256 fee = calculateFee(amount);
        uint256 amountMinusFee = amount - fee;
        require(token.transfer(msg.sender, amountMinusFee), "Transfer failed");
        liquidity[msg.sender] -= amount;
        totalLiquidity -= amount;
        if (liquidity[msg.sender] == 0) {
            removeInvestor(msg.sender);
        }
        emit RemoveLiquidity(msg.sender, amount);
        emit FeePaid(address(this), fee);
    }

    function borrow(uint256 amount) external {
        require(amount <= availableLiquidity(), "Insufficient liquidity");
        uint256 fee = calculateFee(amount);
        uint256 amountMinusFee = amount - fee;
        require(token.transfer(msg.sender, amountMinusFee), "Transfer failed");
        debt[msg.sender] += amountMinusFee;
        emit Borrow(msg.sender, amountMinusFee);
        emit FeePaid(address(this), fee);
    }

    function repay(uint256 amount) external {
        require(debt[msg.sender] >= amount, "Insufficient debt");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        debt[msg.sender] -= amount;
        emit Repay(msg.sender, amount);
    }

    function availableLiquidity() public view returns (uint256) {
        return token.balanceOf(address(this)) - totalLiquidity;
    }

    function calculateFee(uint256 amount) public view returns (uint256) {
        return amount * feePercentage / 100;
    }

    function isInvestor(address investor) public view returns (bool) {
        for (uint256 i = 0; i < investors.length; i++) {
            if (investors[i] == investor) {
                return true;
            }
        }
        return false;
    }

    function removeInvestor(address investor) internal {
        for (uint256 i = 0; i < investors.length; i++) {
            if (investors[i] == investor) {
                investors[i] = investors[investors.length - 1];
                investors.pop();
                return;
            }
        }
        
        
    uint256 public constant INITIAL_SUPPLY = 30_000_000_000 * 3 ** decimals;
    uint256 public totalSupply;
    mapping(address => uint256) balances;
    address public internalPool;
    uint256 public lockTime;
    uint256 public constant lockAmount = INITIAL_SUPPLY / 2;

    constructor(address _internalPool) {
        totalSupply = INITIAL_SUPPLY;
        balances[msg.sender] = INITIAL_SUPPLY;
        internalPool = _internalPool;
        lockTime = block.timestamp + 365 days;
        emit Transfer(address(0), msg.sender, INITIAL_SUPPLY);
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    function transferFrom(address _from, address _to, uint256 _value) public returns (bool success) {
        require(balances[_from] >= _value, "Insufficient balance");
        require(_value <= allowed[_from][msg.sender], "Insufficient allowance");
        balances[_from] -= _value;
        allowed[_from][msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool success) {
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    function allowance(address _owner, address _spender) public view returns (uint256 remaining) {
        return allowed[_owner][_spender];
    }
    
    function sendToInternalPool(uint256 _value) public returns (bool success) {
        require(_value <= lockAmount, "Amount exceeds the lock amount");
        require(block.timestamp >= lockTime, "Lock period has not ended yet");
        balances[msg.sender] -= _value;
        balances[internalPool] += _value;
        emit Transfer(msg.sender, internalPool, _value);
        lockTime = block.timestamp + 365 days;
        return true;
    }
    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 _value);
}

    

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
        uint256 wlcPrice = (lastPrice * 10**(wlcDecimals + 3)) / (10**btcDecimals);
}
modifier onlyOwner() {
                            require(msg.sender == owner, "Only the contract owner can call this function.");
                                    _;
 }

modifier tradingEnabled() {
                                require(isTradingEnabled, "Trading is currently disabled.");
                                        _;
                    }

                        constructor() ERC20("WoldcoinVirtual", "WLCV") {
                                    owner = msg.sender;
                                            isTradingEnabled = false;
                                                    _mint(msg.sender, 300000000 * 3** decimals());
                        }

                            function enableTrading() external onlyOwner {
                                        isTradingEnabled = true;
                            }

                                function transfer(address recipient, uint256 amount) public override tradingEnabled returns (bool) {
                                            return super.transfer(recipient, amount);
                                }

                                    function transferFrom(address sender, address recipient, uint256 amount) public override tradingEnabled returns (bool) {
                                                return super.transferFrom(sender, recipient, amount);
                                    }

                                        function approve(address spender, uint256 amount) public override tradingEnabled returns (bool) {
                                                    return super.approve(spender, amount);
                                        }

                                            function increaseAllowance(address spender, uint256 addedValue) public override tradingEnabled returns (bool) {
                                                        return super.increaseAllowance(spender, addedValue);
                                            }

                                                function decreaseAllowance(address spender, uint256 subtractedValue) public override tradingEnabled returns (bool) {
                                                            return super.decreaseAllowance(spender, subtractedValue);
                                                }

                                                    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override tradingEnabled {
                                                                super._beforeTokenTransfer(from, to, amount); 
    
  
  function totalSupply() external view returns (uint256);
 function balanceOf(address account) external view returns (uint256);
     function transfer(address recipient, uint256 amount) external returns (bool);
}


constructor() {
balanceOf[msg.sender] = totalSupply;
                            }

 function transfer(address recipient, uint256 amount) external override returns (bool) {
require(balanceOf[msg.sender] >= amount, "Insufficient balance");
  balanceOf[msg.sender] -= amount;
 balanceOf[recipient] += amount;
  return true;
  }
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract LiquidityPool {
    address public owner;
    address public tokenAddress;
    uint256 public lastSaleTime;
    uint256 public liquidityAmount;
    
    event LiquidityAdded(uint256 amount);
    event LiquidityRemoved(uint256 amount);
    
    constructor(address _tokenAddress) {
        owner = msg.sender;
        tokenAddress = _tokenAddress;
        lastSaleTime = block.timestamp;
        liquidityAmount = 0;
    }
    
    modifier onlyOwner {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }
    
    function addLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance.");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed.");
        liquidityAmount += amount;
        emit LiquidityAdded(amount);
    }
    
    function removeLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        require(liquidityAmount >= amount, "Insufficient liquidity.");
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed.");
        liquidityAmount -= amount;
        emit LiquidityRemoved(amount);
    }
    
    function transferToVault() external onlyOwner {
        require(block.timestamp - lastSaleTime > 3600, "Cannot transfer during sale.");
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, liquidityAmount), "Transfer failed.");
        liquidityAmount = 0;
    }
    
    function receiveTokens() external payable {
        revert("This contract does not accept ETH.");
    }
    
    fallback() external payable {
        revert("This contract does not accept ETH.");
    }


/**
 * @dev Interface of the ERC20 standard as defined in the EIP.
 */
interface IERC20 {
    /**
     * @dev Returns the amount of tokens in existence.
     */
    function totalSupply() external view returns (uint256);

    /**
     * @dev Returns the amount of tokens owned by `account`.
     */
    function balanceOf(address account) external view returns (uint256);

    /**
     * @dev Moves `amount` tokens from the caller's account to `recipient`.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transfer(address recipient, uint256 amount) external returns (bool);

    /**
     * @dev Returns the remaining number of tokens that `spender` will be
     * allowed to spend on behalf of `owner` through {transferFrom}. This is
     * zero by default.
     *
     * This value changes when {approve} or {transferFrom} are called.
     */
    function allowance(address owner, address spender) external view returns (uint256);

    /**
     * @dev Sets `amount` as the allowance of `spender` over the caller's tokens.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * IMPORTANT: Beware that changing an allowance with this method brings the risk
     * that someone may use both the old and the new allowance by unfortunate
     * transaction ordering. One possible solution to mitigate this race
     * condition is to first reduce the spender's allowance to 0 and set the
     * desired value afterwards:
     * https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
     *
     * Emits an {Approval} event.
     */
    function approve(address spender, uint256 amount) external returns (bool);

    /**
     * @dev Moves `amount` tokens from `sender` to `recipient` using the
     * allowance mechanism. `amount` is then deducted from the caller's
     * allowance.
     *
     * Returns a boolean value indicating whether the operation succeeded.
     *
     * Emits a {Transfer} event.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    /**
     * @dev Emitted when `value` tokens are moved from one account (`from`) to
     * another (`to`).
     *
     * Note that `value` may be zero.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Emitted when the allowance of a `spender` for an `owner` is set by
     * a call to {approve}. `value` is the new allowance.
     */
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

/**
 * @dev Interface for the optional metadata functions from the ERC20 standard.
 *
 * _Available since v4.1._
 */
interface IERC20Metadata is IERC20 {
    /**
     * @dev Returns the name of the token.
     */
    function name() external view returns (string memory);

    /**
     * @dev Returns the symbol of the token.
     */
    function symbol() external view returns (string memory);

    /**
     * @dev Returns the decimals places of the token.
     */
    function decimals() external view returns (uint256);
}

// File: @openzeppelin/contracts/utils/Context.sol






abstract contract Context {
    function _msgSender() internal view virtual returns (address) {
        return msg.sender;
    }

    function _msgData() internal view virtual returns (bytes calldata) {
        this; // silence state mutability warning without generating bytecode - see https://github.com/ethereum/solidity/issues/2691
        return msg.data;
    }

// File: @openzeppelin/contracts/token/ERC20/ERC20.sol

contract ERC20 is Context, IERC20, IERC20Metadata {
    mapping (address => uint256) private _balances;

    mapping (address => mapping (address => uint256)) private _allowances;

    uint256 private _totalSupply;
    uint256 private _decimals;
    string private _name;
    string private _symbol;

    /**
     * @dev Sets the values for {name} and {symbol}.
     *
     * The defaut value of {decimals} is 18. To select a different value for
     * {decimals} you should overload it.
     *
     * All two of these values are immutable: they can only be set once during
     * construction.
     */
    constructor (string memory name_, string memory symbol_,uint256 initialBalance_,uint256 decimals_,address tokenOwner) {
        _name = name_;
        _symbol = symbol_;
        _totalSupply = initialBalance_* 10**decimals_;
        _balances[tokenOwner] = _totalSupply;
        _decimals = decimals_;
        emit Transfer(address(0), tokenOwner, _totalSupply);
    }

    /**
     * @dev Returns the name of the token.
     */
    function name() public view virtual override returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the symbol of the token, usually a shorter version of the
     * name.
     */
    function symbol() public view virtual override returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns the number of decimals used to get its user representation.
     * For example, if `decimals` equals `2`, a balance of `505` tokens should
     * be displayed to a user as `5,05` (`505 / 10 ** 2`).
     *
     * Tokens usually opt for a value of 18, imitating the relationship between
     * Ether and Wei. This is the value {ERC20} uses, unless this function is
     * overridden;
     *
     * NOTE: This information is only used for _display_ purposes: it in
     * no way affects any of the arithmetic of the contract, including
     * {IERC20-balanceOf} and {IERC20-transfer}.
     */
    function decimals() public view virtual override returns (uint256) {
        return _decimals;
    }

    /**
     * @dev See {IERC20-totalSupply}.
     */
    function totalSupply() public view virtual override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev See {IERC20-balanceOf}.
     */
    function balanceOf(address account) public view virtual override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev See {IERC20-transfer}.
     *
     * Requirements:
     *
     * - `recipient` cannot be the zero address.
     * - the caller must have a balance of at least `amount`.
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev See {IERC20-allowance}.
     */
    function allowance(address owner, address spender) public view virtual override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev See {IERC20-approve}.
     *
     * Requirements:
     *
     * - `spender` cannot be the zero address.
     */
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        _approve(_msgSender(), spender, amount);
        return true;
    }

    /**
     * @dev See {IERC20-transferFrom}.
     *
     * Emits an {Approval} event indicating the updated allowance. This is not
     * required by the EIP. See the note at the beginning of {ERC20}.
     *
     * Requirements:
     *
     * - `sender` and `recipient` cannot be the zero address.
     * - `sender` must have a balance of at least `amount`.
     * - the caller must have allowance for ``sender``'s tokens of at least
     * `amount`.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);

        uint256 currentAllowance = _allowances[sender][_msgSender()];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, _msgSender(), currentAllowance - amount);

        return true;
    }

    /**
     * @dev Atomically increases the allowance granted to `spender` by the caller.
     *
     * This is an alternative to {approve} that can be used as a mitigation for
     * problems described in {IERC20-approve}.
     *
     * Emits an {Approval} event indicating the updated allowance.
     *
     * Requirements:
     *
     * - `spender` cannot be the zero address.
     */
    function increaseAllowance(address spender, uint256 addedValue) public virtual returns (bool) {
        _approve(_msgSender(), spender, _allowances[_msgSender()][spender] + addedValue);
        return true;
    }

    /**
     * @dev Atomically decreases the allowance granted to `spender` by the caller.
     *
     * This is an alternative to {approve} that can be used as a mitigation for
     * problems described in {IERC20-approve}.
     *
     * Emits an {Approval} event indicating the updated allowance.
     *
     * Requirements:
     *
     * - `spender` cannot be the zero address.
     * - `spender` must have allowance for the caller of at least
     * `subtractedValue`.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public virtual returns (bool) {
        uint256 currentAllowance = _allowances[_msgSender()][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        _approve(_msgSender(), spender, currentAllowance - subtractedValue);

        return true;
    }

 function _transfer(address sender, address recipient, uint256 amount) internal virtual {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

     uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        _balances[sender] = senderBalance - amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal virtual {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

}
 {
        payable(feeReceiver_).transfer(msg.value);
    }
}   

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

contract MyToken is IBEP20 {
    string public constant name = "My Token";
    string public constant symbol = "MTK";
    uint8 public constant decimals = 3;
    uint256 private constant _totalSupply = 1000000 * 10 ** decimals;
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;
    uint256 public constant feePercentage = 3; // 3% fee on transfers
    address public owner;

    constructor() {
        _balances[msg.sender] = _totalSupply;
        owner = msg.sender;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = (amount * feePercentage) / 100;
        _balances[msg.sender] -= amount;
        _balances[recipient] += (amount - fee);
        _balances[owner] += fee;
        emit Transfer(msg.sender, recipient, amount);
        emit Transfer(msg.sender, owner, fee);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = (amount * feePercentage) / 100;
        _balances[sender] -= amount;
        _balances[recipient] += (amount - fee);
        _balances[owner] += fee;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        emit Transfer(sender, owner, fee);
        return true;
    }
}

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

contract Token is IBEP20 {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 3;
    uint256 public override totalSupply;
    uint256 public tokensLocked;
    uint256 private _totalSupply;
    uint256 private _tokensLocked;
    address public owner;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    struct Stake {
        uint256 amount;
        uint256 unlockTime;
    }

    mapping(address => Stake[]) public stakes;
    mapping(address => uint256) public stakingBalance;
    mapping(address => uint256) public lastClaim;

    uint256 public stakingRewards = 0;
    uint256 public stakingRewardsPaid = 0;
    uint256 public rewardsDuration = 365 days;
    uint256 public lastRewardTime = block.timestamp;

    uint256 public salesProgramPercentage = 25;
    address public salesProgramWallet;

    address public internalPool;

    constructor(uint256 initialSupply, address _salesProgramWallet) {
        totalSupply = initialSupply * 10 ** decimals;
        _balances[msg.sender] = totalSupply;
        owner = msg.sender;
        salesProgramWallet = _salesProgramWallet;
        internalPool = address(this);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    function setInternalPool(address pool) external onlyOwner {
        internalPool = pool;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
}
    
import "./IERC20.sol";

contract PoolFarming {
    address public owner;
    IERC20 public token;
    IERC20 public bnbToken;
    uint256 public totalLPTokens;
    uint256 public totalRewards;
    uint256 public bnbSellThreshold;
    uint256 public lpSellPercentage;
    uint256 public lpSellFeePercentage;
    uint256 public rewardsPercentage;
    uint256 public rewardsFeePercentage;

    mapping(address => uint256) public lpBalances;
    mapping(address => uint256) public rewardsBalances;

    event LPTokensAdded(address indexed user, uint256 amount);
    event LPTokensRemoved(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _token, IERC20 _bnbToken) {
        owner = msg.sender;
        token = _token;
        bnbToken = _bnbToken;
        totalLPTokens = 0;
        totalRewards = 0;
        bnbSellThreshold = 1000000000000000000; // 1 BNB
        lpSellPercentage = 25; // 25%
        lpSellFeePercentage = 3; // 3%
        rewardsPercentage = 75; // 75%
        rewardsFeePercentage = 25; // 2.5%
    }

    function addLPTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(token.allowance(msg.sender, address(this)) >= amount, "Must approve LP tokens first");

        token.transferFrom(msg.sender, address(this), amount);
        lpBalances[msg.sender] += amount;
        totalLPTokens += amount;

        emit LPTokensAdded(msg.sender, amount);
    }

    function removeLPTokens(uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");
        require(lpBalances[msg.sender] >= amount, "Insufficient LP tokens");

        lpBalances[msg.sender] -= amount;
        totalLPTokens -= amount;

        token.transfer(msg.sender, amount);

        emit LPTokensRemoved(msg.sender, amount);
    }

    function claimRewards() public {
        uint256 rewards = rewardsBalances[msg.sender];
        require(rewards > 0, "No rewards to claim");

        rewardsBalances[msg.sender] = 0;
        totalRewards -= rewards;

        token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    function deposit() public {
        require(lpBalances[msg.sender] > 0, "No LP tokens to deposit");

        uint256 bnbBalance = bnbToken.balanceOf(address(this));

        if (bnbBalance >= bnbSellThreshold) {
            uint256 sellAmount = (bnbBalance * lpSellPercentage) / 100;

            bnbToken.transfer(owner, sellAmount);

            uint256 feeAmount = (sellAmount * lpSellFeePercentage) / 100;

            totalLPTokens -= feeAmount;

            uint256 rewardsAmount = (sellAmount * rewardsPercentage) / 100;
            uint256 rewardsFee = (rewardsAmount * rewardsFeePercentage) / 100;

            rewardsBalances[owner] += rewardsFee;
            totalRewards += rewardsAmount - rewardsFee;

            emit LPTokensRemoved(owner, feeAmount);
        }
}

interface IBEP20 {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address who) external view returns (uint256);
    function decimals() external view returns (uint8);
}

contract WoldcoinVirtualPreSale {
    address public tokenAddress;
    address public owner;
    uint256 public totalTokens;
    uint256 public tokensSold;
    uint256 public price;
    uint256 public startDate;
    uint256 public endDate;
    uint256 public minPurchase;
    uint256 public maxPurchase;
    bool public isPresaleOpen;

    mapping(address => uint256) public balances;

    event Buy(address indexed buyer, uint256 tokens);

    constructor(address _tokenAddress, uint256 _totalTokens, uint256 _price, uint256 _startDate, uint256 _endDate, uint256 _minPurchase, uint256 _maxPurchase) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalTokens > 0, "Invalid total tokens");
        require(_price > 0, "Invalid price");
        require(_startDate > 0 && _startDate < _endDate, "Invalid dates");
        require(_minPurchase > 0 && _maxPurchase > 0 && _minPurchase <= _maxPurchase, "Invalid purchase limits");

        tokenAddress = _tokenAddress;
        owner = msg.sender;
        totalTokens = _totalTokens;
        price = _price;
        startDate = _startDate;
        endDate = _endDate;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        isPresaleOpen = false;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    function startPresale() public onlyOwner {
        require(!isPresaleOpen, "Presale is already open.");
        require(IBEP20(tokenAddress).balanceOf(address(this)) >= totalTokens, "Insufficient token balance for presale.");

        isPresaleOpen = true;
    }

    function endPresale() public onlyOwner {
        require(isPresaleOpen, "Presale is not open.");

        isPresaleOpen = false;

        // Calculate remaining tokens in contract after deducting the aidrop
        uint256 remainingTokens = IBEP20(tokenAddress).balanceOf(address(this)) - 2000000 * 10**3;

        // If any remaining tokens, transfer to owner
        if (remainingTokens > 0) {
            IBEP20(tokenAddress).transfer(owner, remainingTokens);
        }
    }

    function buyTokens() public payable {
        require(isPresaleOpen, "Presale is not open.");
        require(block.timestamp >= startDate && block.timestamp <= endDate, "Invalid purchase time.");
        require(msg.value >= minPurchase && msg.value <= maxPurchase, "Invalid purchase amount.");

        uint256 tokensToBuy = msg.value * price;

        require(tokensToBuy <= (totalTokens - tokensSold), "Insufficient tokens for sale.");

        balances[msg.sender] += tokensToBuy;
        tokensSold += tokensToBuy;

        emit Buy(msg.sender, tokensToBuy);
}

 mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    
    uint256 public constant transferFee = 30; // 3% fee
    
    uint256 public releaseTime; // Timestamp when tokens can be released
    address public lockContract; // Address of the lock contract
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    constructor() {
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
        
        releaseTime = block.timestamp + 365 days; // Release time set to 365 days from contract deployment
        lockContract = address(0x1234567890123456789012345678901234567890); // Example address of lock contract
    }
    
    function transfer(address _to, uint256 _value) external returns (bool success) {
        uint256 fee = (_value * transferFee) / 1000;
        uint256 valueAfterFee = _value - fee;
        
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += valueAfterFee;
        balanceOf[lockContract] += fee; // Transfer fee to lock contract
        
        emit Transfer(msg.sender, _to, valueAfterFee);
        emit Transfer(msg.sender, lockContract, fee);
        
        return true;
    }
    
    function approve(address _spender, uint256 _value) external returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        
        emit Approval(msg.sender, _spender, _value);
        
        return true;
    }
    
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool success) {
        uint256 fee = (_value * transferFee) / 1000;
        uint256 valueAfterFee = _value - fee;
        
        balanceOf[_from] -= _value;
        balanceOf[_to] += valueAfterFee;
        balanceOf[lockContract] += fee; // Transfer fee to lock contract
        
        allowance[_from][msg.sender] -= _value;
        
        emit Transfer(_from, _to, valueAfterFee);
        emit Transfer(_from, lockContract, fee);
        
        return true;
    }

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/utils/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/security/Pausable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol";

contract StakingContract is Ownable, Pausable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 startTimestamp;
        uint256 endTimestamp;
        bool isActive;
    }

    mapping (address => Stake) public stakes;

    IERC20 public token;
    uint256 public minimumStakeAmount;
    uint256 public stakingPeriod;

    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event StakingPeriodChanged(uint256 newStakingPeriod);

    constructor(address _token, uint256 _minimumStakeAmount, uint256 _stakingPeriod) {
        token = IERC20(_token);
        minimumStakeAmount = _minimumStakeAmount;
        stakingPeriod = _stakingPeriod;
    }

    function stake(uint256 _amount) external whenNotPaused {
        require(_amount >= minimumStakeAmount, "Amount is below the minimum stake amount");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(token.allowance(msg.sender, address(this)) >= _amount, "Insufficient token allowance");

        // Only allow staking if user doesn't already have an active stake
        require(!stakes[msg.sender].isActive, "Already an active stake");

        // Add staked amount to user's stake
        stakes[msg.sender].amount = _amount;

        // Set start timestamp to current block timestamp
        stakes[msg.sender].startTimestamp = block.timestamp;

        // Set end timestamp to current block timestamp plus staking period
        stakes[msg.sender].endTimestamp = block.timestamp.add(stakingPeriod);

        // Mark stake as active
        stakes[msg.sender].isActive = true;

        // Transfer staked tokens from user to contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    function unstake() external whenNotPaused {
        require(stakes[msg.sender].isActive, "No active stake");

        // Check that staking period has ended
        require(block.timestamp >= stakes[msg.sender].endTimestamp, "Staking period has not ended");

        // Check that contract has enough tokens to fulfill unstake request
        require(token.balanceOf(address(this)) >= stakes[msg.sender].amount, "Insufficient contract balance");

        // Transfer staked tokens from contract to user
        token.safeTransfer(msg.sender, stakes[msg.sender].amount);

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTimestamp = 0;
        stakes[msg.sender].endTimestamp = 0;
        stakes[msg.sender].isActive = false;

        emit Unstaked(msg.sender, stakes[msg.sender].amount);

}

contract NFTMarketplace {
    
    struct NFT {
        uint256 id;
        string name;
        string description;
        string imageURI;
        address owner;
        uint256 price;
        bool isPrimarySale;
        bool isSold;
    }
    
    mapping(uint256 => NFT) public nfts;
    uint256 public nftCount;
    address public poolAddress;
    uint256 public poolBalance;
    
    constructor(address _poolAddress) {
        poolAddress = _poolAddress;
    }
    
    function createNFT(string memory _name, string memory _description, string memory _imageURI, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");
        require(nftCount < 30000000, "Max NFT limit reached");
        nftCount++;
        nfts[nftCount] = NFT(nftCount, _name, _description, _imageURI, msg.sender, _price, true, false);
        uint256 poolFee = 1;
        poolBalance += poolFee;
        payable(poolAddress).transfer(poolFee * 10**18);
    }
    
    function buyNFT(uint256 _nftId) public payable {
        NFT memory nft = nfts[_nftId];
        require(!nft.isSold, "NFT is already sold");
        require(msg.value == nft.price, "Incorrect amount of ETH sent");
        require(nft.isPrimarySale || msg.value >= 1 ether, "Minimum purchase amount for secondary sales is 1 ETH");
        uint256 saleFee = nft.price / 4;
        uint256 ownerPayment = nft.price - saleFee;
        nfts[_nftId].owner = msg.sender;
        nfts[_nftId].isPrimarySale = false;
        nfts[_nftId].isSold = true;
        payable(nfts[_nftId].owner).transfer(ownerPayment);
        poolBalance += saleFee;
        if (nft.isPrimarySale) {
            uint256 poolFee = 1;
            poolBalance += poolFee;
            payable(poolAddress).transfer(poolFee * 10**18);
            if (msg.value > 1 ether) {
                uint256 excess = msg.value - 1 ether;
                payable(msg.sender).transfer(excess);
            }
        } else {
            if (msg.value > saleFee) {
                uint256 excess = msg.value - saleFee;
                payable(msg.sender).transfer(excess);
            }
        }
        if (saleFee > 0) {
            uint256 bnbAmount = (saleFee * 50) / nfts[_nftId].price;
            uint256 usdtAmount = (saleFee * 50) / nfts[_nftId].price;
            payable(poolAddress).transfer(bnbAmount * 10**18);
            payable(poolAddress).transfer(usdtAmount * 10**18);
        }
    }
    
    function getNFT(uint256 _nftId) public view returns (NFT memory) {
        return nfts[_nftId];
    }
    
    function getPoolBalance() public view returns (uint256) {
        return poolBalance;

}

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    address private constant _poolAddress = 0x123...; // Replace with the pool address
    uint256 private constant _lockRatio = 50; // Lock 50% of collected fees
    uint256 private _lockedBalance;
    uint256 private _lastLockedTimestamp;
    uint256 private _totalStaked;
    mapping(address => uint256) private _stakes;
    mapping(address => uint256) private _lastRewardClaim;

    uint256 private constant _rewardRate = 100; // 100 tokens per day
    uint256 private constant _rewardInterval = 1 days;

    function collectFee(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        _lockedBalance += (amount * _lockRatio) / 100;
        uint256 transferAmount = amount - ((amount * _lockRatio) / 100);
        super.transferFrom(msg.sender, _poolAddress, transferAmount);

        // Update user stake
        _stakes[msg.sender] += transferAmount;
        _totalStaked += transferAmount;
        _lastRewardClaim[msg.sender] = block.timestamp;
    }

    function unlockFee() external {
        require(_lockedBalance > 0, "No locked balance");
        require(block.timestamp - _lastLockedTimestamp >= 1 days, "Must wait at least one day");

        uint256 unlockAmount = (_lockedBalance * 100) / _lockRatio;
        _lockedBalance = 0;
        _lastLockedTimestamp = block.timestamp;
        super.transfer(_poolAddress, unlockAmount);
    }

    function claimReward() external {
        require(_stakes[msg.sender] > 0, "No stake to claim reward");
        require(block.timestamp - _lastRewardClaim[msg.sender] >= _rewardInterval, "Must wait for reward interval");

        uint256 reward = (_stakes[msg.sender] * (_rewardRate * _rewardInterval)) / _totalStaked;
        _lastRewardClaim[msg.sender] = block.timestamp;
        super.transfer(msg.sender, reward);
    }

    function getPoolBalance() external view returns (uint256) {
        return balanceOf(_poolAddress);
    }

    function checkMinimumRewards() external view returns (bool) {
        uint256 totalRewards = (_totalStaked * (_rewardRate * _rewardInterval)) / _totalStaked;
        uint256 poolBalance = balanceOf(_poolAddress);
        return (poolBalance >= (totalRewards * 2)); // Check if the pool balance is at least twice the total rewards
    }
}



import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    address private constant _poolAddress = 0x123...; // Replace with the pool address
    uint256 private constant _lockRatio = 50; // Lock 50% of collected fees
    uint256 private _lockedBalance;
    uint256 private _lastLockedTimestamp;
    uint256 private _totalStaked;
    mapping(address => uint256) private _stakes;
    mapping(address => uint256) private _lastRewardClaim;

    uint256 private constant _rewardRate = 100; // 100 tokens per day
    uint256 private constant _rewardInterval = 1 days;

    function collectFee(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        _lockedBalance += (amount * _lockRatio) / 100;
        uint256 transferAmount = amount - ((amount * _lockRatio) / 100);
        super.transferFrom(msg.sender, _poolAddress, transferAmount);

        // Update user stake
        _stakes[msg.sender] += transferAmount;
        _totalStaked += transferAmount;
        _lastRewardClaim[msg.sender] = block.timestamp;
    }

    function unlockFee() external {
        require(_lockedBalance > 0, "No locked balance");
        require(block.timestamp - _lastLockedTimestamp >= 1 days, "Must wait at least one day");

        uint256 unlockAmount = (_lockedBalance * 100) / _lockRatio;
        _lockedBalance = 0;
        _lastLockedTimestamp = block.timestamp;
        super.transfer(_poolAddress, unlockAmount);
    }

    function claimReward() external {
        require(_stakes[msg.sender] > 0, "No stake to claim reward");
        require(block.timestamp - _lastRewardClaim[msg.sender] >= _rewardInterval, "Must wait for reward interval");

        uint256 reward = (_stakes[msg.sender] * (_rewardRate * _rewardInterval)) / _totalStaked;
        _lastRewardClaim[msg.sender] = block.timestamp;
        super.transfer(msg.sender, reward);
    }

    function getPoolBalance() external view returns (uint256) {
        return balanceOf(_poolAddress);
    }

    function checkMinimumRewards() external view returns (bool) {
        uint256 totalRewards = (_totalStaked * (_rewardRate * _rewardInterval)) / _totalStaked;
        uint256 poolBalance = balanceOf(_poolAddress);
        return (poolBalance >= (totalRewards * 2)); // Check if the pool balance is at least twice the total rewards
    }
}

contract LiquidityPool {
    // Variables de la liquidez
    mapping(address => uint) public balances;
    uint public totalSupply;
    uint public rewardRate = 1;
    uint public collateralRatio = 2;
    uint public interestRate = 25;
    uint public loanBalance;

    // Eventos
    event Deposit(address indexed sender, uint amount);
    event Withdraw(address indexed sender, uint amount);
    event LoanApplied(address indexed borrower, uint amount);
    event LoanRepaid(address indexed borrower, uint amount);

    // Funciones para el manejo de la liquidez
    function deposit() public payable {
        balances[msg.sender] += msg.value;
        totalSupply += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    function withdraw(uint amount) public {
        require(amount > 0 && amount <= balances[msg.sender], "No tiene suficientes fondos para retirar");
        balances[msg.sender] -= amount;
        totalSupply -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdraw(msg.sender, amount);
    }

    // Funciones para la gestión del crédito
    function applyLoan(uint amount) public {
        require(amount > 0 && amount <= address(this).balance * collateralRatio / 100, "El monto solicitado no es válido");
        require(loanBalance == 0, "Ya tiene un préstamo pendiente");
        loanBalance = amount;
        payable(msg.sender).transfer(amount);
        emit LoanApplied(msg.sender, amount);
    }

    function repayLoan() public payable {
        require(msg.value > 0 && msg.value <= loanBalance, "El monto ingresado no es válido");
        loanBalance -= msg.value;
        emit LoanRepaid(msg.sender, msg.value);
    }

    function calculateInterest() public view returns (uint) {
        return loanBalance * interestRate / 100;
    }

    function applyInterest() public {
        require(loanBalance > 0, "No tiene un préstamo pendiente");
        uint interest = calculateInterest();
        loanBalance += interest;
        payable(msg.sender).transfer(interest);
    }
}

interface IERC20 {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address owner) external view returns (uint256);
}

contract WoldcoinVirtual {
    string public constant name = "WoldcoinVirtual";
    string public constant symbol = "WLCV";
    uint8 public constant decimals = 3;
    uint256 public constant initialSupply = 30_000_000 * 10 ** uint256(decimals);
    uint256 public totalSupply;
    uint256 public soldTokens;
    uint256 public constant poolPercent = 50; // 50% of totalSupply
    uint256 public constant transferPercent = 25; // 25% of received tokens to be automatically sold and added to liquidity pool
    uint256 public constant poolWithdrawalPeriod = 365 days;
    uint256 public poolWithdrawalStartTime;
    uint256 public poolWithdrawalLastTimeWithdrawn;

    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowed;

    address payable public owner;

    address public liquidityPool;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor() {
        owner = payable(msg.sender);
        totalSupply = initialSupply;
        balances[owner] = totalSupply / 2;
        soldTokens = totalSupply / 2;
        liquidityPool = address(this);
    }

    function() external payable {
        require(msg.value > 0, "Invalid ETH amount");
        uint256 tokensToTransfer = calculateTokens(msg.value);
        require(soldTokens + tokensToTransfer <= totalSupply, "Not enough tokens left to sell");
        balances[msg.sender] += tokensToTransfer;
        soldTokens += tokensToTransfer;
        owner.transfer(msg.value);
        emit Transfer(address(0), msg.sender, tokensToTransfer);
    }

    function calculateTokens(uint256 weiAmount) private pure returns (uint256) {
        return weiAmount * 1000; // 1 BTCB = 1000 WLCV
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);

        // Automatically sell and add 25% of received tokens to liquidity pool
        uint256 transferAmount = _value * transferPercent / 100;
        if (transferAmount > 0) {
            require(IERC20(liquidityPool).balanceOf(address(this)) >= transferAmount, "Insufficient liquidity pool balance");
            IERC20(liquidityPool).transfer(msg.sender, transferAmount);
            uint256 liquidityPoolAmount = transferAmount / 2;
            IERC20(liquidityPool).transfer(owner, liquidityPoolAmount);
            IERC20(liquidityPool).transfer(address(this), liquidityPoolAmount);
        }

        return true;
    }

    function approve(address _spender, uint256 _value) public returns (bool) {
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }
  
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
    
    pragma solidity ^0.8.0;

contract MyToken {
    string public constant name = "My Token";
    string public constant symbol = "MTK";
    uint8 public constant decimals = 18;
    uint256 public constant initialSupply = 30000000 * 10 ** uint256(decimals);
    uint256 public constant lockedSupply = initialSupply / 2;
    uint256 public constant releasePeriod = 365 days;

    mapping(address => uint256) balances;
    mapping(address => mapping(address => uint256)) allowances;
    
    address public lockContractAddress;
    
    constructor(address _lockContractAddress) {
        lockContractAddress = _lockContractAddress;
        balances[msg.sender] = initialSupply - lockedSupply;
        balances[_lockContractAddress] = lockedSupply;
        emit Transfer(address(0), msg.sender, initialSupply - lockedSupply);
        emit Transfer(address(0), _lockContractAddress, lockedSupply);
    }

    function totalSupply() external pure returns (uint256) {
        return initialSupply;
    }

    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[msg.sender] >= amount, "ERC20: insufficient balance");
        
        _transfer(msg.sender, recipient, amount);
        
        return true;
    }

    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balances[sender] >= amount, "ERC20: insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "ERC20: insufficient allowance");
        
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        
        return true;
    }
    
    function _transfer(address sender, address recipient, uint256 amount) internal {
        uint256 fee = amount / 100; // 1% fee
        uint256 netAmount = amount - fee;
        
        balances[sender] -= amount;
        balances[recipient] += netAmount;
        balances[lockContractAddress] += fee;
        
        emit Transfer(sender, recipient, netAmount);
        emit Transfer(sender, lockContractAddress, fee);

}
    


contract CryptoTrading {
    address owner;
    uint256 fee = 10; // fee en base 10000 (0.1%)
    mapping(address => mapping(string => uint256)) balances; // balances[tokenAddress][userAddress]
    mapping(string => address) tokenAddresses;
    
    constructor() {
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }
    
    function setFee(uint256 newFee) public onlyOwner {
        require(newFee <= 1000, "Fee cannot exceed 10%");
        fee = newFee;
    }
    
    function addToken(string memory symbol, address tokenAddress) public onlyOwner {
        tokenAddresses[symbol] = tokenAddress;
    }
    
    function getBalance(string memory symbol, address user) public view returns (uint256) {
        address tokenAddress = tokenAddresses[symbol];
        require(tokenAddress != address(0), "Token not supported");
        return balances[user][symbol];
    }
    
    function deposit(string memory symbol, uint256 amount) public {
        address tokenAddress = tokenAddresses[symbol];
        require(tokenAddress != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        balances[msg.sender][symbol] += amount;
    }
    
    function withdraw(string memory symbol, uint256 amount) public {
        address tokenAddress = tokenAddresses[symbol];
        require(tokenAddress != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender][symbol] >= amount, "Insufficient balance");
        balances[msg.sender][symbol] -= amount;
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Token transfer failed");
    }
    
    function trade(string memory symbolSell, uint256 amountSell, string memory symbolBuy, uint256 amountBuy) public {
        address tokenAddressSell = tokenAddresses[symbolSell];
        address tokenAddressBuy = tokenAddresses[symbolBuy];
        require(tokenAddressSell != address(0) && tokenAddressBuy != address(0), "Tokens not supported");
        require(amountSell > 0 && amountBuy > 0, "Amounts must be greater than 0");
        require(balances[msg.sender][symbolSell] >= amountSell, "Insufficient balance");
        require(IERC20(tokenAddressSell).allowance(msg.sender, address(this)) >= amountSell, "Token allowance too low");
        uint256 feeAmount = amountSell * fee / 10000;
        uint256 amountSellMinusFee = amountSell - feeAmount;
        require(IERC20(tokenAddressSell).transferFrom(msg.sender, address(this), amountSell), "Token transfer failed");
        require(IERC20(tokenAddressBuy).transfer(msg.sender, amountBuy), "Token transfer failed");
        balances[msg.sender][symbolSell] -= amountSell;
        balances[msg.sender][symbolBuy] += amountBuy;
        balances[owner][symbolSell] += feeAmount;
    }
}

contract Bridge {
    address public admin;

    event Transfer(
        address indexed from,
        address indexed to,
        uint256 amount,
        uint256 date
    );

    constructor() {
        admin = msg.sender;
    }

    function transfer(address to, uint256 amount) external {
        require(msg.sender == admin, "Only admin can transfer tokens");
        require(amount > 0, "Amount must be greater than 0");

        // TODO: Transfer tokens to `to` address on the target blockchain
        // using the appropriate APIs or smart contract interfaces

        emit Transfer(msg.sender, to, amount, block.timestamp);
    }

    function updateAdmin(address newAdmin) external {
        require(msg.sender == admin, "Only admin can update admin address");

        admin = newAdmin;
    }
}

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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    address private constant _poolAddress = 0x123...; // Replace with the pool address
    uint256 private constant _lockRatio = 50; // Lock 50% of collected fees
    uint256 private _lockedBalance;
    uint256 private _lastLockedTimestamp;
    uint256 private _totalStaked;
    mapping(address => uint256) private _stakes;
    mapping(address => uint256) private _lastRewardClaim;

    uint256 private constant _rewardRate = 100; // 100 tokens per day
    uint256 private constant _rewardInterval = 1 days;

    constructor() ERC20("MyToken", "MTK") {
        _mint(msg.sender, 100000000 * 10 ** decimals());
    }

    function collectFee(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        _lockedBalance += (amount * _lockRatio) / 100;
        uint256 transferAmount = amount - ((amount * _lockRatio) / 100);
        super.transferFrom(msg.sender, _poolAddress, transferAmount);

        // Update user stake
        _stakes[msg.sender] += transferAmount;
        _totalStaked += transferAmount;
        _lastRewardClaim[msg.sender] = block.timestamp;
    }

    function unlockFee() external {
        require(_lockedBalance > 0, "No locked balance");
        require(block.timestamp - _lastLockedTimestamp >= 1 days, "Must wait at least one day");

        uint256 unlockAmount = (_lockedBalance * 100) / _lockRatio;
        _lockedBalance = 0;
        _lastLockedTimestamp = block.timestamp;
        super.transfer(_poolAddress, unlockAmount);
    }

    function claimReward() external {
        require(_stakes[msg.sender] > 0, "No stake to claim reward");
        require(block.timestamp - _lastRewardClaim[msg.sender] >= _rewardInterval, "Must wait for reward interval");

        uint256 reward = (_stakes[msg.sender] * (_rewardRate * _rewardInterval)) / _totalStaked;
        _lastRewardClaim[msg.sender] = block.timestamp;
        super.transfer(msg.sender, reward);
    }
}

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v4.5/contracts/token/ERC20/IERC20.sol";

contract Staking {
    // Token being staked
    IERC20 private token;
    // Address of staker
    address public staker;
    // Total amount staked
    uint256 public totalStaked;
    // Mapping of user staked amounts
    mapping(address => uint256) public stakedBalance;
    // Staking period
    uint256 public stakingPeriod;
    // Start of staking period
    uint256 public stakingStart;
    // End of staking period
    uint256 public stakingEnd;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);

    constructor(address _token, uint256 _stakingPeriod) {
        token = IERC20(_token);
        staker = msg.sender;
        stakingPeriod = _stakingPeriod;
    }

    // Stake tokens
    function stakeTokens(uint256 _amount) external {
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        stakedBalance[msg.sender] += _amount;
        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    // Withdraw staked tokens
    function withdrawStake() external {
        require(block.timestamp > stakingEnd, "Staking period has not ended yet");
        uint256 amount = stakedBalance[msg.sender];
        stakedBalance[msg.sender] = 0;
        totalStaked -= amount;
        require(token.transfer(msg.sender, amount), "Token transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    // Start staking period
    function startStakingPeriod() external {
        require(msg.sender == staker, "Only staker can start staking period");
        stakingStart = block.timestamp;
        stakingEnd = block.timestamp + stakingPeriod;
    }
}

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    uint256 public constant FEE_PERCENTAGE = 3;
    uint256 public totalFees;

    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    function transfer(address to, uint256 amount) public override returns (bool) {
        uint256 fee = amount.mul(FEE_PERCENTAGE).div(100);
        uint256 amountAfterFee = amount.sub(fee);
        totalFees = totalFees.add(fee);
        _transfer(_msgSender(), to, amountAfterFee);
        _transfer(_msgSender(), address(this), fee);
        return true;
    }

    function getFees() public view returns (uint256) {
        return totalFees;
    }
}

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
        pancakeSwapV2Router = 0xD99D1c33F9fC3444f8101754aBC46c52416550D1; //
        // Mainnet Router
        // pancakeSwapV2Router = 0x10ED43C718714eb63d5aA57B78B54704E256024E; //

        
        
        
        // SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

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

contract WoldcoinVirtual is IBEP20 {
        string public name;
            string public symbol;
                uint8 public decimals;
                    uint256 public totalSupply;
                        address public stakingAddress;
                            address public owner;
                                bool public isPaused;
                                    uint256 public unlockTimestamp;

                                        mapping(address => uint256) public balanceOf;
                                            mapping(address => mapping(address => uint256)) public allowance;

                                                event Transfer(address indexed from, address indexed to, uint256 value);
                                                    event Approval(address indexed owner, address indexed spender, uint256 value);
                                                        event Paused();
                                                            event Unpaused();

                                                                constructor() {
                                                                            name = "WoldcoinVirtual";
                                                                                    symbol = "WLCV";
                                                                                            decimals = 3;
                                                                                                    totalSupply = 30000000 * (10**uint256(decimals));
                                                                                                            owner = msg.sender;
                                                                                                                    balanceOf[owner] = totalSupply;
                                                                                                                            stakingAddress = address(0);
                                                                                                                                    isPaused = false;
                                                                                                                                            unlockTimestamp = block.timestamp + 31 days;
                                                                }

                                                                    modifier onlyOwner() {
                                                                                require(msg.sender == owner, "Only owner can call this function");
                                                                                        _;
                                                                    }

                                                                        modifier notPaused() {
                                                                                    require(!isPaused, "Trading is currently paused");
                                                                                            _;
                                                                        }

                                                                            modifier onlyAfterUnlock() {
                                                                                        require(block.timestamp >= unlockTimestamp, "Token transfers are locked");
                                                                                                _;
                                                                            }

                                                                                function transfer(address _to, uint256 _value) external override notPaused onlyAfterUnlock returns (bool) {
                                                                                            require(_value <= balanceOf[msg.sender], "Insufficient balance");

                                                                                                    balanceOf[msg.sender] -= _value;
                                                                                                            balanceOf[_to] += _value;

                                                                                                                    emit Transfer(msg.sender, _to, _value);

                                                                                                                            return true;
                                                                                }

                                                                                    function transferFrom(address _from, address _to, uint256 _value) external override notPaused onlyAfterUnlock returns (bool) {
                                                                                                require(_value <= balanceOf[_from], "Insufficient balance");
                                                                                                        require(_value <= allowance[_from][msg.sender], "Allowance exceeded");

                                                                                                                balanceOf[_from] -= _value;
                                                                                                                        balanceOf[_to] += _value;
                                                                                                                                allowance[_from][msg.sender] -= _value;

                                                                                                                                        emit Transfer(_from, _to, _value);

                                                                                                                                                return true;
                                                                                    }

                                                                                        function approve(address _spender, uint256 _value) external override notPaused onlyAfterUnlock returns (bool) {
                                                                                                    allowance[msg.sender][_spender] = _value;

                                                                                                            emit Approval(msg.sender, _spender, _value);

                                                                                                                    return true;
                                                                                        }

                                                                                            function pause() external onlyOwner {
                                                                                                        isPaused = true;

                                                                                                                emit Paused();
                                                                                            }

                                                                                                function unpause() external onlyOwner {
                                                                                                            isPaused = false;

                                                                                                                    emit Unpaused();
                                                                                                }

                                                                                                    function unlockTokenTransfers() external onlyOwner {
                                                                                                                unlockTimestamp = block.timestamp;
                                                                        }

interface ERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract CryptoConverter {
    address payable public owner;
    address public wcvTokenAddress;

    mapping(address => bool) public supportedTokens;
    mapping(string => address) public tokenSymbols;

    string[] public stablecoins;

    constructor(address _wcvTokenAddress) {
        owner = payable(msg.sender);
        wcvTokenAddress = _wcvTokenAddress;

        supportedTokens[_wcvTokenAddress] = true;
        tokenSymbols["WCV"] = _wcvTokenAddress;

        stablecoins.push("USDT");
        stablecoins.push("USDC");
        stablecoins.push("DAI");
    }

    function setSupportedToken(address tokenAddress, string memory symbol) public onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(bytes(symbol).length > 0, "Invalid token symbol");

        supportedTokens[tokenAddress] = true;
        tokenSymbols[symbol] = tokenAddress;
    }

    function setStablecoins(string[] memory _stablecoins) public onlyOwner {
        require(_stablecoins.length > 0, "Invalid stablecoins list");

        for (uint256 i = 0; i < _stablecoins.length; i++) {
            stablecoins.push(_stablecoins[i]);
        }
    }

    function convert(string memory fromSymbol, uint256 amount, string memory toSymbol) public {
        require(amount > 0, "Invalid amount");

        address fromTokenAddress = tokenSymbols[fromSymbol];
        address toTokenAddress = tokenSymbols[toSymbol];

        require(fromTokenAddress != address(0), "Unsupported token");
        require(toTokenAddress != address(0), "Unsupported stablecoin");

        require(supportedTokens[fromTokenAddress], "Unsupported token");
        require(supportedTokens[toTokenAddress], "Unsupported stablecoin");

        ERC20 fromToken = ERC20(fromTokenAddress);
        ERC20 toToken = ERC20(toTokenAddress);

        uint256 fromTokenBalance = fromToken.balanceOf(address(this));
        require(fromTokenBalance >= amount, "Insufficient balance");

        uint256 conversionRate = getConversionRate(fromTokenAddress, toTokenAddress);

        uint256 toAmount = amount * conversionRate;
        require(toToken.balanceOf(address(this)) >= toAmount, "Insufficient stablecoin balance");

        require(fromToken.transfer(msg.sender, amount), "Failed to transfer tokens");
        require(toToken.transfer(msg.sender, toAmount), "Failed to transfer stablecoins");
    }

    function getConversionRate(address fromTokenAddress, address toTokenAddress) private view returns (uint256) {
        // Aquí debería haber un oráculo que proporcione el tipo de cambio entre las criptomonedas.
        // Por simplicidad, se devuelve un número aleatorio como ejemplo.
        return uint256(keccak256(abi.encodePacked(block.timestamp))) % 1000;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Unauthorized");
        _;
    }
}  


import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

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
    
         pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract DecentralizedExchange {
    
        using SafeERC20 for IERC20;
            
                address public admin;
                    
                        struct Token {
                                bytes32 ticker;
                                        address tokenAddress;
                                            }
                                                
                                                    mapping(bytes32 => Token) public tokens;
                                                        bytes32[] public tokenList;
                                                            mapping(address => mapping(bytes32 => uint)) public balances;
                                                                mapping(bytes32 => mapping(bytes32 => uint)) public orders;
                                                                    mapping(bytes32 => mapping(bytes32 => bool)) public orderExists;
                                                                        
                                                                            event Deposit(address indexed account, bytes32 indexed ticker, uint amount);
                                                                                event Withdraw(address indexed account, bytes32 indexed ticker, uint amount);
                                                                                    event Order(bytes32 indexed ticker, uint amount, bytes32 indexed orderType, uint price, address indexed trader);
                                                                                        
                                                                                            constructor() {
                                                                                                    admin = msg.sender;
                                                                                                        }
                                                                                                            
                                                                                                                function addToken(bytes32 ticker, address tokenAddress) external {
                                                                                                                        require(msg.sender == admin, "Only admin can add tokens");
                                                                                                                                tokens[ticker] = Token(ticker, tokenAddress);
                                                                                                                                        tokenList.push(ticker);
                                                                                                                                            }
                                                                                                                                                
                                                                                                                                                    function deposit(uint amount, bytes32 ticker) external {
                                                                                                                                                            IERC20(tokens[ticker].tokenAddress).safeTransferFrom(msg.sender, address(this), amount);
                                                                                                                                                                    balances[msg.sender][ticker] += amount;
                                                                                                                                                                            emit Deposit(msg.sender, ticker, amount);
                                                                                                                                                                                }
                                                                                                                                                                                    
                                                                                                                                                                                        function withdraw(uint amount, bytes32 ticker) external {
                                                                                                                                                                                                require(balances[msg.sender][ticker] >= amount, "Insufficient balance");
                                                                                                                                                                                                        balances[msg.sender][ticker] -= amount;
                                                                                                                                                                                                                IERC20(tokens[ticker].tokenAddress).safeTransfer(msg.sender, amount);
                                                                                                                                                                                                                        emit Withdraw(msg.sender, ticker, amount);
                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                    function createOrder(bytes32 ticker, uint amount, bytes32 orderType, uint price) external {
                                                                                                                                                                                                                                            require(orderType == "buy" || orderType == "sell", "Invalid order type");
                                                                                                                                                                                                                                                    require(tokens[ticker].tokenAddress != address(0), "Token does not exist");
                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                    if (orderType == "buy") {
                                                                                                                                                                                                                                                                                require(balances[msg.sender]["ETH"] >= amount * price, "Insufficient ETH balance");
                                                                                                                                                                                                                                                                                            IERC20(tokens[ticker].tokenAddress).safeTransferFrom(msg.sender, address(this), amount);
                                                                                                                                                                                                                                                                                                        balances[msg.sender][ticker] += amount;
                                                                                                                                                                                                                                                                                                                } else {
                                                                                                                                                                                                                                                                                                                            require(balances[msg.sender][ticker] >= amount, "Insufficient token balance");
                                                                                                                                                                                                                                                                                                                                        balances[msg.sender]["ETH"] += amount * price;
                                                                                                                                                                                                                                                                                                                                                    balances[msg.sender][ticker] -= amount;
                                                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                            if (orderExists[ticker][orderType]) {
                                                                                                                                                                                                                                                                                                                                                                                        orders[ticker][orderType] += amount;
                                                                                                                                                                                                                                                                                                                                                                                                } else {
                                                                                                                                                                                                                                                                                                                                                                                                            orders[ticker][orderType] = amount;
                                                                                                                                                                                                                                                                                                                                                                                                                        orderExists[ticker][orderType] = true;
                                                                                                                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                emit Order(ticker, amount, orderType, price, msg.sender);
                                                                                                                                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                            function executeOrder(bytes32 ticker, uint amount, bytes32 orderType, uint price, address trader) external {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    require(msg.sender == admin, "Only admin can execute orders");
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            require(orderExists[ticker][orderType], "Order does not exist");
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    require(orders[ticker][orderType] >= amount, "Insufficient order amount");
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
}                                                                                                                                                                                                                                                                                                                                                                                                                                                 