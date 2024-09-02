# Simple Airline Database
Just a simple SQLite Database with airline informaion. This information was aggregated from several public sources. Sources for all data has been listed and credited.

## Current Data
General Airport information
Airline names and BTS codes
Alaska Airlines routes (2024-09-02)

## Future Updates
Delta Airlines routes
American Airlines routes
United Airlines routes
Southwest Airlines routes
Jetblue Airlines routes
Hawaiian Airlines routes
Breeze Airways routes
Sun Country Airlines routes

For additional airline route requests please create an issue

## How often will the data be updated? What if some data is incorrect or out of date?
I plan to update the data around once a month. Because of the changing nature of the airline industry data is prone to be out of date. If you find data thats out of date please feel free to create an issue. Please do not create a pull request due to how the data is aggregated.

## Database Schema

### airline_routes
| Column | Definition |
|---|---| 
|id|Internal identifer. This identifer may change from version to version depending on the data import|
| airline | Bureau of Transportation Statistics airline code | 
| origin_iata_code | The three-letter IATA code for the origin airport | 
| destination_iata_code	| The three-letter IATA code for the destination airport | 
| direct | Indicate whether the route is direct | 
| active | Indicates whether the route is currently active | 
| seasonal_route | Indicates whether the route is seasonal | 
| start_date | Indicates the start date for the route | 

### airlines
| Column | Definition |
|---|---| 
| id| Internal identifer. This identifer may change from version to version depending on the data import| 
| airline| Bureau of Transportation Statistics airline code| 
| airline_name| Airline name via the Bureau of Transportation Statistics| 

### airports 
(Definitions taken from https://ourairports.com/help/data-dictionary.html)
| Column | Definition |
|---|---| 
| id| Internal OurAirports integer identifier for the airport. This will stay persistent, even if the airport code changes.| 
| ident| The text identifier used in the OurAirports URL. This will be the ICAO code if available. Otherwise, it will be a local airport code (if no conflict), or if nothing else is available, an internally-generated code starting with the ISO2 country code, followed by a dash and a four-digit number.| 
| type| The type of the airport. Allowed values are "closed_airport", "heliport", "large_airport", "medium_airport", "seaplane_base", and "small_airport". See the map legend for a definition of each type.| 
| name| 	The official airport name, including "Airport", "Airstrip", etc.| 
| latitude_deg	| 	The airport latitude in decimal degrees (positive for north).| 
| longitude_deg	| 	The airport longitude in decimal degrees (positive for east).| 
| elevation_ft	| 	The airport elevation MSL in feet (not metres).| 
| continent	| 	The code for the continent where the airport is (primarily) located. Allowed values are "AF" (Africa), "AN" (Antarctica), "AS" (Asia), "EU" (Europe), "NA" (North America), "OC" (Oceania), or "SA" (South America).| 
| iso_country	| 	The two-character ISO 3166:1-alpha2 code for the country where the airport is (primarily) located. A handful of unofficial, non-ISO codes are also in use, such as "XK" for Kosovo. Points to the code column in countries.csv.| 
| iso_region	| 	An alphanumeric code for the high-level administrative subdivision of a country where the airport is primarily located (e.g. province, governorate), prefixed by the ISO2 country code and a hyphen. OurAirports uses ISO 3166:2 codes whenever possible, preferring higher administrative levels, but also includes some custom codes. See the documentation for regions.csv.| 
| municipality	| 	The primary municipality that the airport serves (when available). Note that this is not necessarily the municipality where the airport is physically located.| 
| scheduled_service	| 	"yes" if the airport currently has scheduled airline service; "no" otherwise.| 
| gps_code	| 	The code that an aviation GPS database (such as Jeppesen's or Garmin's) would normally use for the airport. This will always be the ICAO code if one exists. Note that, unlike the ident column, this is not guaranteed to be globally unique.| 
| iata_code	| 	The three-letter IATA code for the airport (if it has one).| 
| local_code	| 	The local country code for the airport, if different from the gps_code and iata_code fields (used mainly for US airports).| 
| home_link	| 	URL of the airport's official home page on the web, if one exists.| 
| wikipedia_link	| 	URL of the airport's page on Wikipedia, if one exists.| 
| keywords	| 	Extra keywords/phrases to assist with search, comma-separated. May include former names for the airport, alternate codes, names in other languages, nearby tourist destinations, etc.| 

## Data Sources

Airport data
  https://ourairports.com/data/
  https://github.com/davidmegginson/ourairports-data

Airline data
  https://www.bts.gov/topics/airlines-and-airports/airline-codes

Airline Route Data
  https://www.alaskaair.com/en/sitemap/flights-from-city-to-city/page-1
  Various press releases and news articles

### If you find this project useful feel free to buy me a coffee

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/travelblerd)
