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
}
}