RED = "\033[1;31m"
GREEN =  "\033[1;32m"
YELLOW = "\033[1;33m"
NOCOLOR = "\033[0m"

INPUT = f"{YELLOW}[INPUT]{NOCOLOR}"
OUTPUT = f"{GREEN}[OUTPUT]{NOCOLOR}"
ERROR = f"{RED}[ERROR]{NOCOLOR}"

room_and_occupancy = {
    "R101": False,
    "R102": False,
    "R103": False,
    "R104": True,
    "R105": False,
    "R106": False,
    "R107": False,
    "R108": True,
    "R109": False,
    "R110": False,
    "R111": True,
    "R112": False,
    "R113": True,
    "R114": False,
    "R115": False,
    "R116": False,
    "R117": True,
    "R118": False,
    "R119": False,
    "R120": False,
}

is_valid_room = lambda room: room in room_and_occupancy
is_available = lambda room: not room_and_occupancy[room]

# def is_valid_date(date):
#     pattern = r'^(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])/20[0-9]{2}$'
#     return re.match(pattern, date)

def is_valid_duration(day):
    try:
        int(day)
    except:
        return False
    else:
        day = int(day)
        return day > 0 and day <= 100
    
def validate_info(info, validators):
    if not validators:
        return True
    
    first = validators[0]
    if first(info):
        return validate_info(info, validators[1:])
    else:
        return False

def get_pax_info(
        pax_info={},
        status=[
            ["Room Number", False, (is_valid_room, is_available)],
            ["Duration", False, (is_valid_duration,)],
            # [info, is_info_valid?, [functions_to_validate_info]]
    ]):
    if not status:
        return pax_info

    first = status[0]

    info = first[0]
    has_valid_info = first[1]
    validators = first[2]

    if has_valid_info:
        return get_pax_info(pax_info, status[1:])
        
    temp = input(f"{INPUT} {info}: ")
    if validate_info(temp, validators):
        has_valid_info = True
        pax_info[info] = temp
        return get_pax_info(pax_info, status[1:])
    
    if info == "Room Number":
        print(f"{ERROR} {info} is either invalid or already occupied! Please try again.\n")
    else:
        print(f"{ERROR} {info} is invalid! Please try again.\n")

    return get_pax_info(pax_info, status)

def book(pax_info=None):
    if pax_info is None:
        pax_info = get_pax_info()

    check_in = input(f"{INPUT} Check-in Date: ")
    name = input(f"{INPUT} Name: ")
    address = input(f"{INPUT} Address: ")
    phone_number = input(f"{INPUT} Phone Number: ")

    print(f"\n{GREEN}{'Reservation Successful!'.center(30, '-')}{NOCOLOR}")
    print("Name:\t\t", GREEN, name, NOCOLOR)
    print("Room Number:\t", GREEN, pax_info["Room Number"], NOCOLOR)
    print("Check-in Date:\t", GREEN, check_in, NOCOLOR)
    print("Days Staying:\t", GREEN, pax_info["Duration"])
    print(f"{'Enjoy your stay! <3'.center(30, '-')}{NOCOLOR}")
book()
