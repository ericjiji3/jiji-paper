# screens.py

from PIL import Image, ImageDraw, ImageFont
import time

def lock_screen(width, height):
    image = Image.new("1", (width, height), 255)
    draw = ImageDraw.Draw(image)

    font_big = ImageFont.truetype("assets/Vanosky-Bold.otf", 48)
    font_small = ImageFont.truetype("assets/Acidic.TTF", 20)

    draw.text((20, 40), "To Sonam :D", font=font_big, fill=0)
    # draw.text((20, 110), time.strftime("%H:%M:%S"), font=font_big, fill=0)
    draw.text((20, 100), "Roses are red", font=font_small, fill=0)
    draw.text((20, 130), "Violets are blue", font=font_small, fill=0)
    draw.text((20, 150), "Just like the dishes", font=font_small, fill=0)
    draw.text((20, 170), "Your all I want to do", font=font_small, fill=0)

    return image


def status_screen(width, height):
    image = Image.new("1", (width, height), 255)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("assets/Acidic.TTF", 28)

    # draw.text((20, 40), "System Status", font=font, fill=0)
    # draw.text((20, 90), "WiFi: Connected", font=font, fill=0)
    draw.text((20, 130), "♡Will you be my valentine?♡", font=font, fill=0)
    # draw.text((20, 170), "Model: Offline", font=font, fill=0)

    return image
