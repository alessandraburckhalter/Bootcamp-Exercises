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




teste = {

    'hotel2' : {
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
    },

    'hotel3' : {
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
    },

    'hotel4' : {
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
}

def print_status():
    for hotel in teste:
        for room, info in teste[hotel].items():
            if len(info) > 0 :
                print(f'Room {room} ococcupied')
            else:
                print(f'Room {room} is empty.')

def check_in2(nome, user_checking_room):
    teste[nome] = user_checking_room
    print(f"\n{teste[hotel]} checked in to room {hotel}.")

while True:
    user_input = int(input("""\nMain Menu
    \nWhat would you like to do?
    \n[1] Print hotel room status 
    \n[2] Check in customer
    \n[3] Check out customer
    \n[4] Quit\n> """))
    if user_input == 1:
        print_status()
    print("=-=" * 20)
    if user_input == 2:
        for name, place in teste.items():
            print(name.title())
        user_checkin_hotel = input("Which hotel would you like to stay in? ").lower()
        print_status()
        user_checking_room = int(input("What room would you like?"))
        check_in2(hotel, user_checking_room)
       

