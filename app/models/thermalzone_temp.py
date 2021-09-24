from .interfaces.temperature import Temperature


class ThermalZoneTemp(Temperature):
    def __init__(self):
        super().__init__("tz")
        self.temp_value = 0

    def get(self) -> float:
        return self.temp_value

    def update(self):
        try:
            self.temp_value = int(open('/sys/class/thermal/thermal_zone0/temp', 'r').read()) / 1000
        except:
            pass
