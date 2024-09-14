const form = document.querySelector('#exchange-form');
const alert = document.querySelector('.alert');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const fromNetwork = form.elements['from-network'].value;
  const toNetwork = form.elements['to-network'].value;
  const fromToken = form.elements['from-token'].value;
  const toToken = form.elements['to-token'].value;
  const amount = form.elements['amount'].value;
  const wallet = form.elements['wallet'].value;

  alert.style.display = 'none';

  try {
    const txHash = await exchange(fromNetwork, toNetwork, fromToken, toToken, amount, wallet);

    alert.classList.add('alert-success');
    alert.textContent = `Exchange successful! Tx hash: ${txHash}`;
  } catch (error) {
    alert.classList.add('alert-danger');
    alert.textContent = error.message;
  }

  alert.style.display = 'block';
});

async function exchange(fromNetwork, toNetwork, fromToken, toToken, amount, wallet) {
  // Implementar lógica de intercambio de tokens
  // ...
}
