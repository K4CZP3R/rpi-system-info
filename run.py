from app.__main__ import App
from app.models.thermalzone_temp import ThermalZoneTemp
from app.models.psutil_memory import PsutilMemory
from app.models.uptime_cpu import UptimeCPU
from app.models.i2c_lcd import I2CLcd
from time import sleep

app = App(I2CLcd(), [ThermalZoneTemp(), PsutilMemory(), UptimeCPU()])
while True:
    app.loop()
    sleep(0.5)