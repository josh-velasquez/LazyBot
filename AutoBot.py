import mouse
import time
import sys

def timerDisplay(duration, message):
    mins, secs = divmod(duration, 60)
    print(message ,': {:02d}:{:02d}'.format(mins, secs), end="\r")

def main(duration = 900):
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
    except KeyboardInterrupt as keyInterrupt:
        remap = input("Remap click location? (y/n)")
        if (remap.lower() == "y"):
            main()
        else:
            print("Stopping now.." + str(keyInterrupt))
            sys.exit(0)
    except Exception as e:
        print("Failed to run clicker..." + str(e))
        print("Stopping now...")
        sys.exit(0)


main()