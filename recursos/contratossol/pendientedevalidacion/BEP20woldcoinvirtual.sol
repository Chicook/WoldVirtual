// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IBEP20 {
  
  function totalSupply() external view returns (uint256);
 function balanceOf(address account) external view returns (uint256);
     function transfer(address recipient, uint256 amount) external returns (bool);
}

contract WoldcoinVirtual is IBEP20 {
string public name = "WoldcoinVirtual";
 string public symbol = "WCV";
 uint8 public decimals = 3;
uint256 public totalSupply = 30000000 * (3**uint256(decimals));
mapping(address => uint256) public balanceOf;

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

          