Valores sugeridos para configurar un simulador básico de estufa turbomecánica, pensados para un ambiente doméstico típico, junto con explicaciones para cada parámetro.

---

## **Valores sugeridos para el simulador**

| Parámetro                         | Valor sugerido | Explicación                                              |
|------------------------------------|---------------|---------------------------------------------------------|
| TURBINE_DIAMETER                   | 0.25 - 0.35   | Diámetro típico de turbinas domésticas, en metros       |
| TURBINE_LENGTH                     | 0.15 - 0.30   | Largo del rotor, en metros                              |
| TURBINE_RPM                        | 2000 - 3500   | RPM de motores eléctricos domésticos                    |
| AIR_INITIAL_TEMP                   | 10 - 18       | Temperatura inicial del aire, en °C (invierno)          |
| AIR_TARGET_TEMP                    | 22 - 25       | Temperatura objetivo confortable, en °C                 |
| AIR_DENSITY                        | 1.225         | kg/m³ a 20°C, valor estándar                            |
| AIR_SPECIFIC_HEAT                  | 1005          | J/kg·K, valor estándar para aire                        |
| ROOM_VOLUME                        | 20 - 40       | m³, una habitación pequeña a mediana                    |
| STRUCTURE_MASS                     | 1500 - 4000   | kg, depende si es casa de ladrillo, madera, etc.        |
| STRUCTURE_SPECIFIC_HEAT            | 840           | J/kg·K, promedio para ladrillo/hormigón                 |
| HEAT_LOSS_COEFFICIENT              | 50 - 120      | W/K, depende aislamiento, ventanas, etc.                |
| MAX_HEATER_POWER                   | 1500 - 2500   | Watts, potencia eléctrica doméstica disponible          |
| SIMULATION_TIME                    | 1800 - 7200   | Segundos (30 min a 2 horas de simulación)               |

---

### **Ejemplo concreto para una casa pequeña:**

```env
TURBINE_DIAMETER=0.3
TURBINE_LENGTH=0.2
TURBINE_RPM=2800
AIR_INITIAL_TEMP=12
AIR_TARGET_TEMP=23
AIR_DENSITY=1.225
AIR_SPECIFIC_HEAT=1005
ROOM_VOLUME=28
STRUCTURE_MASS=2500
STRUCTURE_SPECIFIC_HEAT=840
HEAT_LOSS_COEFFICIENT=80
MAX_HEATER_POWER=2000
SIMULATION_TIME=3600
```

---
