import math

class IdealGas:
    def __init__(self, cp=1005, cv=718, gamma=1.4, R=287):
        self.cp = cp
        self.cv = cv
        self.gamma = gamma
        self.R = R

    def isentropic_exit_temperature(self, T_in, P_in, P_out):
        """Salida de temperatura para compresión/expansión isentrópica."""
        return T_in * (P_out / P_in) ** ((self.gamma - 1) / self.gamma)

    def isentropic_work(self, mass_flow, T_in, T_out):
        """Trabajo requerido en proceso isentrópico."""
        return mass_flow * self.cp * (T_out - T_in)

    def polytropic_work(self, mass_flow, T_in, T_out, n):
        """Trabajo para proceso politrópico."""
        return mass_flow * self.cp * (T_out - T_in) * (self.gamma - 1) / (n - 1)

    def internal_energy(self, mass, T):
        """Energía interna."""
        return mass * self.cv * T

    def enthalpy(self, mass, T):
        """Entalpía."""
        return mass * self.cp * T

    def entropy(self, T1, T2, P1, P2):
        """Variación de entropía para gas ideal."""
        return self.cp * math.log(T2 / T1) - self.R * math.log(P2 / P1)
