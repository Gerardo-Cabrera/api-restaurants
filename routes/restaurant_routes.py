from flask import Blueprint, request, jsonify
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from models import db, Restaurant


class RestaurantRoutes:
    def __init__(self):
        self.blueprint = Blueprint('restaurant_routes', __name__)

    def register_routes(self):
        self.blueprint.add_url_rule('/restaurants/', 'get_all', self.get_all_restaurants, methods=['GET'])
        self.blueprint.add_url_rule('/restaurants/<id>', 'get_by_id', self.get_restaurant_by_id, methods=['GET'])
        self.blueprint.add_url_rule('/restaurants', 'create', self.create_restaurant, methods=['POST'])
        self.blueprint.add_url_rule('/restaurants/<id>', 'update', self.update_restaurant, methods=['PUT'])
        self.blueprint.add_url_rule('/restaurants/<id>', 'delete', self.delete_restaurant, methods=['DELETE'])
        self.blueprint.add_url_rule('/restaurants/rating/<rating>', 'get_by_rating', self.get_restaurants_by_rating, methods=['GET'])
        self.blueprint.add_url_rule('/restaurants/state/<state>', 'get_by_state', self.get_restaurants_by_state, methods=['GET'])
        self.blueprint.add_url_rule('/restaurants/state/<state>/rating/<int:rating>', 'get_by_state_and_rating', self.get_restaurants_by_state_and_rating, methods=['GET'])

    def get_all_restaurants(self):
        try:
            # Query the database to get all restaurants
            restaurants = Restaurant.query.all()

            # Create a list to store restaurant data as dictionaries
            restaurant_list = []
            for restaurant in restaurants:
                restaurant_data = {
                    'id': restaurant.id,
                    'rating': restaurant.rating,
                    'name': restaurant.name,
                    'site': restaurant.site,
                    'email': restaurant.email,
                    'phone': restaurant.phone,
                    'street': restaurant.street,
                    'city': restaurant.city,
                    'state': restaurant.state,
                    'lat': restaurant.lat,
                    'lng': restaurant.lng
                }
                restaurant_list.append(restaurant_data)

            # Return the list of restaurants as JSON
            return jsonify(restaurant_list)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_restaurant_by_id(self, id):
        try:
            restaurant = Restaurant.query.get(id)
            if restaurant is not None:
                    return jsonify({
                        'rating': restaurant.rating,
                        'name': restaurant.name,
                        'site': restaurant.site,
                        'email': restaurant.email,
                        'phone': restaurant.phone,
                        'street': restaurant.street,
                        'city': restaurant.city,
                        'state': restaurant.state,
                        'lat': restaurant.lat,
                        'lng': restaurant.lng
                    }), 200
            else:
                return jsonify({'error': 'Restaurant not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    def get_restaurants_by_state(self, state):
        try:
            # Query the database to get all restaurants in the specified state
            restaurants = Restaurant.query.filter_by(state=state).all()

            # Create a list to store restaurant data as dictionaries
            restaurant_list = []
            for restaurant in restaurants:
                restaurant_data = {
                    'id': restaurant.id,
                    'rating': restaurant.rating,
                    'name': restaurant.name,
                    'site': restaurant.site,
                    'email': restaurant.email,
                    'phone': restaurant.phone,
                    'street': restaurant.street,
                    'city': restaurant.city,
                    'lat': restaurant.lat,
                    'lng': restaurant.lng
                }
                restaurant_list.append(restaurant_data)

            # Return the list of restaurants in the specified state as JSON
            return jsonify(restaurant_list)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    def get_restaurants_by_rating(self, rating):
        try:
            # Query the database to get all restaurants in the specified rating
            restaurants = Restaurant.query.filter_by(rating=rating).all()

            # Create a list to store restaurant data as dictionaries
            restaurant_list = []
            for restaurant in restaurants:
                restaurant_data = {
                    'id': restaurant.id,
                    'name': restaurant.name,
                    'site': restaurant.site,
                    'email': restaurant.email,
                    'phone': restaurant.phone,
                    'street': restaurant.street,
                    'city': restaurant.city,
                    'state': restaurant.state,
                    'lat': restaurant.lat,
                    'lng': restaurant.lng
                }
                restaurant_list.append(restaurant_data)

            # Return the list of restaurants in the specified state as JSON
            return jsonify(restaurant_list)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_restaurants_by_state_and_rating(self, state, rating):
        try:
            # Query the database to get all restaurants in the specified state and the specified rating
            restaurants = Restaurant.query.filter(and_(Restaurant.state == state, Restaurant.rating == rating)).all()

            # Create a list to store restaurant data as dictionaries
            restaurant_list = []
            for restaurant in restaurants:
                restaurant_data = {
                    'id': restaurant.id,
                    'name': restaurant.name,
                    'site': restaurant.site,
                    'email': restaurant.email,
                    'phone': restaurant.phone,
                    'street': restaurant.street,
                    'city': restaurant.city,
                    'lat': restaurant.lat,
                    'lng': restaurant.lng
                }
                restaurant_list.append(restaurant_data)

            # Return the list of restaurants in the specified state as JSON
            return jsonify(restaurant_list)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def create_restaurant(self):
        data = request.get_json()
        new_restaurant = Restaurant(**data)
        try:
            db.session.add(new_restaurant)
            db.session.commit()
            return jsonify({'message': 'Restaurant created successfully'}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Duplicate restaurant ID'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    def update_restaurant(self, id):
        try:
            restaurant = Restaurant.query.get(id)
            if restaurant is not None:
                data = request.get_json()
                for key, value in data.items():
                    setattr(restaurant, key, value)
                db.session.commit()
                return jsonify({'message': 'Restaurant updated successfully'}), 200
            else:
                return jsonify({'error': 'Restaurant not found'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    def delete_restaurant(self, id):
        try:
            restaurant = Restaurant.query.get(id)
            if restaurant is not None:
                    db.session.delete(restaurant)
                    db.session.commit()
                    return jsonify({'message': 'Restaurant deleted successfully'}), 200
            else:
                return jsonify({'error': 'Restaurant not found'}), 404
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
