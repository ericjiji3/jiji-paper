# main.py

from display import Display
import screens
import time

def main():
    display = Display()

    # Show lock screen
    image = screens.lock_screen(display.width, display.height)
    display.show_fast(image)

    time.sleep(5)

    # Show status screen
    image = screens.status_screen(display.width, display.height)
    display.show_fast(image)

    time.sleep(5)

    display.sleep()

if __name__ == "__main__":
    main()
