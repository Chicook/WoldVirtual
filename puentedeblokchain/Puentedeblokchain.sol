pragma solidity ^0.8.0;

interface ERC20 {
    function transfer(address to, uint256 value) external returns (bool);
    function balanceOf(address who) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
    function approve(address spender, uint256 value) external returns (bool);
}

contract TokenBridge {
    mapping (address => uint256) public balances;
    mapping (address => mapping (address => uint256)) public allowed;

    address public token;
    uint256 public rate;
    uint256 public commission = 10;
    address public commissionWallet;
    
    mapping (uint256 => address) public supportedTokens;
    uint256 public supportedTokensCount;
    
    constructor(address _token, uint256 _rate, address _commissionWallet) {
        token = _token;
        rate = _rate;
        commissionWallet = _commissionWallet;
        
        // Agregar la red principal de Bitcoin
        supportedTokensCount = 1;
        supportedTokens[0] = 0x0000000000000000000000000000000000000000; // Dirección de Bitcoin
    }
    
    function transferToken(address _token, address _to, uint256 _value) private {
        ERC20(_token).transfer(_to, _value);
    }
    
    function transferFromToken(address _token, address _from, address _to, uint256 _value) private {
        ERC20(_token).transferFrom(_from, _to, _value);
    }
    
    function setRate(uint256 _rate) public {
        rate = _rate;
    }
    
    function setCommission(uint256 _commission) public {
        commission = _commission;
    }
    
    function setCommissionWallet(address _commissionWallet) public {
        commissionWallet = _commissionWallet;
    }
    
    function addSupportedToken(address _token) public {
        supportedTokens[supportedTokensCount] = _token;
        supportedTokensCount++;
    }
    
    function convertTokens(uint256 _amount, uint256 _tokenIndex) public {
        require(supportedTokens[_tokenIndex] != address(0), "Token no soportado");
        
        // Transferir tokens al contrato
        transferFromToken(token, msg.sender, address(this), _amount);
        
        // Convertir tokens
        uint256 convertedAmount = _amount * rate;
        uint256 commissionAmount = (convertedAmount * commission) / 1000;
        uint256 transferAmount = convertedAmount - commissionAmount;
        
        // Transferir tokens convertidos
        transferToken(supportedTokens[_tokenIndex], msg.sender, transferAmount);
        
        // Transferir comisión
        transferToken(supportedTokens[_tokenIndex], commissionWallet, commissionAmount);
    }
}
