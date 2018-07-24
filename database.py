from orator import DatabaseManager
from os import getenv

config = {
    'pgsql': {
        'driver': 'pgsql',
        'host': getenv('DB_HOST'),
        'database': getenv('DB_DATABASE'),
        'user': getenv('DB_USER'),
        'password': getenv('DB_PASSWORD')
    }
}

db = DatabaseManager(config)
