## Calculator mdoule for math_mods, import to menu_mod.py
# this module is used to handle user input for variables, run the calc_engine.py silently, and display results.
##------------------------------------------
## import modules here
# Base python modules
import sys
# Error Handling
from error_handling import oopsie
# math_mods imports
from math_mods import calc_engine
# mods_menu imports
from mods_menu import eraser
from mods_menu import load_sim
from mods_menu import menu_mod
from mods_menu import msg_bar
##------------------------------------------
def display_calc(power_on):
    while power_on == True:    
        load_sim.loading(duration=1, message="Loading Calculator")
        eraser.clear_screen()
        msg_bar.line()
        print("Welcome to the Calculator Module\nPlease follow the prompts to perform calculations.")
        msg_bar.line()
        msg_bar.line()
        result = calc_engine.info_grab()
        print(result)
        keep_going = input('Would you like to continue using the calculator? Y\\N: ')
        if keep_going == 'n':
            power_on = False
            sys.exit()
        elif keep_going == 'y':
            power_on = True
        else:
            sys.exit()

            
        

