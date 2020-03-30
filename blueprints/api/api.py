import os
import json
from flask import request, Blueprint, jsonify, current_app
from git import Repo

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/full_data', methods=['GET'])
def full_data():
    parent_path = current_app.config.get('DATAPIPELINE_PATH')
    file_path = os.path.join(parent_path, 'json/full_data.json')
    with open(file_path, 'r') as file_data:
        json_data = json.load(file_data)
    return jsonify(json_data)