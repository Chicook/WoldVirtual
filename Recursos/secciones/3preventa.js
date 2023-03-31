const connectMetamaskButton = document.querySelector('#connect-metamask');

// Función que se ejecuta al hacer clic en el botón de Metamask
function connectMetamask() {
  // Verificamos si Metamask está instalado en el navegador
  if (typeof window.ethereum !== 'undefined') {
    console.log('Metamask está instalado');

    // Conectamos Metamask
    window.ethereum.request({ method: 'eth_requestAccounts' })
      .then(() => {
        console.log('Metamask conectado');
        // Aquí puedes agregar más código para realizar operaciones con Metamask
      })
      .catch((error) => {
        console.error('Error al conectar Metamask', error);
      });
  } else {
    console.error('Metamask no está instalado');
  }
}

// Agregamos un evento de clic al botón de Metamask
connectMetamaskButton.addEventListener('click', connectMetamask);



// Crea un array con los precios de cada fase

const precios = [0.0005, 0.00051, 0.00052, 0.00053, 0.00054, 0.00055, 0.00056, 0.00057, 0.00058, 0.0006];

// Obtiene todos los botones de compra

const botonesCompra = document.querySelectorAll('.comprar-btn');

// Itera sobre cada botón de compra y agrega un event listener

botonesCompra.forEach((boton, indice) => {

  boton.addEventListener('click', () => {

    // Obtiene el precio del botón actual utilizando el índice del botón en el array de precios

    const precio = precios[indice];

    // Aquí va el código para procesar la compra

    alert("Se ha comprado WLCV por " + precio + " BTCB");

  });

});
