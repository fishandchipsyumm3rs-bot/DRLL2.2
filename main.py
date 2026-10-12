# SS
from pyscript import display, document


def name_finders(e):
    last_name = document.getElementById('last_name').value.lower().strip()
    first_name = document.getElementById('first_name').value.lower().strip()
    full_name = last_name + ' ' + first_name
    members= ['bueno zoe', 'sia agatha', 'lao liam', 'mirador jayson']
    member_checker = full_name in members


    display_message = (f'Sorry no {full_name}, you did not get in lil bro', f'{full_name} is in the club!')
    display(display_message[member_checker], target='result')






