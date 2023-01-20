class Offer():
    def __init__(self, offer_id, user_id, destination, departure, date_time):
        self.offer_id = offer_id
        self.user_id = user_id
        self.destination = destination
        self.departure = departure
        self.date_time = date_time

class Request():
    def __init__(self, request_id, user_id, destination, departure, date_time):
        self.request_id = request_id
        self.user_id = user_id
        self.destination = destination
        self.departure = departure
        self.date_time = date_time