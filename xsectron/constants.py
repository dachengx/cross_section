import numpy as np

# import hepunits.units as u
# import hepunits.constants as c

A_Xe = np.asarray([124, 126, 128, 129, 130, 131, 132, 134, 136])
y_Xe = np.asarray([0.0009, 0.0009, 0.0192, 0.264, 0.0408, 0.212, 0.269, 0.104, 0.0887])

m_e = 0.51099895000e-3
m_W = 80.377
m_Z = 91.1876
m_p = 938.27208816e-3
m_n = 939.56542052e-3
G_F = 1.1663787e-5
alpha = 1 / 137.035999084
g = (8 * G_F * (m_W**2) / (2**0.5)) ** 0.5

sin2_theta_w = 0.2312
