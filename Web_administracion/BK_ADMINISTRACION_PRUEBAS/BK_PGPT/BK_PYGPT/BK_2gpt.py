import sqlite3

def execute_query(query, params=()):
    conn = sqlite3.connect('blockchain_app.db')
        cursor = conn.cursor()
            cursor.execute(query, params)
                conn.commit()
                    conn.close()

                    def fetch_query(query, params=()):
                        conn = sqlite3.connect('blockchain_app.db')
                            cursor = conn.cursor()
                                cursor.execute(query, params)
                                    result = cursor.fetchall()
                                        conn.close()
                                            return result
    