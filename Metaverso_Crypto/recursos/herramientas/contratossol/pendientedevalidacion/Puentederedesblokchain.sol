pragma solidity ^0.8.0;

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
