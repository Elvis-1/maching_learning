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

def checkCapacity(room_capacity,attendee):
   return room_capacity >= attendee

def convertTimeToMinutes(time):
   split_time = time.split(':') #['10', '30']
   minutes = int(split_time[0]) * 60

   
   return minutes + int(split_time[1])

def checkOverlap(meetings,start_time, end_time):
   # ("Team Beta", "10:00", "11:30"),
        #    if start_minutes < existing_end and existing_start < end_minutes:
        #     return True
    if not meetings:
       return {}
    for meeting in meetings:
     _,existing_start,existing_end = meeting
     existing_start_minutes = convertTimeToMinutes(existing_start)
     existing_end_minutes = convertTimeToMinutes(existing_end)

     start_minutes = convertTimeToMinutes(start_time)
     end_minutes = convertTimeToMinutes(end_time)

     if start_minutes < existing_end_minutes and existing_start_minutes < end_minutes:
        return True #overlap detected
    return False

   
   
   
   
   
def scheduleConferenceRooms():
 rooms =   [("A", 10), ("B", 20), ("C", 15)]
 meetingRequest = [
    ("Team Alpha", "09:00", "10:30", 8),
    ("Team Beta", "10:00", "11:30", 12),
    ("Team Gamma", "14:00", "15:00", 25),
    ("Team Delta", "14:30", "15:30", 6)
  ]
 


 if not rooms:
    return {}
 if not meetingRequest:
    return {}
 # initialize schedule meetings
# sort rooms

 rooms = sorted(rooms, key=lambda x:x[1],reverse=True)

 scheduledMeetinngs = {
   room_name:[] for (room_name, _) in rooms
 }

 # loop through meeting request
 for request in meetingRequest:
    # 0(M)
    if len(request) != 4:
       return {}
    # ("Team Alpha", "09:00", "10:30", 8),
    team_name,start_time,end_time,attendees = request

    for room in rooms:
       # 0(R)
       room_name, room_capacity = room
        # check capacity
       capacity =  checkCapacity(room_capacity,attendees)

       if capacity == False:
         continue

        # check overlap
       meetings = scheduledMeetinngs[room_name]
       isOverlap = checkOverlap(meetings,start_time,end_time) # 0(M)

       if isOverlap == True:
          continue

       scheduledMeetinngs[room_name].append((team_name,start_time,end_time))
       break
 

 print(scheduledMeetinngs)
 

 

  


def main():
    scheduleConferenceRooms()
  

main()