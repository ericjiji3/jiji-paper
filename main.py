# main.py

from display import Display
import screens
import time

def main():
    display = Display()
    try:
        # --- Lock screen ---
        image = screens.lock_screen(display.width, display.height)
        display.show_fast(image)
        time.sleep(5)

        # --- Status screen ---
        image = screens.status_screen(display.width, display.height)
        display.show_fast(image)
        time.sleep(2)

        # --- Start camera once (best practice) ---
        # screens.py has a global picam2, so we can start it here once.
        try:
            screens.picam2.start()
        except Exception:
            # If it's already started or start fails, we'll still try to capture in the loop
            pass

        # --- Camera stream loop (slow, e-ink friendly) ---
        frame_count = 0
        clear_every = 20          # full clear every N frames to reduce ghosting
        interval_sec = 3.0        # 1 frame every 3 seconds

        while True:
            frame_img = screens.camera_screen(display.width, display.height)
            display.show_fast(frame_img)

            frame_count += 1
            if clear_every and (frame_count % clear_every == 0):
                display.clear()

            time.sleep(interval_sec)

    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        # Stop camera if possible
        try:
            screens.picam2.stop()
        except Exception:
            pass

        display.sleep()

if __name__ == "__main__":
    main()
