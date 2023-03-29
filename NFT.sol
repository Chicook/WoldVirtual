// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract NFTMarketplace {
    
    // Variables
    uint256 public totalSupply;
    uint256 public maxNFTs = 30000000;
    uint256 public primaryCost = 1000000000000000; // 0.001 WLCV
    address public poolAddress;
    
    // Structs
    struct NFT {
        uint256 id;
        address owner;
        uint256 price;
        bool forSale;
    }
    
    // Arrays
    NFT[] public nfts;
    
    // Events
    event NewNFT(uint256 indexed id, address indexed owner, uint256 price, bool forSale);
    event NFTSold(uint256 indexed id, address indexed owner, uint256 price);
    
    // Modifiers
    modifier onlyOwner(uint256 _id) {
        require(msg.sender == nfts[_id].owner, "You are not the owner of this NFT.");
        _;
    }
    
    modifier forSale(uint256 _id) {
        require(nfts[_id].forSale == true, "This NFT is not for sale.");
        _;
    }
    
    modifier notForSale(uint256 _id) {
        require(nfts[_id].forSale == false, "This NFT is already for sale.");
        _;
    }
    
    modifier validPrice(uint256 _price) {
        require(_price > 0, "Price must be greater than 0.");
        _;
    }
    
    modifier underMaxNFTs() {
        require(totalSupply < maxNFTs, "The maximum number of NFTs has already been reached.");
        _;
    }
    
    // Constructor
    constructor(address _poolAddress) {
        poolAddress = _poolAddress;
    }
    
    // Functions
    
    function mint() public payable validPrice(msg.value) underMaxNFTs {
        uint256 _id = totalSupply;
        NFT memory newNFT = NFT(_id, msg.sender, msg.value, true);
        nfts.push(newNFT);
        totalSupply++;
        emit NewNFT(_id, msg.sender, msg.value, true);
    }
    
    function buyNFT(uint256 _id) public payable forSale(_id) validPrice(msg.value) {
        require(msg.sender != nfts[_id].owner, "You already own this NFT.");
        require(msg.value == nfts[_id].price, "The value sent does not match the NFT price.");
        address payable oldOwner = payable(nfts[_id].owner);
        oldOwner.transfer(msg.value);
        nfts[_id].owner = msg.sender;
        nfts[_id].forSale = false;
        emit NFTSold(_id, msg.sender, msg.value);
        if(totalSupply == 1) {
            poolAddress.transfer(primaryCost);
        } else {
            uint256 salePrice = msg.value - primaryCost;
            uint256 rewardAmount = salePrice / 2;
            poolAddress.transfer(rewardAmount);
        }
    }
    
    function sellNFT(uint256 _id, uint256 _price) public onlyOwner(_id) notForSale(_id) validPrice(_price) {
        nfts[_id].price = _price;
        nfts[_id].forSale = true;
    }
    
    function withdraw() public {
        require(msg.sender == poolAddress, "You are not authorized to withdraw from this contract.");
        payable(poolAddress).transfer(address(this).balance);
