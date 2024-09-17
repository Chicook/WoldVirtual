contract AvatarMovementContract {
    address public owner;
    mapping(address => bool) public avatarsAtLocation;

    event AvatarMoved(address indexed avatar, string location);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function avatarMoved(string memory location) public {
        require(!avatarsAtLocation[msg.sender], "Avatar is already at this location");
        
        // Perform actions related to avatar movement (e.g., update state, emit events)
        avatarsAtLocation[msg.sender] = true;
        
        // Emit an event to log the avatar movement
        emit AvatarMoved(msg.sender, location);
    }

    // Additional functions and logic can be added based on your requirements
}
