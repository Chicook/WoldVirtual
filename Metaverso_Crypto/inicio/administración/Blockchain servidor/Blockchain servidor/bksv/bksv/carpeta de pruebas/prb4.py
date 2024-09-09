css_content = """
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}
h1, h2 {
    color: #333;
}
#content {
    max-width: 600px;
    margin: auto;
}
input {
    display: block;
    margin-bottom: 10px;
    padding: 8px;
    width: 100%;
    box-sizing: border-box;
}
button {
    padding: 10px 15px;
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}
button:hover {
    background-color: #0056b3;
}
"""

blockchain = []

def get_blockchain():
    """
    Devuelve la blockchain completa.
    
    Returns:
        list: Lista de bloques en la blockchain.
    """
    return blockchain

def add_block():
    """
    Añade un nuevo bloque a la blockchain.
    
    Returns:
        dict: Diccionario con el mensaje y el nuevo bloque.
    """
    data = request.get_json()
    if 'data' in data:
        new_block = {'index': len(blockchain) + 1, 'data': data['data'], 'hash': hashlib.sha256(data['data'].encode()).hexdigest()}
        blockchain.append(new_block)
        registrar_actividad_css(f"Bloque agregado: {new_block}")
        return jsonify({'message': 'Bloque agregado correctamente', 'block': new_block})
    else:
        return jsonify({'error': 'Datos no proporcionados'})

def get_block(block_index):
    """
    Devuelve un bloque específico de la blockchain.
    
    Args:
        block_index (int): Índice del bloque a obtener.
    
    Returns:
        dict: Diccionario con el bloque solicitado o un mensaje de error.
    """
    if 0 < block_index <= len(blockchain):
        return jsonify({'block': blockchain[block_index - 1]})
    else:
        return jsonify({'error': 'Índice de bloque inválido'})
        
