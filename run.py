from app.__main__ import App
from app.models.dummy_lcd import DummyLcd
from app.models.thermalzone_temp import ThermalZoneTemp
from app.models.psutil_memory import PsutilMemory
from app.models.uptime_cpu import UptimeCPU

app = App(DummyLcd(), [ThermalZoneTemp(), PsutilMemory(), UptimeCPU()])
while True:
    app.loop()