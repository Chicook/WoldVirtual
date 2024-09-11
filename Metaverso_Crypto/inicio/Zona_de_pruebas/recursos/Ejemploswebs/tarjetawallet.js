// seleccionamos los elementos del DOM necesarios
const amountEl = document.querySelector(".amount");
const depositBtn = document.querySelector(".deposit-btn");
const withdrawBtn = document.querySelector(".withdraw-btn");
const inputEl = document.querySelector(".input");
const balanceEl = document.querySelector(".balance");

let balance = 0; // inicializamos el balance en 0

// función para actualizar el balance en el DOM
function updateBalance() {
  balanceEl.textContent = balance.toFixed(3); // limitamos el balance a 3 decimales
  }

  // función para manejar el evento de hacer un depósito
  function handleDeposit() {
    const amount = parseFloat(inputEl.value); // convertimos el valor del input a un número de punto flotante
      if (!isNaN(amount) && amount > 0) { // si el input es un número válido y es mayor a 0
          balance += amount; // sumamos el depósito al balance
              updateBalance(); // actualizamos el balance en el DOM
                  inputEl.value = ""; // vaciamos el input
                    }
                    }

                    // función para manejar el evento de hacer un retiro
                    function handleWithdraw() {
                      const amount = parseFloat(inputEl.value); // convertimos el valor del input a un número de punto flotante
                        if (!isNaN(amount) && amount > 0 && amount <= balance) { // si el input es un número válido, es mayor a 0 y es menor o igual al balance
                            balance -= amount; // restamos el retiro al balance
                                updateBalance(); // actualizamos el balance en el DOM
                                    inputEl.value = ""; // vaciamos el input
                                      }
                                      }

                                      // agregamos los event listeners a los botones
                                      depositBtn.addEventListener("click", handleDeposit);
                                      withdrawBtn.addEventListener("click", handleWithdraw);
                                      