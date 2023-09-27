from flask import Flask
from import_data import DataImporter
from routes import restaurant_routes, statistics_routes
from config import Config
from models import db
from routes.restaurant_routes import RestaurantRoutes
from routes.statistics_routes import StatisticsRoutes


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CSV_FILE_PATH = Config.CSV_FILE_PATH

def import_data_on_startup():
    print("Importing data from CSV...")
    importer = DataImporter()
    success, message = importer.import_data()
    if success:
        print(message)
    else:
        print(f'Error: {message}')

with app.app_context():
    db.create_all()
    import_data_on_startup()

restaurant_routes = RestaurantRoutes()
restaurant_routes.register_routes()
app.register_blueprint(restaurant_routes.blueprint)

statistics_routes = StatisticsRoutes()
statistics_routes.register_routes()
app.register_blueprint(statistics_routes.blueprint)


if __name__ == '__main__':
    app.run(debug=True)
