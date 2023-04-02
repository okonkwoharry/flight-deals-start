#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

# TEQUILA_API_KEY = "ELgLEQktk8SdIsKZT43xPhIlWxG0JMgN"
# URL = "https://api.tequila.kiwi.com/locations/query"
#
# header = {
#     "apikey": TEQUILA_API_KEY
# }
#
# #PART TO FILL IN THE SHEET WITH LOCATION IATA CODE
#
# SHEETY_URL = "https://api.sheety.co/e0cb3cda6bca5e2401c00e967de687b5/copyOfFlightDeals/prices/"
#
# sheety_response = requests.get(url=SHEETY_URL)
# sheety_response_variable = sheety_response.json()
#
# for item in sheety_response_variable['prices']:
#     city = item['city']
#     id = item['id']
#     lowest_price = item['lowestPrice']
#     parameter = {
#         "term": city
#     }
#     response = requests.get(url=URL, headers=header, params=parameter)
#     response_variable = response.json()
#     code = response_variable['locations'][0]['code']
#     put_parameter = {
#         "price": {
#             "city": city,
#             "iataCode": code,
#             "lowestPrice": lowest_price
#         }
#     }
#     put_response = requests.put(url=f"{SHEETY_URL}/{id}", headers=header, json=put_parameter)
#     print(put_response.text)


from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

list_id = ['2', '3', '4', '5', '6', '7', '8', '9', '10']

for number in list_id:
    data = DataManager()
    flight_da = FlightSearch()
    city_name = data.name_city_sheet(number)
    row_price = int(data.getting_price_row(number))
    iata_code = data.iata_code_sheet(number)
    search_price = int(flight_da.get_cheapest_flight(iata_code))
    city_from = flight_da.city_from_name(iata_code)
    code_from = flight_da.city_from_code(iata_code)
    city_to = flight_da.city_to_name(iata_code)
    code_to = flight_da.city_to_code(iata_code)
    from_date = flight_da.from_date(iata_code)
    to_date = flight_da.to_date(iata_code)
    if search_price < row_price:
        sms = NotificationManager()
        sms.send_message(search_price, city_from, code_from, city_to, code_to, from_date, to_date)








