import keyboard
import sys
import time
import random

ASCII_LETTERS = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def getRandomLetter():
	return random.choice(ASCII_LETTERS)

def keyboardBot(delay = 1):
    print("Keyboard bot starting...")
    try:
        while(True):
            randomLetter = getRandomLetter()
            keyboard.write(randomLetter)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Stopping now..")
        sys.exit(0)
    except Exception:
        print("Failed to run keyboard bot...")
        print("Stopping now..")
        sys.exit(0)

def main():
    keyboardBot()

main()