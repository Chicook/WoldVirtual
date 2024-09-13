# from database import get_db_connection

# def get_user_by_username(username):
    # conn = get_db_connection()
    # user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
   # conn.close()
   # return user

# def create_user(username, password):
   # conn = get_db_connection()
   # conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
   # conn.commit()
    # conn.close()
