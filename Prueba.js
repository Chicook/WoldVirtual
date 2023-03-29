const web3 = new Web3(Web3.givenProvider || "http://localhost:8545");

const contractAddress = "0x123..."; // Replace with your contract address
const contractABI = [/* Replace with your contract ABI */];

const contract = new web3.eth.Contract(contractABI, contractAddress);

const accounts = await web3.eth.requestAccounts();
const account = accounts[0];

const stakedBalanceElement = document.getElementById("stakedBalance");
const claimableRewardsElement = document.getElementById("claimableRewards");
const totalStakedBalanceElement = document.getElementById("totalStakedBalance");

async function updateUI() {
  const stakedBalance = await contract.methods.balanceOf(account).call();
  stakedBalanceElement.textContent = stakedBalance;

  const claimableRewards = await contract.methods.claimableRewards(account).call();
  claimableRewardsElement.textContent = claimableRewards;

  const totalStakedBalance = await contract.methods.totalStaked().call();
  totalStakedBalanceElement.textContent = totalStakedBalance;
}

async function stake() {
  const amount = document.getElementById("amount").value;
  await contract.methods.st
