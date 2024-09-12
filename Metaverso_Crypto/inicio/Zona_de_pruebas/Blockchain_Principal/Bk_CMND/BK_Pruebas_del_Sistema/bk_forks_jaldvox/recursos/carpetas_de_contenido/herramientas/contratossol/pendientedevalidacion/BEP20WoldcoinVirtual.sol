// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract WoldcoinVirtual is ERC20 {
        address private owner;
            bool private isTradingEnabled;

                modifier onlyOwner() {
                            require(msg.sender == owner, "Only the contract owner can call this function.");
                                    _;
                }

                    modifier tradingEnabled() {
                                require(isTradingEnabled, "Trading is currently disabled.");
                                        _;
                    }

                        constructor() ERC20("WoldcoinVirtual", "WLCV") {
                                    owner = msg.sender;
                                            isTradingEnabled = false;
                                                    _mint(msg.sender, 300000000 * 10 ** decimals());
                        }

                            function enableTrading() external onlyOwner {
                                        isTradingEnabled = true;
                            }

                                function transfer(address recipient, uint256 amount) public override tradingEnabled returns (bool) {
                                            return super.transfer(recipient, amount);
                                }

                                    function transferFrom(address sender, address recipient, uint256 amount) public override tradingEnabled returns (bool) {
                                                return super.transferFrom(sender, recipient, amount);
                                    }

                                        function approve(address spender, uint256 amount) public override tradingEnabled returns (bool) {
                                                    return super.approve(spender, amount);
                                        }

                                            function increaseAllowance(address spender, uint256 addedValue) public override tradingEnabled returns (bool) {
                                                        return super.increaseAllowance(spender, addedValue);
                                            }

                                                function decreaseAllowance(address spender, uint256 subtractedValue) public override tradingEnabled returns (bool) {
                                                            return super.decreaseAllowance(spender, subtractedValue);
                                                }

                                                    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override tradingEnabled {
                                                                super._beforeTokenTransfer(from, to, amount);
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