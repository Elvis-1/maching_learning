"""
Docstring for conference_room_scheduling_sys

A company needs to schedule meetings in conference rooms. Write a function that:

Input:
- rooms: list of room names and capacities [("A", 10), ("B", 20), ("C", 15)]
- meetings: list of meeting requests in format:
  [
    ("Team Alpha", "09:00", "10:30", 8),
    ("Team Beta", "10:00", "11:30", 12),
    ("Team Gamma", "14:00", "15:00", 25),
    ("Team Delta", "14:30", "15:30", 6)
  ]
  Where each tuple is: (team_name, start_time, end_time, attendees)

Rules:
1. Meetings must be assigned to rooms with capacity >= attendees
2. No room can have overlapping meetings
3. Meetings can be moved to any available room that fits
4. If a meeting can't be scheduled, it's skipped
5. Rooms should be utilized as efficiently as possible (fill larger rooms first)

Return:
- Dictionary of scheduled meetings: {room_name: [(team_name, start, end), ...]}
- Return empty dict on any error

Example output:
{
    "B": [("Team Beta", "10:00", "11:30"), ("Team Gamma", "14:00", "15:00")],
    "A": [("Team Alpha", "09:00", "10:30")],
    "C": [("Team Delta", "14:30", "15:30")]
}
"""


# Step 1: Understand the domain
"""
It is about scheduling rooms for different teams
"""
# Step 2: Identify Core Components:
"""
Room : room-name and capacity
Team request: (team_name, start_time, end_time, attendees)
"""

# Step 3: Map Data flow:

"""
input: 
rooms:[("A", 10), ("B", 20), ("C", 15)]
request:
[
    ("Team Alpha", "09:00", "10:30", 8),
    ("Team Beta", "10:00", "11:30", 12),
    ("Team Gamma", "14:00", "15:00", 25),
    ("Team Delta", "14:30", "15:30", 6)
]
Step 1: Validate input
Step 2:


"""

def time_to_minutes(time_str):
     hours,seconds = map(int, time_str.split(':'))
     return hours * 60 + seconds

def minutes_to_time(minutes_str):
   hour = int(minutes_str)//60
   min = int(minutes_str)%60
   time = f"{hour:02d}:{min:02d}"
   return time
   
  
   

def has_overlapping(meetings, start_minutes, end_minutes):
    """Check if new meeting overlaps with any existing meetings"""
    for meeting in meetings:
        if not meeting:
            continue
        
        (_, existing_start_str, existing_end_str) = meeting
        existing_start = time_to_minutes(existing_start_str)
        existing_end = time_to_minutes(existing_end_str)
        
        # CORRECT overlap formula
        if start_minutes < existing_end and existing_start < end_minutes:
            return True
    return False           
   

def schedule_conf_room(rooms,requests): 
  if not rooms or not requests:
    return {}
  sorted_rooms = sorted(rooms, key=lambda x:x[1], reverse=True)
  # initialize schedule
  schedule_meetings = {room_name:[] for room_name,_ in sorted_rooms}


  for request in requests:
     if len(request) != 4:
        continue
     #unpack tuple
     team_name,start_time,end_time,attendees = request
     
     # convert time to comparable format
     start_minutes = time_to_minutes(start_time)     
     end_minutes = time_to_minutes(end_time)

     if start_minutes >= end_minutes:
           continue # invalid time
     if attendees <= 0:
           continue 
    
     scheduled = False
     for room in sorted_rooms:
        room_name,capacity = room

      # rule 1: Meetings must be assigned to rooms with capacity >= attendees

        if capacity < attendees:
           continue
    
        # rule 2: no overlapping meetings
        meetings = schedule_meetings[room_name]
        has_overlap = has_overlapping(meetings,start_minutes,end_minutes)
       
        if has_overlap:
           continue
        # convert back to times
        start_time =  minutes_to_time(start_minutes)
        end_time = minutes_to_time(end_minutes)
        meetings.append((team_name,start_time,end_time))
        scheduled = True
        break
      
     # sort meeting by start time
  for rooms in schedule_meetings:
     schedule_meetings[rooms].sort(key=lambda x:time_to_minutes(x[1]))

     # remove empty rooms
  schedule_meetings = {room_name: meetings for (room_name,meetings) in schedule_meetings.items() if meetings}
  return schedule_meetings


        
        
        
    
def main():
    rooms = [("A", 10), ("B", 20), ("C", 15)]
    requests = [
        ("Team Alpha", "09:00", "10:30", 8),
        ("Team Beta", "10:00", "11:30", 12),
        ("Team Gamma", "14:00", "15:00", 15),  # Changed from 25 to 15
        ("Team Delta", "14:30", "15:30", 6)
    ]
    print(schedule_conf_room(rooms,requests)
)

main()






