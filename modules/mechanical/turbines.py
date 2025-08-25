import math

from modules.geometry.dimensions import Dimensions3D
from modules.mechanical.blades import Blade

class Turbine():
    def __init__(self, rpm, dimensions=None):
        self.rpm = rpm                # Revoluciones por minuto
        self.blades = []              # Lista de cuchillas
        self.blades_counter = 4  # Ejemplo de 4 cuchillas
        if dimensions is not None:
            self.dimensions = dimensions
            self.diameter = dimensions.width / 2
        else:
            pass

    def area(self):
        """Área transversal de la turbina (m²)."""
        return math.pi * (self.diameter / 2) ** 2

    def blade_calc(self):
        i = 0
        while i < (self.blades_counter + 1):
            # Realiza cálculos con cada cuchilla
            blade.angle = 30  # Ejemplo de ángulo
            blade_dimensions = Dimensions3D(.1,.2,.3)
            blade = Blade(blade_dimensions)

            self.blades.append(blade)
            i += 1

    def volume_per_rev(self):
        """Volumen teórico desplazado por una revolución (m³)."""
        return self.area() * self.dimensions.length

    def volume_flow_rate(self):
        """Caudal volumétrico de aire (m³/s)."""
        rev_per_sec = self.rpm / 60
        return self.volume_per_rev() * rev_per_sec

    def mass_flow_rate(self, air_density_kg_m3=1.225):
        """Caudal másico de aire (kg/s)."""
        return self.volume_flow_rate() * air_density_kg_m3

    def velocity_out(self):
        """Velocidad teórica de salida del aire (m/s)."""
        # v = Q / A
        Q = self.volume_flow_rate()
        A = self.area()
        if A == 0:
            return 0
        return Q / A

    def mechanical_power(self, pressure_increase_Pa):
        """Potencia mecánica generada por la turbina (W).
        
        Parámetros:
            pressure_increase_Pa: Diferencia de presión a través de la turbina en Pascales.
        """
        Q = self.volume_flow_rate()  # m³/s
        return pressure_increase_Pa * Q  # W (J/s)

    def __str__(self):
        return (f"Turbine(diameter={self.diameter} m, length={self.dimensions.length} m, rpm={self.rpm})")