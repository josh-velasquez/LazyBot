from pynput.mouse import Button, Controller, Listener
import time
import sys

mouse = Controller()

def timerDisplay(duration, message):
    mins, secs = divmod(duration, 60)
    print(message ,': {:02d}:{:02d}'.format(mins, secs), end="\r")

# duration = seconds
# click every 300 seconds (5 mins)
def main(duration = 300):
    try:
        clickCounter = 0
        print("Waiting for user to click target position...")
        clicked = False
        xLocation, yLocation = None, None

        # Function to capture the first click event
        def on_click(x, y, button, pressed):
            nonlocal clicked, xLocation, yLocation
            if pressed and button == Button.left:
                xLocation, yLocation = x, y
                clicked = True
                return False  # Stop the listener once the target is clicked

        # Start a listener to capture mouse clicks
        with Listener(on_click=on_click) as listener:
            listener.join()

        print(f"Target location logged: X: {xLocation} Y: {yLocation}")
        print("Starting click program...\n")

        # Timer loop for repeated clicking
        timer = duration
        while True:
            timerDisplay(timer, "Next Click")
            time.sleep(1)
            timer -= 1
            if timer == -1:
                clickCounter += 1
                mouse.position = (xLocation, yLocation)
                mouse.click(Button.left, 1)
                print("\nClicked!")
                print(f"Click Counter: {clickCounter}\n")
                timer = duration
    except KeyboardInterrupt as keyInterrupt:
        remap = input("Remap click location? (y/n) ")
        if remap.lower() == "y":
            main()
        else:
            print("Stopping now.." + str(keyInterrupt))
            sys.exit(0)
    except Exception as e:
        print("Failed to run clicker..." + str(e))
        print("Stopping now...")
        sys.exit(0)

main()
