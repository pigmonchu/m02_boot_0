import turtle

class Race():
    def __init__(self, width, height):
        self.players = []
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.startline = -width / 2 * 0.95
        self.finishline = width / 2 * 0.95
        self.screen.bg('lightgray')