## Menu function, display program tools and accept user input to run task modules.
#
## import modules here
# Error Handling
from error_handling import oopsie
# from math_mods
from math_mods import calc_screen
# from menu_mods
from mods_menu import eraser
from mods_menu import msg_bar
from mods_menu import load_sim
## Define menu function here
def menu():
    load_sim.loading(duration=1, message="Loading options")
    eraser.clear_screen()
    msg_bar.line()
    print("Please Select a function from the list below\nEnter the number assigned to the task to run it.")
    msg_bar.line()
    msg_bar.line()
    option_first = '1. Calculator - Press 1 + ENTER.'
    print(f"{option_first}\n")
    menu_choice = input("SELECTION: ")
    if menu_choice == '1':
        power_on = True
        calc_screen.display_calc(power_on)
    else:
        error_code = '0x000001: Invalid Selection'
        return oopsie.daisy(error_code)
   
        

    