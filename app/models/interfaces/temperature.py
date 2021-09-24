from app.models.interfaces.hardware import Hardware


class Temperature(Hardware):
    def __init__(self, display_name: str):
        super().__init__("tmp")
        self.display_name.append(display_name)
