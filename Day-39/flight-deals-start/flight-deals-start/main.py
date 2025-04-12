#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime, timedelta
import data_manager
import flight_search
from flight_data import find_cheapest_flight
import notification_manager

GET_URL = "https://api.sheety.co/2d12ff83c151f901aafd8be7f981be40/flightDealsProject/prices"
POST_URL = "https://api.sheety.co/2d12ff83c151f901aafd8be7f981be40/flightDealsProject/prices"
IATA_CODE = "GRU"

# ==================== Update the Airport Codes in Google Sheet ====================
dataManager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
notification_manager = notification_manager.NotificationManager()

sheetData = dataManager.getData()
sheetData = sheetData['prices']
for i in sheetData:
    i['iataCode'] = flight_search.getCode(i['city'])

dataManager.updateData(sheetData)

# ==================== Search for Flights ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in sheetData:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        IATA_CODE,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )

