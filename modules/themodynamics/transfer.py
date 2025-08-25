import math

def mass_transfer(mass_in, mass_out):
    """Balance simple de masa."""
    return mass_in - mass_out

def energy_transfer(Q_in, Q_out, W_in, W_out):
    """Balance simple de energía."""
    return (Q_in - Q_out) + (W_in - W_out)