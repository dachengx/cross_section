import numpy as np
from xsectron.neutrino import NeutrinoElectron


def test_placeholder():
    E = np.linspace(1, 40, 31)
    NeutrinoElectron.sigma(E * 1e-3)
