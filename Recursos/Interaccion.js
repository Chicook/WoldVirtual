const contratoAbi = [/* insertar aquí el ABI del contrato */];
const contratoAddress = '/* insertar aquí la dirección del contrato */';

// Conectar a la red Ethereum usando web3.js
const web3 = new Web3(window.ethereum);

// Obtener la instancia del contrato inteligente
const contrato = new web3.eth.Contract(contratoAbi, contratoAddress);

// Mostrar los detalles del contrato en la página web
const nombreToken = await contrato.methods.name().call();
const simboloToken = await contrato.methods.symbol().call();
const totalSupply = await contrato.methods.totalSupply().call();
const poolGarantia = await contrato.methods.poolGarantia().call();
const poolLiquidez = await contrato.methods.poolLiquidez().call();
const precioInicial = await contrato.methods.precioInicial().call();
const preVenta = await contrato.methods.preVenta().call();
const tokensPreVenta = await contrato.methods.tokensPreVenta().call();
const fechaInicioPreVenta = await contrato.methods.fechaInicioPreVenta().call();
const fechaFinPreVenta = await contrato.methods.fechaFinPreVenta().call();
const precioPreVenta = await contrato.methods.precioPreVenta().call();

document.getElementById('contrato').innerHTML = `
  <p>Nombre del Token: ${nombreToken}</p>
  <p>Símbolo del Token: ${simboloToken}</p>
  <p>Total de Suministro: ${totalSupply}</p>
  <p>Pooll Interno de Garantía: ${poolGarantia}</p>
  <p>Pooll Interno de Liquidez: ${poolLiquidez}</p>
  <p>Precio Inicial: ${precioInicial} BTCB</p>
  <p>Período de Pre-venta: ${fechaInicioPreVenta} - ${fechaFinPreVenta}</p>
  <p>Precio de Pre-venta: ${precioPreVenta} BTCB</p>
  <p>Tokens en Pre-venta:
