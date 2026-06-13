## main.py runs program by calling menu_mod.py
# 
## import mods here
import sys
import time 
from mods_menu import eraser
from mods_menu import load_sim
from mods_menu import menu_mod
from mods_menu import msg_bar
## define run function that calls the menu here
def run_program():
    msg_bar.line()
    print('Opening Program')
    msg_bar.line()
    load_sim.loading()
    time.sleep(2)
    eraser.clear_screen()
    menu_mod.menu()
    
if __name__ == "__main__":
    run_program()
