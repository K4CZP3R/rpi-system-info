from app.models.interfaces.hardware import Hardware


class Memory(Hardware):
    def __init__(self, display_name: str):
        super().__init__("mem")
        self.display_name.append(display_name)