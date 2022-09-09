import keyboard
import mouse
import time
import sys

# 15 minutes duration
# https://github.com/boppreh/mouse#api
def clicker(duration = 900):
    try:
        print("Waiting for user to click target position...")
        clicked = False
        while(not clicked):
            if (mouse.is_pressed("left")):
                xLocation, yLocation = mouse.get_position()
                clicked = True

        print("Target location logged: X: " + str(xLocation) + " Y: " + str(yLocation))
        print("Starting click program...\n")
        # record initial press
        while(True):
            mouse.move(xLocation, yLocation)
            mouse.click("left")
            print("Clicked!")
            time.sleep(int(duration)) 
    except KeyboardInterrupt:
        print("Stopping now..")
        sys.exit(0)
    except Exception:
        print("Failed to run clicker...")
        print("Stopping now...")
        sys.exit(0)

# 900 = 15 minutes
def typer(keystrokes = "a", delay = 900):
    print("Starting typer program...\n")
    try:
        while(True):
            keyboard.write(keystrokes)
            print("Typed!")
            time.sleep(int(delay))
    except KeyboardInterrupt:
        print("Stopping now..")    
        sys.exit(0)
    except Exception:
        print("Failed to run typer...")
        print("Stopping now...")
        sys.exit(0)

# def incognito():
    

def main():
    print("Welcome to LazyBot!")
    print("Options:")
    print("0. Auto clicker")
    print("1. Auto keystrokes")
    print("2. Manual clicker")
    print("3. Manual keystrokes")
    print("4. Exit")


    mode = input("Select a mode: ")
    match mode:
        case "0":
            clicker()
        case "1":
            typer()
        case "2":
            duration = input("Duration per per click (seconds): ")
            clicker(duration)
        case "3":
            keystrokes = input("Enter the keystrokes combination: ")
            delay = input("Enter delay duration (seconds): ")
            typer(keystrokes, delay)
        case _:
            sys.exit(0)



main()

# keyboard 
# LazyBot