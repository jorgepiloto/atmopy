""" U.S. Standard Atmosphere 1976 numerical Constants

The following scripts contains main COESA76 utilities and auxiliary routines for
main coesa76.py logical file.

"""

import numpy as np

from atmopy.coesa76 import constants as c


def g_at_Z(Z):
    r"""Gravity acceleration at given geometrical height

    Parameters
    ----------
    Z: float
        Geometric height in meters.

    Returns
    -------
    g: float
        Gravity acceleration at given height in [m  / s2]

    """

    # Apply geometric height conversion
    Z = Z_at_H(H)

    # Recall gravity acceleration expression as function of Z
    g = g_at_Z(Z)
    return g


def g_at_H(H):
    r"""Gravity acceleration at given geometrical height

    Parameters
    ----------
    Z: float
        Geometric height in meters.

    Returns
    -------
    g: float
        Gravity acceleration at given height in [m  / s2]

    Notes
    -----

    This is equation (17) from original report:

    .. math::

      g = g_{0} \left(\frac{r_{0}}{r_{0} + Z} \right)^{2}

    """


def Z_at_H(H):
    r"""Solves for geometric height at given geopotential one

    Parameters
    ----------
    H: float
        Geopotential height in meters.

    Returns
    -------
    Z: float
        Geometric height at previously given geopotential height.

    Notes
    -----
    This is equation (19) from official report:

    .. math::

      Z = \frac{r_{0} \cdot H}{\Gamma \cdot r_{0} - H}

    """

    Z = (c.r_0 * H) / (c.r_0 - H)
    return Z


def H_at_Z(Z):
    r"""Solves for geopotential height at given geometric one

    Parameters
    ----------
    Z: float
        Geometric height in meters.

    Returns
    -------
    H: float
        Geopotential height at previously given geometric height.

    Notes
    -----
    This is equation (18) from original report:

    .. math::

      H = \Gamma \cdot \left( \frac{r_{0} \cdot Z}{r_{0} + Z} \right)

    """

    H = c.Gamma * (c.r_0 * Z) / (c.r_0 + Z)
    return H


def b_at_H(H):
    """Returns base layer index at given geopotential height

    Parameters
    ----------
    H: float
        Geopotential height in meters

    Returns
    -------
    b: int
        Integer value within [0, 12] referred to atmospheric base layer index

    """

    # Generate atmospheric layers in terms of geopotential height
    H_layers = np.concatenate((c.H_b, H_at_Z(c.Z_b[1:])))

    # Get last layer where H >= H_layers
    b = np.where(H_layers <= H)[0][-1]
    return b


def b_at_Z(Z):
    """Returns base layer at given geometric height

    Parameters
    ----------
    Z: float
        Geometric height

    Returns
    -------
    b: int
        Integer value within [0, 12] referred to atmospheric base layer index

    """

    # Generate atmospheric layers in terms of geometric height
    Z_layers = np.concatenate((Z_at_H(c.H_b), c.Z_b[1:]))

    # Get last layer where Z >= Z_layers
    b = np.where(Z_layers <= Z)[0][-1]
    return b


def M_M0_at_H_under_86km(H):
    """Molecular-weight interpolation within transition region

    Parameters
    ----------
    H: float
        Geopotential altitude in meters.

    Returns
    -------
    M_M0: float
        Air mean molecular-weight ratio for transition region

    Notes
    -----
    Interpolation is carried out by making use from values of table (8).

    """

    # Assumes air molecular weight is constant
    if H <= 79000:
        return 1.00

    # Collect table for interpolation
    H_table = c.M_M0_H_table_under_86km[0]
    M_M0_table = c.M_M0_H_table_under_86km[-1]

    # Interpolate and compute molecular weight
    M_M0 = np.interp(H, H_table, M_M0_table)
    return M_M0


