from app.models.interfaces.hardware import Hardware


class Processor(Hardware):
    def __init__(self, display_name: str):
        super().__init__("cpu")
        self.display_name.append(display_name)
