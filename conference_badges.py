# Write your code here.

def badge_maker(name):
  return "Hello, my name is {}.".format(name)

def batch_badge_creator(attendees):
  badges = []
  for attendee in attendees:
    badges.append(badge_maker(attendee))
  return badges

def assign_rooms(attendees):
  rooms = []
  counter = 1
  for attendee in attendees:
    room_assignment = "Hello, {}! You'll be assigned to room {}!".format(attendee, counter)
    rooms.append(room_assignment)
    counter += 1
  return rooms

def printer(attendees):
  final_string = ""
  badges = batch_badge_creator(attendees)
  for badge in badges:
    final_string += (badge + "\n")
  room_assignments = assign_rooms(attendees)
  for assignment in room_assignments:
    final_string += (assignment + "\n")
  return final_string.strip()
