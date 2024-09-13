pragma solidity ^0.8.0;

interface ERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract CryptoConverter {
    address payable public owner;
    address public wcvTokenAddress;

    mapping(address => bool) public supportedTokens;
    mapping(string => address) public tokenSymbols;

    string[] public stablecoins;

    constructor(address _wcvTokenAddress) {
        owner = payable(msg.sender);
        wcvTokenAddress = _wcvTokenAddress;

        supportedTokens[_wcvTokenAddress] = true;
        tokenSymbols["WCV"] = _wcvTokenAddress;

        stablecoins.push("USDT");
        stablecoins.push("USDC");
        stablecoins.push("DAI");
    }

    function setSupportedToken(address tokenAddress, string memory symbol) public onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(bytes(symbol).length > 0, "Invalid token symbol");

        supportedTokens[tokenAddress] = true;
        tokenSymbols[symbol] = tokenAddress;
    }

    function setStablecoins(string[] memory _stablecoins) public onlyOwner {
        require(_stablecoins.length > 0, "Invalid stablecoins list");

        for (uint256 i = 0; i < _stablecoins.length; i++) {
            stablecoins.push(_stablecoins[i]);
        }
    }

    function convert(string memory fromSymbol, uint256 amount, string memory toSymbol) public {
        require(amount > 0, "Invalid amount");

        address fromTokenAddress = tokenSymbols[fromSymbol];
        address toTokenAddress = tokenSymbols[toSymbol];

        require(fromTokenAddress != address(0), "Unsupported token");
        require(toTokenAddress != address(0), "Unsupported stablecoin");

        require(supportedTokens[fromTokenAddress], "Unsupported token");
        require(supportedTokens[toTokenAddress], "Unsupported stablecoin");

        ERC20 fromToken = ERC20(fromTokenAddress);
        ERC20 toToken = ERC20(toTokenAddress);

        uint256 fromTokenBalance = fromToken.balanceOf(address(this));
        require(fromTokenBalance >= amount, "Insufficient balance");

        uint256 conversionRate = getConversionRate(fromTokenAddress, toTokenAddress);

        uint256 toAmount = amount * conversionRate;
        require(toToken.balanceOf(address(this)) >= toAmount, "Insufficient stablecoin balance");

        require(fromToken.transfer(msg.sender, amount), "Failed to transfer tokens");
        require(toToken.transfer(msg.sender, toAmount), "Failed to transfer stablecoins");
    }

    function getConversionRate(address fromTokenAddress, address toTokenAddress) private view returns (uint256) {
        // Aquí debería haber un oráculo que proporcione el tipo de cambio entre las criptomonedas.
        // Por simplicidad, se devuelve un número aleatorio como ejemplo.
        return uint256(keccak256(abi.encodePacked(block.timestamp))) % 1000;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Unauthorized");
        _;
    }
}
