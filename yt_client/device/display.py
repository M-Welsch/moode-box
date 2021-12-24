from yt_client.device.utils import hardware


if hardware() == "rpi":
    import board
    import digitalio
    import adafruit_ssd1306
else:
    print("sorry, display doesnt work here. Aborting")
    exit()

from PIL import Image, ImageDraw, ImageFont


class Params:
    WIDTH = 128
    HEIGHT = 64
    BORDER = 5


class Display:
    def __init__(self):

        oled_reset = digitalio.DigitalInOut(board.D4)



        spi = board.SPI()
        oled_cs = digitalio.DigitalInOut(board.D5)
        oled_dc = digitalio.DigitalInOut(board.D6)
        self._dis = adafruit_ssd1306.SSD1306_SPI(Params.WIDTH, Params.HEIGHT, spi, oled_dc, oled_reset, oled_cs)

    def clear(self):
        self._dis.fill(0)
        self._dis.show()

    def hello_world_test(self):
        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (self._dis.width, self._dis.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a white background
        draw.rectangle((0, 0, self._dis.width, self._dis.height), outline=255, fill=255)

        # Draw a smaller inner rectangle
        draw.rectangle(
            (Params.BORDER, Params.BORDER, self._dis.width - Params.BORDER - 1, self._dis.height - Params.BORDER - 1),
            outline=0,
            fill=0,
        )

        # Load default font.
        font = ImageFont.load_default()

        # Draw Some Text
        text = "Hello Wörld!"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (self._dis.width // 2 - font_width // 2, self._dis.height // 2 - font_height // 2),
            text,
            font=font,
            fill=255,
        )

        # Display image
        self._dis.image(image)
        self._dis.show()