## handles Errors and Exceptions in python by exiting the program with a message.

import time
import sys
def daisy(error_code):
    display_code = f"Encountered Program Error: {error_code}"
    print (f"{display_code}\n Exiting Program")
    time.sleep(2)