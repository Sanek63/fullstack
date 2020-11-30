from flask import request, Flask, Response
from flask_cors import CORS
from database import database_actions, config
from actions import get_last_id, dict_from_tuple
import json

app = Flask(__name__)
cors = CORS(app, resources={"/*": {"origins": "*"}})


@app.route('/add', methods=['POST'])
def append_hero():
    try:
        args = request.get_json(force=True)

        hero_id = get_last_id() + 1
        hero_name = args['name']
        hero_health = args['health']
        hero_damage = args['damage']
        hero_mana = args['mana']
        hero_attribute = args['attribute']

        query = f"INSERT INTO {config.TABLE_NAME} VALUES("\
                f"{hero_id}, '{hero_name}', {hero_health},"\
                f"{hero_damage}, {hero_mana}, '{hero_attribute}')"

        database_actions.update_query(query)
        response = dict(id=hero_id)
        r = json.dumps(response)

        return Response(r, status=200, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response(status=500)


@app.route('/get_sorted', methods=['POST'])
def return_sorted_heroes():
    args = request.get_json(force=True)
    attribute = args['attribute']

    try:

        query = f"SELECT * FROM {config.TABLE_NAME} ORDER BY \"{attribute}\""

        result = database_actions.execute_query(query)
        heroes = dict_from_tuple(result)
        response = json.dumps(heroes, ensure_ascii=False)

        return Response(response=response, status=200)
    except Exception as e:
        print(e)
        return Response(status=500)


@app.route('/get', methods=['GET'])
def return_heroes():
    try:
        query = f"SELECT * FROM {config.TABLE_NAME}"

        result = database_actions.execute_query(query)
        heroes = dict_from_tuple(result)
        response = json.dumps(heroes, ensure_ascii=False)

        return Response(response=response, status=200)
    except Exception as e:
        print(e)
        return Response(status=500)


@app.route('/remove', methods=['POST'])
def remove_hero():
    try:
        data = request.get_json(force=True)

        query = f"DELETE FROM {config.TABLE_NAME} WHERE id = {int(data['id'][5:])}"
        database_actions.update_query(query)

        return Response(status=200)
    except Exception as e:
        print(e)
        return Response(status=500)


if __name__ == '__main__':
    app.run()
