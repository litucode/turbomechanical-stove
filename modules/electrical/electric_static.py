from dataclasses import dataclass

@dataclass
class StaticParams:
    air_velocity: float           # m/s
    material_type: str           # 'metal', 'plastico', 'vidrio', etc.
    humidity: float              # [0-1] fracción
    surface: float               # m^2

class StaticElectricity:
    """
    Módulo para simular la acumulación y efectos de electricidad estática.
    """
    # Factores simplificados por material, pueden personalizarse
    MATERIAL_FACTORS = {
        'metal': 0.1,
        'plastic': 0.8,
        'glass': 0.5,
        'other': 0.3
    }

    def __init__(self, params: StaticParams):
        self.params = params

    def calculate_charge(self) -> float:
        """
        Calcula la carga acumulada (Coulombs, simplificado)
        """
        f_material = self.MATERIAL_FACTORS.get(self.params.material_type, self.MATERIAL_FACTORS['other'])
        friction = self.params.air_velocity * (1 - self.params.humidity) * self.params.surface
        charge = friction * f_material
        return charge

    def electric_potential(self) -> float:
        """
        Calcula el potencial eléctrico generado (Voltios, simplificado)
        """
        charge = self.calculate_charge()
        if self.params.surface == 0:
            return 0
        return charge / self.params.surface

    def condensation_effect(self, air_temperature: float) -> bool:
        """
        Determina si la electricidad estática puede inducir condensación (simplificado)
        """
        # Umbral arbitrario para ejemplo
        return self.electric_potential() > 10 and air_temperature > 30

# Ejemplo de uso
if __name__ == "__main__":
    temp_start = -20 # °C
    temp_end = 45 + 1 # °C
    materials = ['metal', 'plastic', 'glass', 'other']
    calc_range = {"start": 0, "end": 100, "step": 10}
    
    for temp in range(temp_start, temp_end, 5):
        for material in materials:
            for i in range(calc_range["start"], calc_range["end"], calc_range["step"]):
                params = StaticParams(
                    air_velocity=15,
                    material_type=material,
                    humidity=calc_range["step"]/100,
                    surface=2.5
                )
                module = StaticElectricity(params)
                if module.condensation_effect(air_temperature=temp):
                    print(f"Material: {material} | Temp: {temp:>3}°C | Charge: {module.calculate_charge()} C | Potential: {module.electric_potential()} V | Condensation: {'Sí' if module.condensation_effect(air_temperature=temp) else 'No'}")
