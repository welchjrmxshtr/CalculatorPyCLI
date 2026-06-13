## Performs calclations to return to display, process input, creates display result string and returns the string to Calc_screen.
## Import modules here
##------------------------------------------
## Basic Python Modules
import time
import sys
##
# Error Handling mods
from error_handling import oopsie
# Math Mods mods
from math_mods import calc_screen
# Mods Menu mods
from mods_menu import eraser
from mods_menu import load_sim
from mods_menu import msg_bar
##------------------------------------------
## gather operation information
def info_grab():
    op_var_1 = float(input("Please enter the first Variable: "))
    op_type_symbol = input("Please Select an Operation Type by symbol, e.g., +, -, *, /.: ")
    op_var_2 = float(input("Please enter the second variable: "))
    return calc_process(op_var_1, op_type_symbol, op_var_2)
## process calculation
def calc_process(op_var_1, op_type_symbol, op_var_2):
    if op_type_symbol == '+':
        add_sum = op_var_1 + op_var_2
        return add_sum
    elif op_type_symbol == '-':
        sub_diff = op_var_1 - op_var_2
        return sub_diff
    elif op_type_symbol == '*':
        multi_pro = op_var_1 * op_var_2
        return multi_pro
    elif op_type_symbol == '/':
        div_quot = op_var_1 / op_var_2
        return div_quot
    elif op_type_symbol == '%':
        prcnt_of_var_2 = (op_var_1 / op_var_2) * 100
        return prcnt_of_var_2
    elif op_type_symbol == '^' or op_type_symbol == '**':
        exponent_result = op_var_1 ** op_var_2
        return exponent_result
    else:
        error_code = '0x000002: Could not complete calculation.'
        oopsie.daisy(error_code)
        sys.exit()


    