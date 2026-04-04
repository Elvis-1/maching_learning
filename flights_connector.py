from typing import List

"""
An airline needs to find connecting flights between cities. Write a function that:
s
Input:
- flights: list of (flight_id, origin, destination, departure_time, arrival_time, price)
  Example: [
    ("F1", "NYC", "CHI", "08:00", "10:00", 300),
    ("F2", "CHI", "LAX", "11:00", "13:30", 400),
    ("F3", "NYC", "DFW", "09:00", "12:00", 350),
    ("F4", "DFW", "LAX", "13:00", "15:00", 250),
    ("F5", "NYC", "LAX", "14:00", "17:00", 600),  # Direct flight
    ("F6", "LAX", "SFO", "16:00", "17:30", 150),
  ]

- origin: str (e.g., "NYC")
- destination: str (e.g., "LAX")

Return:
- List of possible routes from origin to destination, sorted by total price (cheapest first)
- Each route should be a dictionary:
  {
    "flights": ["F1", "F2"],  # List of flight IDs in order
    "total_price": 700,
    "total_duration": 330,  # Total journey time in minutes (including layovers)
    "layovers": [60]  # Layover times in minutes between flights
  }

Rules:
1. Connections must have at least 30 minutes layover time
2. Flights cannot go backwards in time (arrival < departure for same day)
3. Maximum 2 connections (3 flights total)
4. If multiple routes have same price, sort by shorter total duration
5. Return empty list if no routes found
6. Handle invalid input by returning empty list
"""

class Flights:
 #  list of (flight_id, origin, destination, departure_time, arrival_time, price)
   def __init__(self,flight_id,origin,destination,departure_time,arrival_time,price):
      self.flight_id = flight_id
      self.origin = origin
      self.destination = destination
      self.departure_time = departure_time
      self.arrival_time = arrival_time
      self.price = price
   

def convert_time_string_to_minutes(time:str) -> int:
      t:str= "10:30"
      sp = t.split(':')
      minutes = (int(sp[0]) * 60) + int(sp[1])
      print(minutes)
      
      return time

def conv_minutes_to_str(minutes:int) -> str:

    h = minutes//60
    s = minutes%60
    print(h,' hours ', s,' seconds')
    return f'{h:1d}:{s:1d}'
      


      
      

def flight_connector(flights:List[str]) -> List:
  flight =   [
    ("F1", "NYC", "CHI", "08:00", "10:00", 300),
    ("F2", "CHI", "LAX", "11:00", "13:30", 400),
    ("F3", "NYC", "DFW", "09:00", "12:00", 350),
    ("F4", "DFW", "LAX", "13:00", "15:00", 250),
    ("F5", "NYC", "LAX", "14:00", "17:00", 600),  # Direct flight
    ("F6", "LAX", "SFO", "16:00", "17:30", 150),
  ]

def main():
    print(convert_time_string_to_minutes('5'))
    print(conv_minutes_to_str(60))

if __name__ == '__main__':
    main()