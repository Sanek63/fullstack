from database.database_actions import get_connection
from database import config


def get_last_id():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT max(id) from {config.TABLE_NAME}")

    result = cursor.fetchall()[0][0]

    return result


def dict_from_tuple(tuple):
    heroes = {
        'items': [

        ],
        'count': 0
    }

    for hero in tuple:
        heroes['items'].append({
            'id': hero[0],
            'name': hero[1],
            'health': hero[2],
            'damage': hero[3],
            'mana': hero[4],
            'attribute': hero[5]
        })
        heroes['count'] = heroes.get('count', 0) + 1

    return heroes