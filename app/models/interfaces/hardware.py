class Hardware:
    def __init__(self, display_name:str):
        self.display_name = ["hw", display_name]

    def update(self):
        pass

    def get(self):
        pass

    def __str__(self):
        return "-".join(self.display_name)