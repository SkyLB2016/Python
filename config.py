_config = {
    'db': {
        'host': '192.168.12.203',
        'port': 3306,
        'user': 'coach',
        'password': 'vLSkL6SMmCsrGuGQ',
        'database': 'coach',
        'chart_set': 'utf8mb4'
    },

    'redis': {
        'host': '10.0.30.202',
        'port': 6379,
        'password': 'HRWuu996',
        'db': 4
    },
}


def get_config(name):
    return _config.get(name)
