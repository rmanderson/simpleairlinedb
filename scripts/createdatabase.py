import csv
import sqlite3
import requests
from sqlite3 import Cursor

database_name = "../simpleairline.db"

airline_table_schema = ('CREATE TABLE IF NOT EXISTS "airlines" ('
	'"id" INTEGER,'
	'"airline" TEXT,'
	'"airline_name" TEXT,'
	'PRIMARY KEY("id"))')

airline_route_table_schema = ('CREATE TABLE IF NOT EXISTS "airline_routes" ('
    '"id" INTEGER PRIMARY key,'
	'"airline" TEXT,'
	'"origin_iata_code" TEXT,'
	'"destination_iata_code" TEXT,'
	'"direct" TEXT,'
	'"active" TEXT,'
	'"seasonal_route" TEXT,'
	'"start_date" TEXT)' )

airports_table_schema = ('CREATE TABLE IF NOT EXISTS "airports" ('
	'"id" INTEGER,'
	'"ident" TEXT,'
	'"type" TEXT,'
	'"name" TEXT,'
	'"latitude_deg" REAL,'
	'"longitude_deg" REAL,'
	'"elevation_ft" INTEGER,'
	'"continent" TEXT,'
	'"iso_country" TEXT,'
	'"iso_region" TEXT,'
	'"municipality" TEXT,'
	'"scheduled_service" TEXT,'
	'"gps_code" TEXT,'
	'"iata_code" TEXT,'
	'"local_code" TEXT,'
	'"home_link" TEXT,'
	'"wikipedia_link" TEXT,'
	'"keywords"	TEXT)')

files_to_import = ["../raw_data/as_routes.csv", 
                   "../raw_data/ha_routes.csv", 
                   "../raw_data/g4_routes.csv",
                   "../raw_data/mx_routes.csv",
                   "../raw_data/b6_routes.csv",
                   "../raw_data/sy_routes.csv"]

airport_data_download_location = "https://davidmegginson.github.io/ourairports-data/airports.csv"

def main():
    connection = sqlite3.connect(database_name)

    cursor = connection.cursor()

    cursor.execute(airline_route_table_schema)
    cursor.execute(airline_table_schema)
    cursor.execute(airports_table_schema)

    import_airlines("../raw_data/airlines.csv", cursor)
    
    for airline_file in files_to_import:
        import_airline_routes(airline_file, cursor)

    import_airports(airport_data_download_location, cursor)

    connection.commit()
    connection.close()

def import_airlines(filename: str, dbcursor: Cursor):
    airline_insert_sql = "INSERT INTO airlines (airline, airline_name) VALUES (?, ?)"
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)    
        for row in csv_reader:        
            db_parameters = (row['airline'], row['airline_name'])
            dbcursor.execute(airline_insert_sql, db_parameters)
    

def import_airline_routes(filename: str, dbcursor: Cursor):
    airline_route_insert_sql = "INSERT INTO airline_routes (airline, origin_iata_code, destination_iata_code, direct, active, seasonal_route, start_date) VALUES (?, ?, ?, ?, ?, ?, ?)"
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)    
        for row in csv_reader:        
            db_parameters = (row['airline'], row['origin_iata_code'], row['destination_iata_code'], 
                             row['direct'], row['active'],row['seasonal_route'],
                             row['start_date'])
            dbcursor.execute(airline_route_insert_sql, db_parameters)

def import_airports(airport_data_url: str, dbcursor: Cursor):
    airport_insert_sql ="INSERT INTO airports values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    r = requests.get(airport_data_url, allow_redirects=True)
    open("airports.csv", "wb").write(r.content)
    with open("airports.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:        
            db_parameters = (row['id'], row['ident'], row['type'], 
                            row['name'], row['latitude_deg'],row['longitude_deg'],
                            row['elevation_ft'], row['continent'],row['iso_country'],
                            row['iso_region'], row['municipality'],row['scheduled_service'],
                            row['gps_code'], row['iata_code'],row['local_code'],
                            row['home_link'], row['wikipedia_link'],row['keywords'])            
            dbcursor.execute(airport_insert_sql, db_parameters)

if __name__ == "__main__":
    main()
