// SPDX-License-Identifier: MIT
pragma solidity 0.8.20;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WoldcoinVirtual is Ownable {
    using SafeMath for uint256;

        string public name = "WoldcoinVirtual";
        string public symbol = "WLCV";
        uint8 public decimals = 3;
        uint256 public totalSupply = 30000000000 * 10**uint256(decimals);

                        
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

         return true;
                    
                     }
}
