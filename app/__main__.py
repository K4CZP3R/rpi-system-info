from app.models.interfaces.display import Display
from app.models.interfaces.hardware import Hardware
from typing import List
from time import time

class App:
    def __init__(self, display: Display, modules: List[Hardware]):
        self.display = display
        self.hardware_modules = modules

        self.current_module = 0
        self.last_change = time()
        self.render = True

    def loop(self):

        if self.render is True:
            self.display.clear()
            self.hardware_modules[self.current_module].update()
            self.display.print(f"{self.hardware_modules[self.current_module]}",0)
            self.display.print(f"{self.hardware_modules[self.current_module].get()}",1)
            self.render = False

        if time() - self.last_change > 5:
            self.last_change = time()
            self.render = True
            self.current_module += 1
            if self.current_module > len(self.hardware_modules) - 1:
                self.current_module = 0