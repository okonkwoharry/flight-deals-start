class DataManager:
    def __init__(self):

        self.SHEETY_URL = "https://api.sheety.co/a3ed72cedc6fb9ebaee3730775d892fe/copyOfFlightDeals/prices"

    def getting_price_row(self, number):
        import requests
        response = requests.get(url=f"{self.SHEETY_URL}/{number}")
        value = response.json()
        price = value['price']['lowestPrice']
        return price

    def name_city_sheet(self, number):
        import requests
        response = requests.get(url=f"{self.SHEETY_URL}/{number}")
        value = response.json()
        city = value['price']['city']
        return city

    def iata_code_sheet(self, number):
        import requests
        response = requests.get(url=f"{self.SHEETY_URL}/{number}")
        value = response.json()
        iata_code = value['price']['iataCode']
        return iata_code




