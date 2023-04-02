class FlightSearch:
    def __init__(self):
        self.SEARCH_URL = "https://api.tequila.kiwi.com/v2/search"
        self.SEARCH_API_KEY = "ELgLEQktk8SdIsKZT43xPhIlWxG0JMgN"
        self.fly_from_code = "DUB"
        # self.fly_to_code = ""
        from datetime import datetime, timedelta
        self.present_day = datetime.now()
        self.t = self.present_day + timedelta(1)
        self.tomorrow = self.t.strftime('%d/%m/%Y')
        self.c = self.t + timedelta(183)
        self.six_month = self.c.strftime('%d/%m/%Y')
        self.min_length_stay = "3"
        self.max_length_stay = "10"

    def get_cheapest_flight(self, iata_code):
        import requests
        fly_to_code = iata_code
        header = {
            "apikey": self.SEARCH_API_KEY
        }
        parameters = {
            "fly_from": self.fly_from_code,
            "fly_to": fly_to_code,
            "date_from": self.tomorrow,
            "date_to": self.six_month,
            "nights_in_dst_from": self.min_length_stay,
            "nights_in_dst_to": self.max_length_stay,
            "flight_type": "round",
            "sort": "price",
            "asc": 1,
            "limit": 1,
        }
        response = requests.get(url=self.SEARCH_URL, headers=header, params=parameters)
        deee = response.json()
        return deee['data'][0]['price']

    def city_from_name(self, iata_code):
        import requests
        fly_to_code = iata_code
        header = {
            "apikey": self.SEARCH_API_KEY
        }
        parameters = {
            "fly_from": self.fly_from_code,
            "fly_to": fly_to_code,
            "date_from": self.tomorrow,
            "date_to": self.six_month,
            "nights_in_dst_from": self.min_length_stay,
            "nights_in_dst_to": self.max_length_stay,
            "flight_type": "round",
            "sort": "price",
            "asc": 1,
            "limit": 1
        }
        response = requests.get(url=self.SEARCH_URL, headers=header, params=parameters)
        deee = response.json()
        return deee['data'][0]['cityFrom']

    def city_from_code(self, iata_code):
        import requests
        fly_to_code = iata_code
        header = {
            "apikey": self.SEARCH_API_KEY
        }
        parameters = {
            "fly_from": self.fly_from_code,
            "fly_to": fly_to_code,
            "date_from": self.tomorrow,
            "date_to": self.six_month,
            "nights_in_dst_from": self.min_length_stay,
            "nights_in_dst_to": self.max_length_stay,
            "flight_type": "round",
            "sort": "price",
            "asc": 1,
            "limit": 1
        }
        response = requests.get(url=self.SEARCH_URL, headers=header, params=parameters)
        deee = response.json()
        return deee['data'][0]['cityCodeFrom']

    def city_to_name(self, iata_code):
        import requests
        fly_to_code = iata_code
        header = {
            "apikey": self.SEARCH_API_KEY
        }
        parameters = {
            "fly_from": self.fly_from_code,
            "fly_to": fly_to_code,
            "date_from": self.tomorrow,
            "date_to": self.six_month,
            "nights_in_dst_from": self.min_length_stay,
            "nights_in_dst_to": self.max_length_stay,
            "flight_type": "round",
            "sort": "price",
            "asc": 1,
            "limit": 1
        }
        response = requests.get(url=self.SEARCH_URL, headers=header, params=parameters)
        deee = response.json()
        return deee['data'][0]['cityTo']

    def city_to_code(self, iata_code):
        import requests
        fly_to_code = iata_code
        header = {
            "apikey": self.SEARCH_API_KEY
        }
        parameters = {
            "fly_from": self.fly_from_code,
            "fly_to": fly_to_code,
            "date_from": self.tomorrow,
            "date_to": self.six_month,
            "nights_in_dst_from": self.min_length_stay,
            "nights_in_dst_to": self.max_length_stay,
            "flight_type": "round",
            "sort": "price",
            "asc": 1,
            "limit": 1
        }
        response = requests.get(url=self.SEARCH_URL, headers=header, params=parameters)
        deee = response.json()
        return deee['data'][0]['cityCodeTo']

    def from_date(self, iata_code):
        import requests
        fly_to_code = iata_code
        header = {
            "apikey": self.SEARCH_API_KEY
        }
        parameters = {
            "fly_from": self.fly_from_code,
            "fly_to": fly_to_code,
            "date_from": self.tomorrow,
            "date_to": self.six_month,
            "nights_in_dst_from": self.min_length_stay,
            "nights_in_dst_to": self.max_length_stay,
            "flight_type": "round",
            "sort": "price",
            "asc": 1,
            "limit": 1
        }
        response = requests.get(url=self.SEARCH_URL, headers=header, params=parameters)
        deee = response.json()
        leee = deee['data'][0]['route'][0]['local_departure']
        seee = leee.split("T", 1)[0]
        return seee

    def to_date(self, iata_code):
        import requests
        fly_to_code = iata_code
        header = {
            "apikey": self.SEARCH_API_KEY
        }
        parameters = {
            "fly_from": self.fly_from_code,
            "fly_to": fly_to_code,
            "date_from": self.tomorrow,
            "date_to": self.six_month,
            "nights_in_dst_from": self.min_length_stay,
            "nights_in_dst_to": self.max_length_stay,
            "flight_type": "round",
            "sort": "price",
            "asc": 1,
            "limit": 1
        }
        response = requests.get(url=self.SEARCH_URL, headers=header, params=parameters)
        deee = response.json()
        leee = deee['data'][0]['route'][1]['local_departure']
        seee = leee.split("T", 1)[0]
        return seee







