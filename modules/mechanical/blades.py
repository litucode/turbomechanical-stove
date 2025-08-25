class Blade():
    def __init__(self, dimension = None):
        self.dimension = dimension
        self.angle = 0

    def surface_area(self):
        """Calcula el área superficial de la hoja (m²)."""
        # todo: add an angle
        return 2 * (self.dimension.length * self.dimension.width + self.dimension.length * self.dimension.height + self.dimension.width * self.dimension.height)

    def volume(self):
        """Calcula el volumen de la hoja (m³)."""
        # todo: add an angle
        return self.dimension.length * self.dimension.width * self.dimension.height