pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

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

   
