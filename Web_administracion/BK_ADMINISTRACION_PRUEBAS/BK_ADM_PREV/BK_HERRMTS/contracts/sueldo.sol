contract sueldo {
    address public owner;
    mapping(address => uint256) public salaries;

    event SalaryPaid(address indexed employee, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function setSalary(address employee, uint256 amount) external onlyOwner {
        salaries[employee] = amount;
    }

    function paySalary() external {
        uint256 salary = salaries[msg.sender];
        require(salary > 0, "No salary set for the caller");

        // Consider additional conditions and security checks as needed

        // Transfer the salary in cryptocurrency (replace 'tokenTransferFunction' with the actual transfer function)
        // tokenTransferFunction(msg.sender, salary);

        emit SalaryPaid(msg.sender, salary);
    }
}
