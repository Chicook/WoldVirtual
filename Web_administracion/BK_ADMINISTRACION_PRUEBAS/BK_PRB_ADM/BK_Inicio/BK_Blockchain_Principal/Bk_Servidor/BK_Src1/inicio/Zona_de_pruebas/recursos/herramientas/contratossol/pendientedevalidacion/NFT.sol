// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract NFTMarketplace {
    
    struct NFT {
        uint256 id;
        string name;
        string description;
        string imageURI;
        address owner;
        uint256 price;
        bool isPrimarySale;
        bool isSold;
    }
    
    mapping(uint256 => NFT) public nfts;
    uint256 public nftCount;
    address public poolAddress;
    uint256 public poolBalance;
    
    constructor(address _poolAddress) {
        poolAddress = _poolAddress;
    }
    
    function createNFT(string memory _name, string memory _description, string memory _imageURI, uint256 _price) public {
        require(_price > 0, "Price must be greater than zero");
        require(nftCount < 30000000, "Max NFT limit reached");
        nftCount++;
        nfts[nftCount] = NFT(nftCount, _name, _description, _imageURI, msg.sender, _price, true, false);
        uint256 poolFee = 1;
        poolBalance += poolFee;
        payable(poolAddress).transfer(poolFee * 10**18);
    }
    
    function buyNFT(uint256 _nftId) public payable {
        NFT memory nft = nfts[_nftId];
        require(!nft.isSold, "NFT is already sold");
        require(msg.value == nft.price, "Incorrect amount of ETH sent");
        require(nft.isPrimarySale || msg.value >= 1 ether, "Minimum purchase amount for secondary sales is 1 ETH");
        uint256 saleFee = nft.price / 4;
        uint256 ownerPayment = nft.price - saleFee;
        nfts[_nftId].owner = msg.sender;
        nfts[_nftId].isPrimarySale = false;
        nfts[_nftId].isSold = true;
        payable(nfts[_nftId].owner).transfer(ownerPayment);
        poolBalance += saleFee;
        if (nft.isPrimarySale) {
            uint256 poolFee = 1;
            poolBalance += poolFee;
            payable(poolAddress).transfer(poolFee * 10**18);
            if (msg.value > 1 ether) {
                uint256 excess = msg.value - 1 ether;
                payable(msg.sender).transfer(excess);
            }
        } else {
            if (msg.value > saleFee) {
                uint256 excess = msg.value - saleFee;
                payable(msg.sender).transfer(excess);
            }
        }
        if (saleFee > 0) {
            uint256 bnbAmount = (saleFee * 50) / nfts[_nftId].price;
            uint256 usdtAmount = (saleFee * 50) / nfts[_nftId].price;
            payable(poolAddress).transfer(bnbAmount * 10**18);
            payable(poolAddress).transfer(usdtAmount * 10**18);
        }
    }
    
    function getNFT(uint256 _nftId) public view returns (NFT memory) {
        return nfts[_nftId];
    }
    
    function getPoolBalance() public view returns (uint256) {
        return poolBalance;
    }
    
    function withdrawPoolFunds(uint256 _amount) public {
        require(msg
