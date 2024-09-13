if __name__ == '__main__':
        from BK_bkP1.main import app, blockchain, db

            # Añadir el bloque génesis a la base de datos interna
                db.add_block(blockchain.chain[0])

                    # Ejecutar la API
                        app.run(debug=True)
        