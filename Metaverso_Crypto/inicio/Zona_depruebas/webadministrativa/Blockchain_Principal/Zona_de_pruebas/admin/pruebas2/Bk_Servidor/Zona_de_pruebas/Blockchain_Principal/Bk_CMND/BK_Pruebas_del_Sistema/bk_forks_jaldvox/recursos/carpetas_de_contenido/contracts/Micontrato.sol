import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@pancakeswap/pancake-swap-lib/contracts/token/BEP20/IBEP20.sol";


contract  Micontrato{

using SafeMath for uint256;
using SafeERC20 for IERC20;
    using SafeMath for uint256;
    using SafeERC20 for IERC20;
event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
        event EmergencyWithdrawal(address indexed user, uint256 amount);

constructor(){
    btcbAddress = 0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c;
    allowedWallet = 0xA8E670588bbB447c1e98557C64f740016d908085;
    name = "WoldcoinVirtual";
    symbol = "WCV";
    decimals = 3;
    totalSupply = 30000000;  
}
  function transfer(address to, uint256 amount) external {
    require(amount > 0, "Amount must be greater than 0");
    require(balanceOf[msg.sender] >= amount, "Insufficient balance");

    balanceOf[msg.sender] -= amount;
    balanceOf[to] += amount;

    emit Transfer(msg.sender, to, amount);
  }

event Transfer(address indexed from, address indexed to, uint256 amount);
bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
using SafeMath for uint256;
using SafeERC20 for IERC20;
 address public btcbAddress = 0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c;
 address public allowedWallet
=0xA8E670588bbB447c1e98557C64f740016d908085;
string public name = "WoldcoinVirtual";
 string public symbol = "WCV";
 uint8 public decimals = 3;
uint256 public totalSupply = 30000000  ;
mapping(address => uint256) public balanceOf;
    mapping(address => uint256) public liquidityPool;
    event LiquidityAdded(address indexed provider, uint256 amount);
    event LiquidityRemoved(address indexed provider, uint256 amount);
    function addLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        balanceOf[msg.sender] -= amount;
        totalSupply += amount;
        liquidityPool[msg.sender] += amount;
        emit LiquidityAdded(msg.sender, amount);
    }
    function removeLiquidity(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(liquidityPool[msg.sender] >= amount, "Insufficient liquidity");
        balanceOf[msg.sender] += amount;
        totalSupply -= amount;
        liquidityPool[msg.sender] -= amount;

        emit LiquidityRemoved(msg.sender, amount);
        }
    event LiquidityAddedWithBTCB(address indexed provider, uint256 amount);
    function getTokenPrice() external view returns (uint256) {
    }
}
