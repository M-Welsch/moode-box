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
        self._image = Image.new("1", (self._dis.width, self._dis.height))

    def clear(self):
        draw = ImageDraw.Draw(self._image)
        draw.rectangle((0, 0, self._dis.width, self._dis.height), outline=0, fill=0)
        self._dis.fill(0)
        #self._dis.show()

    def write_text(self, line: int, text: str):
        draw = ImageDraw.Draw(self._image)

        # font = ImageFont.load_default()
        font_size = 12
        font_path = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"
        font = ImageFont.truetype(font_path, font_size)
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (0, (line-1)*font_height+1),
            text,
            font=font,
            fill=255
        )
        self._dis.image(self._image)
        self._dis.show()

    def hello_world_test(self):
        image = Image.new("1", (self._dis.width, self._dis.height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, self._dis.width, self._dis.height), outline=255, fill=255)
        draw.rectangle(
            (Params.BORDER, Params.BORDER, self._dis.width - Params.BORDER - 1, self._dis.height - Params.BORDER - 1),
            outline=0,
            fill=0,
        )
        font = ImageFont.load_default()
        text = "Hello Wörld!"
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (self._dis.width // 2 - font_width // 2, self._dis.height // 2 - font_height // 2),
            text,
            font=font,
            fill=255,
        )
        self._dis.image(image)
        self._dis.show()