from modules.geometry.dimensions import Dimensions3D
from modules.mechanical.turbines import Turbine

def main():
    d = Dimensions3D(length=1.0, width=0.5, height=0.3)
    print("Volumen:", d.volume(), "m³")
    print("Área superficial:", d.surface_area(), "m²")

    t_d = Dimensions3D(length=0.2, width=0.3, height=0.3)
    turbine = Turbine(dimensions=t_d, rpm=2800)
    print("Área:", turbine.area(), "m²")
    print("Volumen por revolución:", turbine.volume_per_rev(), "m³")
    print("Caudal volumétrico:", turbine.volume_flow_rate(), "m³/s")
    print("Caudal másico:", turbine.mass_flow_rate(), "kg/s")
    print("Velocidad de salida:", turbine.velocity_out(), "m/s")
    # Ejemplo de presión diferencial: 150 Pascales
    print("Potencia mecánica:", turbine.mechanical_power(pressure_increase_Pa=150), "W")

if __name__ == "__main__":
    main()

