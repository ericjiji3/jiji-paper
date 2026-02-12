# screens.py

from PIL import Image, ImageDraw, ImageFont, ImageOps
import time
from picamera2 import Picamera2
import numpy as np

# Initialize camera once globally (important)
picam2 = Picamera2()
cam_w, cam_h = 640, 380
config = picam2.create_still_configuration(
    main={"size": (cam_w, cam_h), "format": "RGB888"}
)
picam2.configure(config)


def lock_screen(width, height):
    image = Image.new("1", (width, height), 255)
    draw = ImageDraw.Draw(image)

    font_big = ImageFont.truetype("assets/Vanosky-Bold.otf", 48)
    font_small = ImageFont.truetype("assets/Acidic.TTF", 20)

    draw.text((20, 40), "TESTING SHIT", font=font_big, fill=0)
    # draw.text((20, 110), time.strftime("%H:%M:%S"), font=font_big, fill=0)
    draw.text((20, 100), "Could get Stinky", font=font_small, fill=0)

    return image


def status_screen(width, height):
    image = Image.new("1", (width, height), 255)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("assets/Acidic.TTF", 28)

    # draw.text((20, 40), "System Status", font=font, fill=0)
    # draw.text((20, 90), "WiFi: Connected", font=font, fill=0)
    draw.text((20, 130), "STatus Screen", font=font, fill=0)
    # draw.text((20, 170), "Model: Offline", font=font, fill=0)

    return image


def camera_screen(width, height):
    """
    Capture one frame from camera and convert for 4.2" e-paper (400x300 landscape)
    """
    # Capture frame as numpy array
    frame = picam2.capture_array()

    # Convert numpy array to PIL Image
    image = Image.fromarray(frame)

    # Convert to grayscale
    image = image.convert("L")

    # Improve contrast for e-ink
    image = ImageOps.autocontrast(image)

    # Resize to exact e-paper resolution
    image = image.resize((width, height))

    # Convert to 1-bit black/white with dithering
    image = image.convert("1")

    return image
