pragma solidity ^0.8.0;

contract WoldcoinVirtual {
    string public constant name = "WoldcoinVirtual";
    string public constant symbol = "WDCV";
    uint8 public constant decimals = 9;
    uint256 public constant INITIAL_SUPPLY = 30_000_000_000 * 10 ** decimals;
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
