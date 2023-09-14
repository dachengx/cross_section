import numpy as np


def O(n=2):
    return np.zeros((n, n))


def I(n=2):
    return np.eye(n)


def pauli(index):
    if index == 0:
        return I(2)
    elif index == 1:
        return np.array([[0, 1], [1, 0]])
    elif index == 2:
        return np.array([[0, -1j], [1j, 0]])
    elif index == 3:
        return np.array([[1, 0], [0, -1]])
    else:
        raise ValueError("Invalid index: {index} for Pauli matrix")


def gamma(index):
    if index == 0:
        return np.block([[O(), I()], [I(), O()]])
    elif index in [1, 2, 3]:
        return np.block([[O(), pauli(index)], [-pauli(index), O()]])
    elif index == 5:
        return np.block([[-I(), O()], [O(), I()]])
    else:
        raise ValueError("Invalid index: {index} for Gamma matrix")
