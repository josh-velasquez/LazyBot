import keyboard
import mouse
import time
import sys

def timerDisplay(duration, message):
    mins, secs = divmod(duration, 60)
    print(message ,': {:02d}:{:02d}'.format(mins, secs), end="\r")

# 15 minutes duration
# https://github.com/boppreh/mouse#api
def clicker(duration = 900):
    try:
        clickCounter = 0
        print("Waiting for user to click target position...")
        clicked = False
        while(not clicked):
            if (mouse.is_pressed("left")):
                xLocation, yLocation = mouse.get_position()
                clicked = True

        print("Target location logged: X: " + str(xLocation) + " Y: " + str(yLocation))
        print("Starting click program...\n")
        # record initial press
        timer = duration
        while(True):
            timerDisplay(timer, "Next Click")
            time.sleep(1)
            timer -= 1
            if (timer == -1):
                clickCounter += 1
                mouse.move(xLocation, yLocation)
                mouse.click("left")
                print("\nClicked!")
                print("Click Counter: " + str(clickCounter) + "\n")
                timer = duration
            
    except KeyboardInterrupt:
        print("Stopping now..")
        sys.exit(0)
    except Exception as e:
        print("Failed to run clicker..." + str(e))
        print("Stopping now...")
        sys.exit(0)

# 900 = 15 minutes
def typer(keystrokes = "a", delay = 900):
    print("Starting typer program...\n")
    try:
        typeCounter = 0
        timer = delay
        while(True):
            timerDisplay(timer, "Next Type")
            time.sleep(1)
            timer -= 1
            if (timer == -1):
                typeCounter += 1
                keyboard.write(keystrokes)
                print("\nTyped!")
                print("Type Counter: " + str(typeCounter) + "\n")
                timer = delay
            
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
    print("1. Auto clicker")
    print("2. Auto keystrokes")
    print("3. Manual clicker")
    print("4. Manual keystrokes")
    print("5. Exit")
    print("ctrl + c to exit the whole program.\n")


    mode = input("Select a mode: ")
    match mode:
        case "1":
            clicker()
        case "2":
            typer()
        case "3":
            duration = input("Duration per per click (seconds): ")
            clicker(int(duration))
        case "4":
            keystrokes = input("Enter the keystrokes combination: ")
            delay = input("Enter delay duration (seconds): ")
            typer(keystrokes, int(delay))
        case _:
            sys.exit(0)



main()
