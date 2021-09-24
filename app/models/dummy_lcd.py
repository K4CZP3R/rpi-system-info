from app.models.interfaces.display import Display


class DummyLcd(Display):
    def __init__(self):
        super().__init__()
        self.buffer = ["".ljust(16, " "),"".ljust(16, " ")]

    def print(self, content: str, line: int):
        self.buffer[line] = content[:16].ljust(16, " ")

        if(line == 1):
            self.__push_buffer()

    def __push_buffer(self):
        print("-"*18)
        print(f"|{self.buffer[0]}|")
        print(f"|{self.buffer[1]}|")
        print("-"*18)