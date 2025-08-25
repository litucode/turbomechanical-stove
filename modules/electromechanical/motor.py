class Motor:
    def __init__(self, rated_power_watts, efficiency=0.85):
        self.rated_power = rated_power_watts  # Potencia nominal del motor en Watts
        self.efficiency = efficiency          # Eficiencia eléctrica-mecánica

    def input_power(self, mechanical_power_needed):
        """
        Calcula la potencia eléctrica requerida para una potencia mecánica dada.
        """
        if self.efficiency == 0:
            return float('inf')
        return mechanical_power_needed / self.efficiency

    def consumption_kwh(self, mechanical_power_needed, hours):
        """
        Calcula el consumo eléctrico en kWh para una demanda mecánica dada y tiempo.
        """
        p_elec = self.input_power(mechanical_power_needed)
        return (p_elec * hours) / 1000
