SELECT_FROM_USERS_BY_ID = (
    """SELECT * FROM users WHERE id = (%s);"""
)

SELECT_FROM_USERS_BY_EMAIL = (
    """SELECT * FROM users WHERE email = (%s);"""
)

ADD_USER = (
    """INSERT INTO users (name, email, password, token) VALUES (%s, %s, %s, %s);"""
)

LOGIN = (
    """SELECT * FROM users WHERE email = (%s);"""
)

LOGOUT = (
    """UPDATE users SET token = (%s) WHERE token = (%s)"""
)

GET_TODAYS_HAPPINESS_RECORD_FOR_USER = (
    """SELECT hr.* FROM happiness_recordings AS hr
        JOIN users ON users.id = hr.user_id
        WHERE users.token = (%s) AND hr.record_date = CURRENT_DATE"""
)

CREATE_TODAYS_HAPPINESS_RECORD_FOR_USER = (
    """INSERT INTO happiness_recordings (user_id, record_date, happiness_level)
        SELECT id, CURRENT_DATE, (%s)
        FROM users WHERE token = (%s);"""
)

UPDATE_TODAYS_HAPPINESS_RECORD_FOR_USER = (
    """UPDATE happiness_recordings
        SET happiness_level = happiness_level + (%s)
        WHERE user_id = (
            SELECT id
            FROM users
            WHERE token = (%s)
        ) AND record_date = CURRENT_DATE"""
)

GET_TWO_WEEK_HAPPINESS_RECORDS_FOR_USER = (
    """SELECT hr.* FROM happiness_recordings AS hr
        JOIN users ON users.id = hr.user_id
        WHERE users.token = (%s) AND hr.record_date > CURRENT_DATE - interval '14' day"""
)