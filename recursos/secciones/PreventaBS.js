// Definimos el precio inicial de la pre-venta
let precioInicial = 0.0005;

// Definimos el precio final de la pre-venta
let precioFinal = 0.0006;

// Definimos la cantidad total de WLCV a vender
let cantidadTotal = 10000000;

// Definimos la cantidad de fases de venta
let numFases = 10;

// Calculamos la cantidad de tokens a vender en cada fase
let cantidadPorFase = cantidadTotal / numFases;

// Creamos un array para almacenar los precios de cada fase
let preciosFases = [];

// Calculamos el precio de cada fase y lo almacenamos en el array
for (let i = 0; i < numFases; i++) {
  let precioFase = precioInicial + (i * (precioFinal - precioInicial) / (numFases - 1));
  preciosFases.push(precioFase);
}

// Mostramos los precios de cada fase en la consola
console.log("Precios por fase:");
for (let i = 0; i < numFases; i++) {
  console.log("Fase " + (i + 1) + ": " + preciosFases[i] + " BTCB");
}
