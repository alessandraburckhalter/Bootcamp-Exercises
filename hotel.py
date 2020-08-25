print("=-=" * 20)
print("                           HOTEL")
print("=-=" * 20)
# dicticonary
hotel = {
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}

# create function is_vacant
def is_vacant(which_hotel, rooms):
    if "guest" in which_hotel[rooms]:
        return True
    else :
        return False

new_guest = {
    'guest': {
        'name': 'Derek',
        'phone': 8923
    }
}

# create  a function for check in
def check_in(rooms, guest_dictionary):
    if is_vacant(hotel, rooms) :
        print("pick a different a room")
    else:
        hotel[rooms]= guest_dictionary
        print(f"\n{hotel[rooms]} checked in to room {rooms}.")

# call function is_vacant to check room availability
print("\nIs there a guest in the room? ", is_vacant(hotel, '102'))
# assign a person to the available room
check_in('102', new_guest)
# print hotel list with the new guest
print(f"\nHotel info: {hotel}")

# create a function for check out
def check_out(rooms):
    if is_vacant ==  True:
        return "nothing"
    else :
        hotel[rooms] = {}
    print(f"\nUpdated hotel info: {hotel}")
check_out('102')






hotel2 = {
     '201': {
        'guest': {
            'name': 'Alessandra',
            'phone': 1515151
        }
    },
    '202': {},
    '203': {},
    '204': {
        'guest': {
            'name': 'Jacky',
            'phone': 9009099
         }
    },
    '205': {},
}

hotel3 = {
     '301': {
        'guest': {
            'name': 'Alessandra',
            'phone': 1515151
        }
    },
    '302': {},
    '303': {},
    '304': {
        'guest': {
            'name': 'Jacky',
            'phone': 9009099
         }
    },
    '305': {},
}

hotel4 = {
     '401': {
        'guest': {
            'name': 'Alessandra',
            'phone': 1515151
        }
    },
    '402': {},
    '403': {},
    '404': {
        'guest': {
            'name': 'Jacky',
            'phone': 9009099
         }
    },
    '405': {},
}
hotels = [hotel2, hotel3, hotel4]
def print_status():
    for hotel in hotels:
        for key in hotel.keys():
            if hotel[key]:
                print(f"{key} Guest name: {hotel[key]['guest']['name']}.")
            else:
                print(f"Room {key} is empty.")

def check_in2(user_checkin_hotel, user_checking_room):
    if 


while True:
    user_input = int(input("""\nMain Menu
    \nWhat would you like to do?
    \n[1] Print hotel room status 
    \n[2] Check in customer
    \n[3] Check out customer
    \n[4] Quit\n> """))
    print(user_input)
    if user_input == 1:
        print_status()
    if user_input == 2:
        user_checkin_hotel = input("What hotel would you like? ").lower()
        user_checking_room = int(input("What room would you like?")


