import numpy as np

from .constants import m_Z, sin2_theta_w, g


class NeutrinoElectron:
    def __init__(self, energy: float, angle: float) -> None:
        self.energy = energy
        self.angle = angle

    @staticmethod
    def sigma(E):
        c_V = -0.5 + 2 * sin2_theta_w
        c_A = -0.5
        return (
            1
            / (24 * np.pi)
            * (g / m_Z) ** 4
            * E**2
            * (c_V**2 + c_A**2 + c_V * c_A)
            * (0.1973**2)
            / (1e-2 / 1e-15) ** 2
        )
