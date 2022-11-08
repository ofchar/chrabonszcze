SELECT_FROM_USERS_BY_ID = (
    """SELECT * FROM users WHERE id = (%s);"""
)

ADD_USER = (
    """INSERT INTO users (name, email, password, token) VALUES (%s, %s, %s, %s)"""
)