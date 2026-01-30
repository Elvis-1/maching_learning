"""
Docstring for table_reservations
A restaurant needs to manage table reservations. Write a function that:

Input:
- tables: list of (table_id, capacity, location) 
  Example: [("T1", 4, "window"), ("T2", 2, "center"), ("T3", 6, "window"), ("T4", 4, "corner")]
  
- reservations: list of reservation requests in format:
  [
    ("R1", "19:00", 4, "window"),
    ("R2", "19:30", 2, "any"),
    ("R3", "20:00", 6, "window"),
    ("R4", "19:00", 3, "center"),
    ("R5", "19:30", 5, "any")
  ]
  Where each tuple is: (reservation_id, time, party_size, preferred_location)
  
- restaurant_hours: ("18:00", "23:00")  # opening and closing times

Rules:
1. Tables can only be reserved within restaurant hours
2. Reservation time is when guests arrive (occupancy is 2 hours)
3. Preferred location: "any" means any location, otherwise try to match preference
4. Party must fit at table (party_size ≤ table_capacity)
5. No table can have overlapping reservations
6. Try to satisfy location preference when possible
7. If exact preference not available, use any available table
8. Return empty dict if reservation time outside hours

Return:
- Dictionary of assignments: {reservation_id: table_id}
- Return empty dict on any error

Example output:
{
    "R1": "T1",  # 4 people, window preference
    "R2": "T2",  # 2 people, any location  
    "R3": "T3",  # 6 people, window preference
    "R4": "T4",  # 3 people, center preference (but T4 is corner - rule 7)
    "R5": ""     # No table fits 5 people (T3 already booked at 19:30-21:30)
}
"""

def convertTimeToMinutes(time):
   split_time = time.split(':')
   hour = int(split_time[0]) * 60
   return hour + int(split_time[1])

def is_restuarant_hours(restaurant_open, restuarant_close, reserved_time):
   return reserved_time >= restaurant_open and reserved_time <= restuarant_close 


def check_table_fit(table_capacity,party_size):
   return party_size <= table_capacity

def is_table_overlap(start_time,end_time,table_schedules,table_id):
   for sched in table_schedules[table_id]:

      exist_start,exist_end = sched
      if start_time < exist_end and end_time > exist_start:
       return True  # overlap detected
   return False
  
   
   
   
def table_reservation():

  tables = [("T1", 4, "window"), ("T2", 2, "center"), ("T3", 6, "window"), ("T4", 4, "corner")] # (table_id, capacity, location)
  reservations =   [
    ("R1", "17:00", 4, "window"),
    ("R2", "19:30", 2, "any"),
    ("R3", "20:00", 6, "window"),  # (reservation_id, time, party_size, preferred_location)
    ("R4", "19:00", 3, "center"),
    ("R5", "19:30", 5, "any")
  ]
  table_map = {table_id:(capacity,location) for (table_id, capacity, location) in tables}
 

  by_location =   {location: [] for (table_id,capacity,location) in tables}
  for (table_i,capacity,location) in tables:
     by_location[location].append(table_i)


  restaurant_hours = ("18:00", "23:00")
  restaurant_open, restaurant_close = restaurant_hours
  restaurant_open = convertTimeToMinutes(restaurant_open)
  restaurant_close = convertTimeToMinutes(restaurant_close) 

  assignments  = {}
  table_schedules = {table_i:[] for (table_i, capacity, location) in tables}

  
  for reservation in reservations:
     #0(R)
     reservation_id, reserved_time,party_size,preferred_location = reservation

     start_time = convertTimeToMinutes(reserved_time)
     end_time = start_time + 120
  

      #1. Tables can only be reserved within restaurant hours
     is_restuarant_hr = is_restuarant_hours(restaurant_open,restaurant_close,start_time)
     if is_restuarant_hr == False:
        continue
     candidate_ids = set()
     
     if preferred_location == 'any':
      for t_id in by_location.values():
        candidate_ids.update(t_id)
     else:
        candidate_ids.update(by_location[preferred_location])
     

     for table_d in candidate_ids:
               
          table = table_map[table_d]
          table_capacity, table_location = table

   
          is_table_fit = check_table_fit(table_capacity,party_size)
        
          if is_table_fit == False:
            continue # go to next table
        
          # initialize assignments
          assignments.setdefault(reservation_id)
        
          # 5. No table can have overlapping reservations
          is_overlap = is_table_overlap(start_time,end_time,table_schedules,table_d)

          if is_overlap:
           continue
  
          table_schedules[table_d].append((start_time,end_time))
          assignments[reservation_id] = table_d
          break
  
  
  return assignments
       
        
  
        


        



        
def main():
    
    print(table_reservation())


main()


