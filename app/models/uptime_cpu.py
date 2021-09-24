from app.models.interfaces.processor import Processor
from typing import List
import psutil


class UptimeCPU(Processor):
    def __init__(self):
        super().__init__('uptime')
        self.avgs: List[float] = [0.0,0.0,0.0]

    def get(self):
        return ",".join( str(x) for x in self.avgs)

    def update(self):
        try:
            raw = open('/proc/loadavg', 'r').read()
            splitted = raw.split(" ")
            for i in range(0, 3):
                self.avgs[i] = float(splitted[i])
        except:
            pass

