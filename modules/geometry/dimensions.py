class Dimensions3D:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surface_area(self):
        lw = self.length * self.width
        lh = self.length * self.height
        wh = self.width * self.height
        return 2 * (lw + lh + wh)
