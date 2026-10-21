# Set Operators
from pyscript import display, document


def student_members(e):
    document.getElementById('output').innerHTML = '' # No multiple outputs
    student_fname = document.getElementById('student_firstname').value
    student_lname = document.getElementById('student_lastname').value
    full_name = student_fname + ' ' + student_lname

    club7 = {'Chiikawa Dela Cruz', 'Usagi Santos'}
    club8 = {'Hachiware Bautista', 'Momonga Garcia'}
    club9 = {'Rakko Ramos', 'Kurimanju Fernandez'}
    club10 = {'Shisa Castillo', 'Furuhonya Gonzales'}
    club_members = club7 | club8 | club9 | club10
    new_member = club_members | {full_name} # Adds the member

    display_len = (len(club_members | new_member)) # Amount of members
    display_message = (f'Here is the updated list of club members: {club_members | new_member}. The total amount of members are: {display_len}') 

    display(display_message, target='output')  