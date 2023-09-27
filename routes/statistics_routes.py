from flask import Blueprint, request, jsonify
from models import Restaurant
import math

class StatisticsRoutes:
    def __init__(self):
        self.blueprint = Blueprint('statistics_routes', __name__)

    def register_routes(self):
        self.blueprint.add_url_rule('/restaurants/statistics', 'get', self.get_restaurant_statistics, methods=['GET'])

    def get_restaurant_statistics(self):
        try:
            # Parse request parameters
            latitude = float(request.args.get('latitude'))
            longitude = float(request.args.get('longitude'))
            radius = float(request.args.get('radius'))

            # Calculate the bounding box for the circle
            lat_range = (latitude - (radius / 111.32), latitude + (radius / 111.32))
            lng_range = (longitude - (radius / (111.32 * math.cos(math.radians(latitude)))), 
                        longitude + (radius / (111.32 * math.cos(math.radians(latitude)))))

            # Query restaurants within the bounding box
            restaurants_in_circle = Restaurant.query.filter(
                Restaurant.lat.between(lat_range[0], lat_range[1]),
                Restaurant.lng.between(lng_range[0], lng_range[1])
            ).all()

            # Calculate count, average rating, and standard deviation
            count = len(restaurants_in_circle)
            avg_rating = sum(restaurant.rating for restaurant in restaurants_in_circle) / count
            std_deviation = math.sqrt(sum((restaurant.rating - avg_rating) ** 2 for restaurant in restaurants_in_circle) / count)

            # Return the statistics as JSON
            return jsonify({
                'count': count,
                'avg': avg_rating,
                'std': std_deviation
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
