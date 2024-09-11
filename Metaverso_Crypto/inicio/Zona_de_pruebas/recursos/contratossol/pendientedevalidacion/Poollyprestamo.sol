// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

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
