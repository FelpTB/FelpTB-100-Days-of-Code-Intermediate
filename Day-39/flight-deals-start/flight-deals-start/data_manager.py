import requests
from pprint import pprint
class DataManager:

    def __init__(self):
        self.getUrl = "https://api.sheety.co/2d12ff83c151f901aafd8be7f981be40/flightDealsProject/prices"
        self.postUrl = "https://api.sheety.co/2d12ff83c151f901aafd8be7f981be40/flightDealsProject/prices"
        self.putUrl = "https://api.sheety.co/2d12ff83c151f901aafd8be7f981be40/flightDealsProject/prices/"

    def getData(self):
        response = requests.get(self.getUrl)
        data = response.json()
        return data

    def updateData(self, data):
        for i in data:
            body = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            requests.put(self.putUrl + str(i["id"]), json=body)
        return 0





