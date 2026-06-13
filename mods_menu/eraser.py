## Eraser clears the running terminal window for clean output
## import mods here
import os
## define eraser function
def clear_screen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
## __if__ for best practice run.
if __name__ == '__main__':
	clear_screen()
