from app.models.interfaces.memory import Memory
import psutil


class PsutilMemory(Memory):
    def __init__(self):
        super().__init__('psutil')
        self.mem_used = 0

    def get(self):
        return self.mem_used

    def update(self):
        self.mem_used = psutil.virtual_memory().percent
