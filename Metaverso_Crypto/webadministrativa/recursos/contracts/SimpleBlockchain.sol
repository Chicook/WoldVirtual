pragma solidity ^0.8.24;

contract SimpleBlockchain {
    mapping(address => uint256) public balances;

    event Transfer(address indexed from, address indexed to, uint256 value);

    function transfer(address to, uint256 value) external {
        require(balances[msg.sender] >= value, "Saldo insuficiente");
        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
    }
}
