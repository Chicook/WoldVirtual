// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC20.sol"; // Importa el contrato del token ERC20

contract TokenLock {
        address public owner;
            address public tokenAddress;
                uint256 public totalTokens;
                    uint256 public releaseAmount;
                        uint256 public releaseInterval;
                            uint256 public lastReleaseTime;
                                
                                    modifier onlyOwner() {
                                                require(msg.sender == owner, "Solo el propietario puede llamar a esta función");
                                                        _;
                                    }

                                        constructor(
                                                    address _tokenAddress,
                                                            uint256 _totalTokens,
                                                                    uint256 _releaseAmount,
                                                                            uint256 _releaseInterval
                                        ) {
                                                    owner = msg.sender;
                                                            tokenAddress = _tokenAddress;
                                                                    totalTokens = _totalTokens;
                                                                            releaseAmount = _releaseAmount;
                                                                                    releaseInterval = _releaseInterval;
                                                                                            lastReleaseTime = block.timestamp;
                                        }

                                            function releaseTokens() public onlyOwner {
                                                        require(block.timestamp >= lastReleaseTime + releaseInterval, "Aún no ha pasado el tiempo suficiente para la liberación");
                                                                
                                                                        ERC20 token = ERC20(tokenAddress);
                                                                                uint256 balance = token.balanceOf(address(this));
                                                                                        
                                                                                                require(balance >= releaseAmount, "El contrato no tiene suficientes tokens para la liberación");
                                                                                                        
                                                                                                                lastReleaseTime = block.timestamp;
                                                                                                                        token.transfer(owner, releaseAmount);
                                            }
}


                                            }
                                        }
                                        )
                                    }
}