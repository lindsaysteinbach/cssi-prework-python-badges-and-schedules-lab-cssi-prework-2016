# Write your code here.
def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(name_list):
    new_name_list=[]

    for item in name_list:
        new_name_list.append(badge_maker(item))

    return new_name_list

def assign_rooms(name_list):
    i = 0
    room_list=[]

    for i in range(0,len(name_list)):
        room_assignment="Hello, " + name_list[i] + "! You'll be assigned to room " + str(i+1) + "!"
        room_list.append(room_assignment)
        i = i+1
    return room_list

def printer(name_list):
    final_string=""
    i = 0
    final_list=batch_badge_creator(name_list)
    room_list=assign_rooms(name_list)

    final_list.extend(room_list)

    for i in range(0,(len(final_list)-1)):
        final_string=final_string + final_list[i] + "\n"
        i = i+1
    return final_string + final_list[len(final_list)-1]
