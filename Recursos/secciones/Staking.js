const addLpButtons = document.querySelectorAll('.add-lp-button');

addLpButtons.forEach(button => {
  button.addEventListener('click', e => {
    e.preventDefault();
    // Aquí iría la lógica para añadir LP tokens a la dirección del usuario
    console.log('LP tokens añadidos');
  });
});
