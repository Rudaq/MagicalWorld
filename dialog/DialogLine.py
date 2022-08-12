class DialogLine:
    def __init__(self, text, position, color):
        super().__init__()
        self.text = text
        self.transparent = False
        self.position = position
        self.color = color