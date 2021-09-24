from app.modules.i2c_dev import Lcd
from app.models.interfaces.display import Display


class I2CLcd(Display):
    def __init__(self):
        super().__init__()
        self.display = Lcd()

    def print(self, content, line):
        self.display.lcd_display_string(content, line + 1)