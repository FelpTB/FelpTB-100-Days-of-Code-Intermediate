import requests
class FlightSearch:
    def __init__(self):
        self.apiKey = "GrIbzAyYgx5121HRtvUxpDAKB1w9uHYP"
        self.url = "test.api.amadeus.com"
        self.apiSecret = "WLUCf1lKURc1K3kA"
        self.apiToken = self.get_new_token()

    def getCode(self, city):
        url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        headers = {"Authorization": f"Bearer {self.apiToken}"}
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=url,
            headers=headers,
            params=query
        )
        data = response.json()["data"][0]["iataCode"]
        return data

    def get_new_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.apiKey,
            'client_secret': self.apiSecret
        }
        response = requests.post(url=url, headers=header, data=body)
        data = response.json()
        print(f"Your token is {data["access_token"]}")
        return data["access_token"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):


        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self.apiToken}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers",
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()




