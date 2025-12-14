from core.models import Favorite,favorite_dict
from core import db


class FavoriteService:
    @staticmethod
    def get_all_favorite():
        favoriteies= Favorite.query.order_by(Favorite.id.asc()).all()
        favorite_list=[favorite_dict(favorite) for favorite in favoriteies]
        return favorite_list
    
    @staticmethod
    def get_favorite_id(id):
        favorite= Favorite.query.filter_by(id=id).first()
        return favorite
    
    @staticmethod
    def add_favorite(data):
        user_id=data['user_id']
        people_id=data['people_id']
        vehicle_id=data['vehicle_id']
        planet_id=data['planet_id']
        new_favorite=Favorite(
            user_id=user_id,people_id=people_id,
            vehicle_id=vehicle_id,planet_id=planet_id)
        db.session.add(new_favorite)
        db.session.commit()
        return new_favorite
    @staticmethod
    def remove_favorite(id):
        favorite = Favorite.query.filter_by(id=id).first()

        if favorite is None:
            return False   # ✅ nothing to delete

        db.session.delete(favorite)
        db.session.commit()
        return True


