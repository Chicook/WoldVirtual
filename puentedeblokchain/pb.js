const form = document.querySelector('form');
const error = document.querySelector('.error');

form.addEventListener('submit', (event) => {
	event.preventDefault();
    	error.textContent = '';

        	const token = document.querySelector('#token').value.trim();
            	const amount = document.querySelector('#amount').value.trim();
                	const recipient = document.querySelector('#recipient').value.trim();
                    	const network = document.querySelector('#network').value;

                        	if (!token || !amount || !recipient || !network) {
                            		error.textContent = 'Todos los campos son obligatorios.';
                                    		return;
                                            	}

                                                	// Lógica para transferir tokens a la red de destino

                                                    	alert(`Se ha transferido ${amount} ${token} a ${recipient} en la red de ${network}.`);
                                                        });
                                                        