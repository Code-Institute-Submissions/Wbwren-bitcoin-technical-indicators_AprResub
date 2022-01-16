

# Loading Bitcoin Price Data
- download bitcoin historical data csv from predered source (e.g. investing.com)
- edit csv to include the following cols: id, date, price, open, high, low
- delete header row (just include the data rows)
- set the date col to the format Y-m-d
- set all other cols to a type of number (otherwise prices may have ',' symbol which can cause errors)
- install sqlite extension for visual studio code
- load the csv to the project root directory
- use the following commands to load the data into the Django database:
    .\sqlite3.exe metrics_bitcoin_price_data
    .mode csv
    .import btc_price_data.csv metrics_bitcoin_price_data

# Loading metic data




Super user can edit bitcoin price data undert the account section in nav



# Testing
- test super user can crud price data

- test non super user cannot crud data

