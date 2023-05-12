// Configurar web3.js con la dirección y la clave privada de tu billetera Ethereum
const Web3 = require("web3");
const web3 = new Web3(
  new Web3.providers.HttpProvider("https://rinkeby.infura.io/v3/<tu-proyecto-ID>")
);
const account = "<tu-direccion-Ethereum>";
const privateKey = "<tu-clave-privada>";

// Crear una instancia del contrato Solidity
const abi = [...]; // El ABI generado por el compilador de Solidity
const address = "<la-direccion-del-contrato-en-la-red-Ethereum>";
const contract = new web3.eth.Contract(abi, address);

// Función para obtener el saldo de WLCV del usuario
async function getBalance() {
  const balance = await contract.methods.balanceOf(account).call();
  document.getElementById("balance").innerText = balance;
}

// Función para depositar WLCV en el pool de liquidez
async function deposit() {
  const amount = document.getElementById("deposit-amount").value;
  const result = await contract.methods.deposit(amount).send({
    from: account,
    gas: 200000,
  });
  console.log(result); // Imprimir el resultado de la transacción en la consola
}

// Función para retirar WLCV del pool de liquidez
async function withdraw() {
  const amount = document.getElementById("withdraw-amount").value;
  const result = await contract.methods.withdraw(amount).send({
    from: account,
    gas: 200000,
  });
  console.log(result); // Imprimir el resultado de la transacción en la consola
}

// Función para solicitar un préstamo
async function requestLoan() {
  const amount = document.getElementById("loan-amount").value;
  const result = await contract.methods.requestLoan(amount).send({
    from: account,
    gas: 200000,
  });
  console.log(result); // Imprimir el resultado de la transacción en la consola
}

// Función para pagar un préstamo
async function payLoan() {
  const amount = document.getElementById("loan-payment-amount").value;
  const result = await contract.methods.payLoan(amount).send({
    from: account,
    gas: 200000,
  });
  console.log(result); // Imprimir el resultado de la transacción en la consola
}

// Actualizar el saldo de WLCV del usuario al cargar la página
window.addEventListener("load", async () => {
  await getBalance();
});
