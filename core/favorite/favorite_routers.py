from flask import request,jsonify
from .favorite_service import FavoriteService
from core import app
from core.models import favorite_dict

@app.route('/favorite',methods=['GET'])
def get_favorite():
    service = FavoriteService()
    favorite =service.get_all_favorite()
    return favorite

@app.route('/favorite/<string:id>',methods=['GET'])
def get_by_id_favorite(id):
    service = FavoriteService()
    favorite=service.get_favorite_id(id)
    return jsonify(favorite_dict(favorite))

@app.route('/favorite',methods=['POST'])
def create_favorite():
    data=request.get_json()
    service=FavoriteService()
    favorite=service.add_favorite(data)
    return jsonify(favorite_dict(favorite))

@app.route('/favorite/<string:id>', methods=['DELETE'])
def delete_favorite(id):
    service = FavoriteService()
    deleted = service.remove_favorite(id)

    if deleted:
        return jsonify({'msg': 'Favorite deleted successfully'}), 200
    else:
        return jsonify({'msg': 'Favorite not found'}), 404