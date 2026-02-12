# display.py
import sys
import os

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd4in2_V2
from PIL import Image

class Display:
    def __init__(self):
        self.epd = epd4in2_V2.EPD()
        self.epd.init_fast(self.epd.Seconds_1_5S)

        self.width = self.epd.width     # 400
        self.height = self.epd.height   # 300

    def clear(self):
        self.epd.init()
        self.epd.Clear()

    def show_fast(self, image):
        self.epd.display_Fast(self.epd.getbuffer(image))

    def show_partial(self, image):
        self.epd.display_Partial(self.epd.getbuffer(image))

    def sleep(self):
        self.epd.sleep()
