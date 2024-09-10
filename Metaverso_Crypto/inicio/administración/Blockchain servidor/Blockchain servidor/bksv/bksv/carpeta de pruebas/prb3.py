from vpython import vec, cylinder, pi, cos, sin

def create_structure():
    radius = 10
    num_spaces = 6
    space_width = 2

    structure = []
    for i in range(num_spaces):
        theta = i * 2 * pi / num_spaces
        x = radius * cos(theta)
        y = radius * sin(theta)
        space = cylinder(pos=vec(x, y, 0), axis=vec(0, 0, space_width), radius=space_width / 2)
        structure.append(space)
    
    return structure

def create_block(module_name, previous_hash):
    import hashlib
    block_data = f'{module_name}-{previous_hash}'
    block_hash = hashlib.sha256(block_data.encode()).hexdigest()
    return {'module': module_name, 'hash': block_hash, 'previous_hash': previous_hash}

def validate_block(block):
    print(f"Validating block: {block['module']} with hash: {block['hash']}")
