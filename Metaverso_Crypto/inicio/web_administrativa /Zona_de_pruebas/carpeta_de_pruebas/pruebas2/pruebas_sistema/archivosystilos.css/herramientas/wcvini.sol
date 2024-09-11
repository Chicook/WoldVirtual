// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC20.sol";  // Asegúrate de importar el contrato ERC20 que defines

contract WoldcoinVirtual is ERC20 {
    address public owner;  // La dirección del propietario del contrato
        uint256 public stakingStartTime;  // El momento en que comienza el staking
            uint256 public stakingDuration;   // La duración del staking en segundos
                uint256 public annualRelease;     // La cantidad que se libera anualmente
                    uint256 public lastReleaseTime;   // El momento de la última liberación
                        uint256 public transactionFee;    // La comisión por transacción
                            address public liquidityPool;     // Dirección del pool de liquidez
                                uint256 public totalCommissions;  // Total de comisiones recibidas

                                    constructor(
                                            uint256 initialSupply,
                                                    uint256 _stakingDurationYears,
                                                            uint256 _annualRelease,
                                                                    uint256 _transactionFee,
                                                                            address _liquidityPool
                                                                                ) ERC20("WoldcoinVirtual", "WCV") {
                                                                                        owner = msg.sender;
                                                                                                _mint(msg.sender, initialSupply * (10 ** uint256(decimals()))); // Define el suministro inicial con 3 decimales

                                                                                                        stakingDuration = _stakingDurationYears * 365 days; // Convierte la duración a segundos
                                                                                                                annualRelease = _annualRelease * (10 ** uint256(decimals())); // Define la liberación anual con 3 decimales
                                                                                                                        stakingStartTime = block.timestamp; // Inicia el staking en el momento de desplegar el contrato
                                                                                                                                lastReleaseTime = stakingStartTime;
                                                                                                                                        transactionFee = _transactionFee * (10 ** uint256(decimals())); // Define la comisión por transacción con 3 decimales
                                                                                                                                                liquidityPool = _liquidityPool; // Asigna la dirección del pool de liquidez
                                                                                                                                                    }

                                                                                                                                                        // Función para liberar tokens anualmente al pool de liquidez
                                                                                                                                                            function release() external {
                                                                                                                                                                    require(msg.sender == owner, "Solo el propietario puede liberar tokens.");
                                                                                                                                                                            require(block.timestamp >= lastReleaseTime + 1 years, "Aún no puedes liberar tokens este año.");

                                                                                                                                                                                    uint256 timeSinceStart = block.timestamp - stakingStartTime;
                                                                                                                                                                                            require(timeSinceStart <= stakingDuration, "El período de staking ha terminado.");

                                                                                                                                                                                                    uint256 tokensToRelease = annualRelease + totalCommissions; // Agrega comisiones al total
                                                                                                                                                                                                            totalCommissions = 0; // Reinicia el total de comisiones
                                                                                                                                                                                                                    _transfer(address(this), liquidityPool, tokensToRelease);
                                                                                                                                                                                                                            lastReleaseTime = block.timestamp;
                                                                                                                                                                                                                                }

                                                                                                                                                                                                                                    // Función para realizar transferencias con comisión
                                                                                                                                                                                                                                        function transferWithFee(address to, uint256 amount) external returns (bool) {
                                                                                                                                                                                                                                                uint256 feeAmount = (amount * transactionFee) / (10 ** uint256(decimals()));
                                                                                                                                                                                                                                                        uint256 transferAmount = amount - feeAmount;

                                                                                                                                                                                                                                                                require(transferAmount > 0, "La cantidad transferida debe ser mayor que la comisión.");

                                                                                                                                                                                                                                                                        // Transfiere la cantidad principal
                                                                                                                                                                                                                                                                                _transfer(msg.sender, to, transferAmount);

                                                                                                                                                                                                                                                                                        // Agrega la comisión al total de comisiones
                                                                                                                                                                                                                                                                                                totalCommissions += feeAmount;

                                                                                                                                                                                                                                                                                                        return true;
                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                            