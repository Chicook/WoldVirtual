// Get the form and result elements from the HTML document
const form = document.getElementById("converter-form");
const result = document.getElementById("result");

// Define the conversion rates for each supported pair of tokens
const conversionRates = {
  "WCV_USDT": 0.5,
  "ETH_USDT": 2000,
  "BTC_USDT": 50000,
  // add more conversion rates here
};

// Define the contract address and ABI for the Solidity contract
const contractAddress = "0x1234567890abcdef";
const contractABI = [
  // add the contract ABI here
];

// Create a new instance of the web3.js library
const web3 = new Web3(window.ethereum);

// Create a new instance of the contract using the address and ABI
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Add an event listener to the form submit button
form.addEventListener("submit", async (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();
  
  // Get the selected crypto and stablecoin from the form
  const fromCrypto = form.elements["from-crypto"].value;
  const toStablecoin = form.elements["to-stablecoin"].value;
  
  // Get the amount to convert from the form
  const amount = form.elements["amount"].value;
  
  // Calculate the equivalent amount in the stablecoin using the conversion rate
  const conversionRateKey = `${fromCrypto}_${toStablecoin}`;
  const conversionRate = conversionRates[conversionRateKey];
  const equivalentAmount = amount * conversionRate;
  
  // Show the conversion result to the user
  result.textContent = `You will receive ${equivalentAmount} ${toStablecoin} for ${amount} ${fromCrypto}. Please confirm the transaction in your wallet.`;
  
  // Call the Solidity function to initiate the transaction
  const accounts = await web3.eth.getAccounts();
  const result = await contract.methods.convert(fromCrypto, toStablecoin, amount).send({
    from: accounts[0],
    value: 0,
  });
  
  // Show a success message to the user
  result.textContent = `Transaction successful! You have received ${equivalentAmount} ${toStablecoin}.`;
});
