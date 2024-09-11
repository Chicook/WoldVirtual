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
    
    function unlockSupply() external {
        require(msg.sender == lockContractAddress, "MyToken: caller is not the lock contract");
        
        uint256 amount = getLockedAmount();
        require(amount > 0, "MyToken: no tokens to unlock");
        
        balances[lockContractAddress] -= amount;
        balances[msg
