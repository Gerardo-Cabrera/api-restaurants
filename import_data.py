import pandas as pd
from models import Restaurant
from config import Config 
from models import db


class DataImporter:
    def __init__(self):
        self.csv_file_path = Config.CSV_FILE_PATH

    def import_data(self):
        try:
            # Read the CSV file
            df = pd.read_csv(self.csv_file_path)

            # Loop through each row in the CSV and insert it into the database
            for index, row in df.iterrows():
                existing_record = Restaurant.query.filter_by(id=row['id']).first()

                if existing_record is None:
                    restaurant = Restaurant(
                        id=row['id'],
                        rating=row['rating'],
                        name=row['name'],
                        site=row['site'],
                        email=row['email'],
                        phone=row['phone'],
                        street=row['street'],
                        city=row['city'],
                        state=row['state'],
                        lat=row['lat'],
                        lng=row['lng']
                    )
                    db.session.add(restaurant)
                else:
                    return True, 'The data has already been inserted into the database.'

            # Commit the changes to the database
            db.session.commit()
            return True, 'Data imported successfully'
        except Exception as e:
            db.session.rollback()
            return False, str(e)
