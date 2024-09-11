// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract WoldcoinVirtual {
        string public name = "WoldcoinVirtual";
            string public symbol = "WCV";
                uint8 public decimals = 3;
                    uint256 public totalSupply = 30000000 * (10 ** uint256(decimals));
                        address public owner;
                            uint256 public commission = 1 * (10 ** uint256(decimals - 3)); // 0.001 tokens

                                mapping(address => uint256) public balanceOf;
                                    mapping(address => mapping(address => uint256)) public allowance;
                                        mapping(address => uint256) public stakedBalance;
                                            mapping(address => uint256) public stakedTimestamp;

                                                event Transfer(address indexed from, address indexed to, uint256 value);
                                                    event Approval(address indexed owner, address indexed spender, uint256 value);
                                                        event Staked(address indexed user, uint256 amount);
                                                            event Unstaked(address indexed user, uint256 amount);

                                                                constructor() {
                                                                            owner = msg.sender;
                                                                                    balanceOf[msg.sender] = totalSupply;
                                                                }

                                                                    modifier onlyOwner() {
                                                                                require(msg.sender == owner, "Only owner can call this function");
                                                                                        _;
                                                                    }

                                                                        function transfer(address to, uint256 value) public returns (bool) {
                                                                                    require(to != address(0), "Invalid address");
                                                                                            require(balanceOf[msg.sender] >= value, "Insufficient balance");

                                                                                                    uint256 fee = (value * commission) / (10 ** uint256(decimals));
                                                                                                            uint256 netValue = value - fee;

                                                                                                                    balanceOf[msg.sender] -= value;
                                                                                                                            balanceOf[to] += netValue;
                                                                                                                                    balanceOf[owner] += fee;

                                                                                                                                            emit Transfer(msg.sender, to, netValue);
                                                                                                                                                    emit Transfer(msg.sender, owner, fee);

                                                                                                                                                            return true;
                                                                        }

                                                                            function approve(address spender, uint256 value) public returns (bool) {
                                                                                        allowance[msg.sender][spender] = value;
                                                                                                emit Approval(msg.sender, spender, value);
                                                                                                        return true;
                                                                            }

                                                                                function transferFrom(address from, address to, uint256 value) public returns (bool) {
                                                                                            require(from != address(0), "Invalid address");
                                                                                                    require(to != address(0), "Invalid address");
                                                                                                            require(balanceOf[from] >= value, "Insufficient balance");
                                                                                                                    require(allowance[from][msg.sender] >= value, "Allowance exceeded");

                                                                                                                            uint256 fee = (value * commission) / (10 ** uint256(decimals));
                                                                                                                                    uint256 netValue = value - fee;

                                                                                                                                            balanceOf[from] -= value;
                                                                                                                                                    balanceOf[to] += netValue;
                                                                                                                                                            balanceOf[owner] += fee;
                                                                                                                                                                    allowance[from][msg.sender] -= value;

                                                                                                                                                                            emit Transfer(from, to, netValue);
                                                                                                                                                                                    emit Transfer(from, owner, fee);

                                                                                                                                                                                            return true;
                                                                                }

                                                                                    function stake(uint256 amount) public returns (bool) {
                                                                                                require(amount > 0, "Amount must be greater than zero");
                                                                                                        require(balanceOf[msg.sender] >= amount, "Insufficient balance");

                                                                                                                balanceOf[msg.sender] -= amount;
                                                                                                                        stakedBalance[msg.sender] += amount;
                                                                                                                                stakedTimestamp[msg.sender] = block.timestamp;

                                                                                                                                        emit Staked(msg.sender, amount);

                                                                                                                                                return true;
                                                                                    }

                                                                                        function unstake(uint256 amount) public returns (bool) {
                                                                                                    require(amount > 0, "Amount must be greater than zero");
                                                                                                            require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");
                                                                                                                    require(block.timestamp >= stakedTimestamp[msg.sender] + 1 days, "Staking duration not met");

                                                                                                                            stakedBalance[msg.sender] -= amount;
                                                                                                                                    balanceOf[msg.sender] += amount;
                                                                                                                                            stakedTimestamp[msg.sender] = 0;

                                                                                                                                                    emit Unstaked(msg.sender, amount);

                                                                                                                                                            return true;
                                                                                        }
}

                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
}