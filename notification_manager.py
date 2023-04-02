class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.account_sid = "AC9e7fc9299902cc5811e4aab121e49daf"
        self.auth_token = "23f0de75c7f22d0b9e695de9ffacf6e0"

    def send_message(self, search_price, city_from, code_from, city_to, code_to, from_date, to_date):
        from twilio.rest import Client
        client = Client(self.account_sid, self.auth_token)
        message = client.messages\
            .create(
            body=f"Low price alert! Only €{search_price} to fly from {city_from}-{code_from} to {city_to}-{code_to}, from {from_date} to {to_date}",
            from_='+13465122591',
            to='+237653919277'
        )
        print(message.status)