// Esperamos a que la página esté cargada
window.addEventListener('load', async () => {
	// Comprobamos si MetaMask está instalado
	if (typeof window.ethereum !== 'undefined') {
		// Obtenemos la dirección del usuario
		const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
		const address = accounts[0];
		
		// Mostramos la dirección del usuario
		alert(`Bienvenido a mi plataforma web!\n\nTu dirección de Ethereum es: ${address}`);
	}