def M_M0_at_Z_under_86km(Z):
    """Molecular-weight interpolation within transition region

    Parameters
    ----------
    Z: float
        Geometric  altitude in meters.

    Returns
    -------
    M_M0: float
        Air mean molecular-weight ratio for transition region

    Notes
    -----
    Interpolation is carried out by making use from values of table (8).

    """

    # Assumes air molecular weight is constant
    if Z <= 80000:
        return 1.00

    # Collect table for interpolation
    Z_table = c.M_M0_Z_table_under_86km[0]
    M_M0_table = c.M_M0_Z_table_under_86km[-1]

    # Interpolate and compute molecular weight
    M_M0 = np.interp(Z, Z_table, M_M0_table)
    return M_M0


def T_M_at_H_under_86km(H):
    """Returns molecular temperature at given geopotential height under 86 [km]

    Parameters
    ----------
    H: float
        Geopotential height in [m]

    Returns
    -------
    T_M: float
        Molecular temperature at given geopotential height

    Notes
    -----
    This is equation (23) from official report.

    """

    # Solve for actual base layer index
    b = b_at_H(H)

    # Compute molecular temperature
    T_M = c.T_Mb[b] + c.L_Mb[b] * (H - c.H_b[b])
    return T_M


def T_at_H_under_86km(H):
    """Solves for kinetic temperature at given geopotential height under 86 [km]

    Parameters
    ----------
    H: float
        Geopotential height in [m]

    Returns
    -------
    T: float
        Absolute kinetic temperature in [K]

    Notes
    -----
    This is equation (22) from official report.

    """

    # Solve for molecular temperature at corresponding base
    T_M = T_M_at_H_under_86km(H)
    M_M0 = M_M0_at_Z_under_86km(Z_at_H(H))

    # Compute actual kinetic temperature at given height
    # TODO: FOR TESTING PURPOSES, M_M0 = 1.00
    # M_M0 = 1.00
    T = T_M * M_M0
    return T


def T_at_Z_above_86km(Z):
    """Solves for kinetic temperature at given geometric height above 86 [km].

    Parameters
    ----------
    Z: float
        Gometric height in [m]

    Returns
    -------
    T: float
        Absolute kinetic temperature in [K]

    Notes
    -----
    This is equation (23) from official report.

    """

    # Retrieve layer index
    b = b_at_Z(Z)

    if c.Z_b[0] <= Z < c.Z_b[1] or c.Z_b[2] <= Z < c.Z_b[3]:
        # Geometric altitude within 86-91 [km] or 110-120 [km]
        T = c.T_b[b - 7] + c.L_Kb[b - 7] * (Z - c.Z_b[b - 7])

    elif c.Z_b[1] <= Z <= c.Z_b[2]:
        # This is equation (27) from official report
        T = 263.1905 - 76.3232 * (1 - ((Z - c.Z_b[b - 7]) / -19.9429e3) ** 2) ** 0.5

    else:
        # This is equation (31) from official report
        gamma = c.L_Kb[2] / (c.T_inf - c.T_b[3])
        chi = (Z - c.Z_b[3]) * (c.r_0 + c.Z_b[3]) / (c.r_0 + Z)
        T = c.T_inf - (c.T_inf - c.T_b[3]) * np.exp(-gamma * chi)

    return T


def p_at_H_under_86km(H):
    """Solves for barometric pressure at given geopotential height under 86[kn]

    Parameters
    ----------
    H: float
        Geopotential height in [m]

    Returns
    -------
    P: float
        Barometric pressure under 86[km] height.

    Notes
    -----
    These are equations (33a) and (33b) from official report.

    """

    # Compute necessary values
    b = b_at_H(H)

    # Check if gradient non-zero
    if c.L_Mb[b] != 0.00:
        # Apply non-zero thermal gradient equation
        p = c.P_b[b] * (c.T_Mb[b] / (c.T_Mb[b] + c.L_Mb[b] * (H - c.H_b[b]))) ** (
            c.g_0prime * c.M_0 / c.R_star / c.L_Mb[b]
        )
    else:
        p = c.P_b[b] * np.exp(
            -c.g_0prime * c.M_0 * (H - c.H_b[b]) / c.R_star / c.T_Mb[b]
        )

    return p
