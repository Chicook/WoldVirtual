document.addEventListener('DOMContentLoaded', function () {
  initApp();
});

function initApp() {
  console.log('La aplicación se ha inicializado correctamente.');
  // Aquí continuarías con la lógica de tu aplicación
}

// Variables de estado
let isConnected = false;
let balance = 0;

// Referencias a elementos del DOM
const saldoElement = document.getElementById('saldo');
const conectarBtn = document.getElementById('conectarBtn');
const enviarBtn = document.getElementById('enviarBtn');

// Manejadores de eventos
conectarBtn.addEventListener('click', () => {
  if (!isConnected) {
    conectarWallet();
  } else {
    desconectarWallet();
  }
});

enviarBtn.addEventListener('click', () => {
  if (isConnected) {
    enviarETH();
  } else {
    console.log('Primero debes conectar tu wallet.');
  }
});

// Funciones
function conectarWallet() {
  // Aquí implementarías la lógica para conectar la wallet
  isConnected = true;
  console.log('Wallet conectada correctamente.');
  actualizarInterfaz();
}

function desconectarWallet() {
  // Aquí implementarías la lógica para desconectar la wallet
  isConnected = false;
  console.log('Wallet desconectada.');
  actualizarInterfaz();
}

function enviarETH() {
  // Aquí implementarías la lógica para enviar ETH
  console.log('Enviando ETH...');
}

function actualizarInterfaz() {
  // Actualizar la interfaz según el estado actual
  saldoElement.textContent = `${balance} ETH`;
  conectarBtn.textContent = isConnected ? 'Desconectar Wallet' : 'Conectar Wallet';
}
