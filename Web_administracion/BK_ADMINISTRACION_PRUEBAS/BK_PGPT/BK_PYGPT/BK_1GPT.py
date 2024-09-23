import sqlite3

def init_db():
    conn = sqlite3.connect('blockchain_app.db')
        c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                    nombre TEXT NOT NULL, 
                                                                        contraseña TEXT NOT NULL, 
                                                                                            wallet TEXT)''')
                                                                                                c.execute('''CREATE TABLE IF NOT EXISTS wallets (
                                                                                                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                                                                                                        usuario_id INTEGER, 
                                                                                                                                                            wallet_id TEXT, 
                                                                                                                                                                                FOREIGN KEY(usuario_id) REFERENCES usuarios(id))''')
                                                                                                                                                                                    conn.commit()
                                                                                                                                                                                        conn.close()
    