CREATE_USERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS users (
        id INT GENERATED ALWAYS AS IDENTITY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        token TEXT,
        PRIMARY KEY(id)
    );"""
)

CREATE_HAPPINESS_RECORDINGS_TABLE = (
    """CREATE TABLE IF NOT EXISTS happiness_recordings (
        id INT GENERATED ALWAYS AS IDENTITY,
        user_id INT NOT NULL,
        record_date DATE NOT NULL,
        happiness_level REAL DEFAULT 0 NOT NULL,
        PRIMARY KEY(id),
        CONSTRAINT fk_user
            FOREIGN KEY(user_id)
                REFERENCES users(id)
    );"""
)



def runMigrations(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_HAPPINESS_RECORDINGS_TABLE)