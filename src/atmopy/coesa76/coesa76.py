""" U.S. Standard Atmosphere 1976 numerical Constants

The following scripts contains main COESA76 routines for solving different
thermodynamic variables as function of height.

"""

import numpy as np
from atmopy.coesa76 import constants as c
from atmopy.coesa76.utils import T_at_H_under_86km, T_at_Z_above_86km, H_at_Z, Z_at_H


def T_at_Z(Z):
    """ Solves kinetic temperature at given geometrical altitude """

    # Filter if below or above 86 [km]
    if Z > 86000:
        T = T_at_Z_above_86km(Z)
    else:
        T = T_at_H_under_86km(H_at_Z(Z))

    return T

