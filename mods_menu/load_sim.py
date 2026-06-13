## copilot generated loading animation for terminal applications.
## import 
import sys
import time

def loading(duration=4, message="Intializing Program Data"):
    """
    Simulates a loading animation on a single line.
    
    :param duration: Total time in seconds the animation should run
    :param message: The text to display before the dots
    """
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for dots in [".", "..", "...", "   "]:
            # \r moves the cursor back to the start of the line
            # end="" prevents Python from automatically jumping to a new line
            sys.stdout.write(f"\r{message}{dots}")
            sys.stdout.flush()
            time.sleep(0.4)
            
    # Clear the "Loading..." text and leave a clean newline when finished
    sys.stdout.write(f"\r{message}... Loading Complete.\n")

# --- How to use it in your code ---
if __name__ == "__main__":
    print("Initializing system...")
    
    # Drops the animation right here for 4 seconds
    loading(duration=4, message="Connecting to database")
    
    print("Proceeding with the rest of your script!")