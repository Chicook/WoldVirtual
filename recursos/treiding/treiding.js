// Define trading pairs
const tradingPairs = [
  {id: 1, pair: 'ETH/BTC'},
    {id: 2, pair: 'LTC/BTC'},
      {id: 3, pair: 'XRP/BTC'}
      ];

      // Populate trading pairs select element
      const pairSelect = document.getElementById('pair-select');
      tradingPairs.forEach(pair => {
        const option = document.createElement('option');
          option.value = pair.id;
            option.textContent = pair.pair;
              pairSelect.appendChild(option);
              });

              // Place order
              const orderForm = document.getElementById
                  