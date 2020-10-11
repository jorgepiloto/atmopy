""" U.S. Standard Atmosphere 1976 numerical Constants

The following scripts contains main COESA76 variable definition directly taken
from official paper. Both numerical and theoretical background are provided
together with corresponding references.

"""

import numpy as np

# ----------- A. Category I Constants as listed in Table 2 -------------------

k = 1.380622e-23
""" The Boltzmann constant given in [N * m / K] is theoretically equal to the
ratio :math:`R^{*} / N_{a}`, and has a value, consistent with the carbon-12
scale, as cited by Mechtly (1973).
"""

M_N2 = 28.0134
""" Diatomic nitrogen molecular weight based upon the carbon-12 isotope scale
for which C12 = 12. This scale was adopted in 1961 at the Montreal meeting of
the International Union of Pure and Applied Chemistry. It is measured in [kg /
kmol].
"""

M_O2 = 31.9988
""" Diatomic oxygen molecular weight based upon the carbon-12 isotope scale
for which C12 = 12. This scale was adopted in 1961 at the Montreal meeting of
the International Union of Pure and Applied Chemistry. It is measured in [kg /
kmol].
"""

M_Ar = 39.948
""" Argon molecular weight based upon the carbon-12 isotope scale for which C12
= 12. This scale was adopted in 1961 at the Montreal meeting of the
International Union of Pure and Applied Chemistry. It is measured in [kg /
kmol].
"""

M_CO2 = 44.00995
""" Carbon dioxide molecular weight based upon the carbon-12 isotope scale for
which C12 = 12. This scale was adopted in 1961 at the Montreal meeting of the
International Union of Pure and Applied Chemistry. It is measured in [kg /
kmol].
"""

M_Ne = 20.183
""" Neon molecular weight based upon the carbon-12 isotope scale for which C12 =
12. This scale was adopted in 1961 at the Montreal meeting of the International
Union of Pure and Applied Chemistry. It is measured in [kg / kmol].
"""

M_He = 4.0026
""" Helium molecular weight based upon the carbon-12 isotope scale for which C12 =
12. This scale was adopted in 1961 at the Montreal meeting of the International
Union of Pure and Applied Chemistry. It is measured in [kg / kmol].
"""

M_Kr = 83.80
""" Krypton molecular weight based upon the carbon-12 isotope scale for which C12 =
12. This scale was adopted in 1961 at the Montreal meeting of the International
Union of Pure and Applied Chemistry. It is measured in [kg / kmol].
"""

M_Xe = 131.30
""" Xenon molecular weight based upon the carbon-12 isotope scale for which C12
= 12. This scale was adopted in 1961 at the Montreal meeting of the
International Union of Pure and Applied Chemistry. It is measured in [kg /
kmol].
"""

M_CH4 = 16.04303
""" Methane molecular weight based upon the carbon-12 isotope scale for which
C12 = 12. This scale was adopted in 1961 at the Montreal meeting of the
International Union of Pure and Applied Chemistry. It is measured in [kg /
kmol].
"""

M_H2 = 2.01594
""" Diatomic hidrogen  molecular weight based upon the carbon-12 isotope scale
for which C12 = 12. This scale was adopted in 1961 at the Montreal meeting of
the International Union of Pure and Applied Chemistry. It is measured in [kg /
kmol].
"""

M_i = np.array([M_N2, M_O2, M_Ar, M_CO2, M_Ne, M_He, M_Kr, M_Xe, M_CH4, M_H2])
""" Arrays of molecular weights """

N_A = 6.022169e26
""" The Avogadro's constant, measured in [1 / kmol], is consistent with the
carbon-12 scale and is the value cited in Mechtly (1973).
"""

R_star = 8.31432e3
""" The gas constant, in [N * m / kmol / K], is consistent with the carbon-12
scale, and is the value used in the 1962 Standard. This value is not exactly
consistent wiuth the cited values of k and N_A.
"""

# ----------- B. Category II Constants as listed in Table 2 ------------------

F_N2 = 0.78084
""" Value of the fractional-volume concentration of diatomic nitrogen listed in
table 3, is assumed to represent the relative concentrations of the several gas
species comprising dry air at sea level. These values are identical to those
given in the 1962 Standard (COESA 1962), and except for minor modifications
which are based upon CO2 measurements by Keeling (1960), these values are the
same as those given by Glueckauf (1951), an are based upon the earlier work of
Paneth (1939). Dimensionless constant.
"""

F_O2 = 0.209476
""" Value of the fractional-volume concentration of diatomic oxygen listed in
table 3, is assumed to represent the relative concentrations of the several gas
species comprising dry air at sea level. These values are identical to those
given in the 1962 Standard (COESA 1962), and except for minor modifications
which are based upon CO2 measurements by Keeling (1960), these values are the
same as those given by Glueckauf (1951), an are based upon the earlier work of
Paneth (1939). Dimensionless constant.
"""

F_Ar = 0.00934
""" Value of the fractional-volume concentration of argon listed in table 3, is
assumed to represent the relative concentrations of the several gas species
comprising dry air at sea level. These values are identical to those given in
the 1962 Standard (COESA 1962), and except for minor modifications which are
based upon CO2 measurements by Keeling (1960), these values are the same as
those given by Glueckauf (1951), an are based upon the earlier work of Paneth
(1939). Dimensionless constant.
"""

F_CO2 = 0.000314
""" Value of the fractional-volume concentration of carbon dioxide listed in
table 3, is assumed to represent the relative concentrations of the several gas
species comprising dry air at sea level. These values are identical to those
given in the 1962 Standard (COESA 1962), and except for minor modifications
which are based upon CO2 measurements by Keeling (1960), these values are the
same as those given by Glueckauf (1951), an are based upon the earlier work of
Paneth (1939). Dimensionless constant.  
"""

F_Ne = 0.00001818
""" Value of the fractional-volume concentration of neon listed in table 3, is
assumed to represent the relative concentrations of the several gas species
comprising dry air at sea level. These values are identical to those given in
the 1962 Standard (COESA 1962), and except for minor modifications which are
based upon CO2 measurements by Keeling (1960), these values are the same as
those given by Glueckauf (1951), an are based upon the earlier work of Paneth
(1939). Dimensionless constant.
"""

F_He = 0.00000524
""" Value of the fractional-volume concentration of helium listed in table 3, is
assumed to represent the relative concentrations of the several gas species
comprising dry air at sea level. These values are identical to those given in
the 1962 Standard (COESA 1962), and except for minor modifications which are
based upon CO2 measurements by Keeling (1960), these values are the same as
those given by Glueckauf (1951), an are based upon the earlier work of Paneth
(1939). Dimensionless constant.
"""

F_Kr = 0.00000114
""" Value of the fractional-volume concentration of krypton listed in table 3,
is assumed to represent the relative concentrations of the several gas species
comprising dry air at sea level. These values are identical to those given in
the 1962 Standard (COESA 1962), and except for minor modifications which are
based upon CO2 measurements by Keeling (1960), these values are the same as
those given by Glueckauf (1951), an are based upon the earlier work of Paneth
(1939). Dimensionless constant.
"""

F_Xe = 0.000000087
""" Value of the fractional-volume concentration of xenon listed in table 3, is
assumed to represent the relative concentrations of the several gas species
comprising dry air at sea level. These values are identical to those given in
the 1962 Standard (COESA 1962), and except for minor modifications which are
based upon CO2 measurements by Keeling (1960), these values are the same as
those given by Glueckauf (1951), an are based upon the earlier work of Paneth
(1939). Dimensionless constant.
"""

F_CH4 = 0.000002
""" Value of the fractional-volume concentration of methane listed in table 3,
is assumed to represent the relative concentrations of the several gas species
comprising dry air at sea level. These values are identical to those given in
the 1962 Standard (COESA 1962), and except for minor modifications which are
based upon CO2 measurements by Keeling (1960), these values are the same as
those given by Glueckauf (1951), an are based upon the earlier work of Paneth
(1939). Dimensionless constant.
"""

F_H2 = 0.0000005
""" Value of the fractional-volume concentration of diatomic hydrogen listed in
table 3, is assumed to represent the relative concentrations of the several gas
species comprising dry air at sea level. These values are identical to those
given in the 1962 Standard (COESA 1962), and except for minor modifications
which are based upon CO2 measurements by Keeling (1960), these values are the
same as those given by Glueckauf (1951), an are based upon the earlier work of
Paneth (1939). Dimensionless constant.  """

F_i = np.array([F_N2, F_O2, F_Ar, F_CO2, F_Ne, F_He, F_Kr, F_Xe, F_CH4, F_H2])
""" Array of fractional volumes """

g_0 = 9.80665
""" The quantity represents the mean-sea level value of the acceleration adopted
for this Standard. This value is the one originally adopted by the International
Committee on Weights and Measures in 1901 for 45º latitude, and even though it
has since been shown to be too high by about five parts in ten thousand (List
1968), this value has persisted in meteorology and in some standard atmospheres
as the value associated with 45º latitude, even though it applies more
precisely to a latitude of 45º 32' 33''. Units are given in [m / s2].
"""

g_0prime = 9.80665
""" This dimensional constant selected to relate the geopotential meter to
geometric height is numerically equal to :math:`g_{0}`, but with appropriate
different dimensions. This constant implicitly defines one standard geopotential
meter as the vertical increment through which one must lift one kilogram to
increase its potential energy by 9.80665 joules. The geometric length of this
vertical increment varies inversely with the height-dependent value of
:math:`g`. Units are in [m2 / s].
"""

Gamma = 1.00
""" This non-dimensional constant relates the geometric and geopotential gravity
acceleration values """

b_levels = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
""" Subscript representing different atmospheric layers in which different
temperature gradients occur.
"""

H_b = np.array([0, 11000, 20000, 32000, 47000, 51000, 71000, 84.8520e3])
""" Each of the members of the set of geopotential-height values in
:math:`H_{b}` listed in table 4 represents the base of one of eight successive
atmospheric layers. The pairs of values oh :math:`H_{b}` and :math:`L_{Mb}` are
based partly on tradition and partly on present-day observations. The first five
of these pairs are identically to those of the first five layers in the 1962
Standard while the remaining two values of both :math:`H_{b}` and
:math:`L_{Mb}`, have been selected to provide a reasonable fit to the presently
available atmospheric data. The first two values of the related sets have their
own origin in one of the earliest aeronautical standard atmospheres (Toussaint
1919), and were approximated by the first U.S. Standard Atmosphere (Diehl 1925).
"""

L_Mb = np.array([-6.5, 0.0, 1.0, 2.8, 0.0, -2.8, -2.0, -2.0]) * 1e-3
""" Each member of the set of seven gradients :math:`L_{Mb} = dT_{M}/dH` [i.e.,
of molecular scale temperature :math:`T_{M}` (Minzner and Ripley 1965) with
respect to geopotential :math:`H`] listed in table 4 represents the fixed value
appropriate throughout its related layer, :math:`H_{b}` to :math:`H_{b+1}`.
"""

P_0 = 1.013250e5
""" The standard sea-level atmospheric pressure who's units are in [Pa] was
adopted in 1974 in Resolution 164 of the International Meteorologival
Organization, and corresponds to the pressure exerted by a column of mercury
0.760 [m] high, having a density of 1.35951e4 [kg / m3] and subject to an
acceleration due to gravity of 9.80665 [m / s2]. This equivalency definition was
adopted by the International Commission on Weights and Measures in 1948.
"""

r_0 = 6356766
""" The effective Earth's radius for purposes of calculating geopotential at any
latitude is readily obtained from equatoins given by Harrison (1968). The value
is given in [m] and corresponds to the latitude for which :math:`g = g_{0}`.
"""

T_0 = 288.15
""" The standard sea-level temperature in [K]. This value is based upon two
International agreements. The first of these is Resolution 192 of the
International Commission for Air Navigation which in 1924 adopted 15ºC as the
sea-level temperature of The International Standard Atmosphere. This value has
been retained unchanged in all known standard atmospheres since that date. The
second agreement is that of the 1954 Tenth General Conference on Weights and
Measures which set the fixed point of the Kelvin temperature scale at the
triple-point temperature 273.16 [K], which is 0.01 [K] above the ice-point
temperature at standard sea-level pressure.
"""

S = 110
""" The Sutherland constant in [K] from (Hilsenrath et al. 1955) is a constant
in the empirical expression for dynamic viscosity.
"""

beta = 1.458e6
"""
This quantity in [kg / s / m / K0.5], (Hilsenrath et al. 1955) is a constant in
the empirical expression for dynamic viscosity.
"""

gamma = 1.400
""" The ratio of specific heat of air at constant pressure to the specific heat
of air at constant volume is a dimensionless quantity. This is the value adopted
by the Aerological Commission of the International Meteorological Organization,
in Toronto in 1948.
"""

sigma = 3.65e-10
""" The mean effective collusion diameter of molecules in [m] is a quantity
which varies with gas species and temperature. The adopted value is assumed to
apply in a dry, sea-level atmosphere. Above 85 [km] the validity  of the adopted
value decreases with increasing altitude (Hirschfelder et al. 1965; Chepman and
Cowling 1960) due to the change in atmospheric composition. For this reason the
number of significan figures in tabulations of quatities involving it is reduced
from that used for other tabulated quantities at heights above 86 [km].
"""

# ---------- C. Category III Constants as listed in Table 2 ------------------

a_N2 = None
""" The quantity measured in [1 / m / s] represents a coefficient used in a
particular function for designating the height-dependent molecular-diffusion
coefficient D_i for the related gas species, in this case diatomic nitrogen. """

a_O = 6.986e20
""" The quantity measured in [1 / m / s] represents a coefficient used in a
particular function for designating the height-dependent molecular-diffusion
coefficient D_i for the related gas species, in this case oxygen. """

a_O2 = 4.863e20
""" The quantity measured in [1 / m / s] represents a coefficient used in a
particular function for designating the height-dependent molecular-diffusion
coefficient D_i for the related gas species, in this case diatomic oxygen. """

a_Ar = 4.487e20
""" The quantity measured in [1 / m / s] represents a coefficient used in a
particular function for designating the height-dependent molecular-diffusion
coefficient D_i for the related gas species, in this case argon. """

a_He = 1.700e21
""" The quantity measured in [1 / m / s] represents a coefficient used in a
particular function for designating the height-dependent molecular-diffusion
coefficient D_i for the related gas species, in this case helium. """

a_H = 3.305e21
""" The quantity measured in [1 / m / s] represents a coefficient used in a
particular function for designating the height-dependent molecular-diffusion
coefficient D_i for the related gas species, in this case hydrogen. """

b_N2 = None
""" This dimensionless quantity is used as an exponent along with the
corresponding values of a_i in eq (8) ofr designating the height-dependent ,
molecular-diffusion coefficient for the related gas species. The particular
values of a_i and b_i adopted for this Standard have been selected to yield a
height variation of D_i assumed to be realistic. This value is associated to
nitrogen. """

b_O = 0.750
""" This dimensionless quantity is used as an exponent along with the
corresponding values of a_i in eq (8) ofr designating the height-dependent ,
molecular-diffusion coefficient for the related gas species. The particular
values of a_i and b_i adopted for this Standard have been selected to yield a
height variation of D_i assumed to be realistic. This value is associated to
oxygen. """

b_O2 = 0.750
""" This dimensionless quantity is used as an exponent along with the
corresponding values of a_i in eq (8) ofr designating the height-dependent ,
molecular-diffusion coefficient for the related gas species. The particular
values of a_i and b_i adopted for this Standard have been selected to yield a
height variation of D_i assumed to be realistic. This value is associated to
diatomic oxygen. """

b_Ar = 0.870
""" This dimensionless quantity is used as an exponent along with the
corresponding values of a_i in eq (8) ofr designating the height-dependent ,
molecular-diffusion coefficient for the related gas species. The particular
values of a_i and b_i adopted for this Standard have been selected to yield a
height variation of D_i assumed to be realistic. This value is associated to
argon. """

b_He = 0.691
""" This dimensionless quantity is used as an exponent along with the
corresponding values of a_i in eq (8) ofr designating the height-dependent ,
molecular-diffusion coefficient for the related gas species. The particular
values of a_i and b_i adopted for this Standard have been selected to yield a
height variation of D_i assumed to be realistic. This value is associated to
helium. """

b_H = 0.500
""" This dimensionless quantity is used as an exponent along with the
corresponding values of a_i in eq (8) ofr designating the height-dependent ,
molecular-diffusion coefficient for the related gas species. The particular
values of a_i and b_i adopted for this Standard have been selected to yield a
height variation of D_i assumed to be realistic. This value is associated to
hydrogen. """

K_7 = 1.2e2
""" This quantity measured in [m2 / s] is the adopted value of the
eddy-diffusion coefficient K, at Z_7 and in the height interval from 86 up to 91
[km]. Beginning at 91 [km] and extending up to 115 [km], the value of K is
defined by eq (7b). At 115 [km] the value of [K] equals K_10. """

K_10 = 0.0
""" This quantity measured in [m2 / s] is the adopted value of the
eddy-diffusion coefficient K at Z_10 = 120 [km] and throughout the height
interval from 115 [km] to 1000 [km]. """

L_Kb = np.array([0.0, np.nan, 12.0, np.nan, np.nan, np.nan]) * 1e-3
""" A set of values representing the gradients dT/dZ listed in table 5 was
specifically selected for this Standard to represent available observations.
Each of these two values of L_Kb is associated with the entire extent of a
corresponding layer whose base is Z_b and whose top is Z_b+1. """

n0_7 = 8.6e16
""" This quantity measured in [1 / m3] is the number density of atomic oxygen
assymed for this Standard to exist at Z_7 = 86 [km]. This value of atomic oxygen
number density, along with other defined constants, leads to number densities of
N_2, O_2, Ar, and He at 86 [km]. (See Appendix A.) """

nH_11 = 8.0e10
""" This quantity measured in [1 / m3] is the assumed number density of atomic
hydrogen at height Z_11 = 500 [km], and is used as the reference value in
computing the height profile of atomic hydrogen between 150 and 1000 [km]. """

q_O = -3.416248e-12
""" The quantity measured in [1 / m3] represents the first set of six
species-dependent sets of coefficients or terms (i.e., sets of q_i, Q_i, u_i,
U_i, w_i and W_i), the corresponding members of all six of which are
simultaneously used in an empirical expression [eq (7)] for the vertical
transport term v_i / (D_i + K) in the vertical flux equation for the particular
gas species. The species-dependent values of all six sets have been selected for
this Standard to adjust number-density profiles of the related gas species to
particular boundary conditions at 150 and 450 [km], as well as at 97 [km] in hte
case of atomic oxygen. These boundary conditions all represent observed or
assumed average conditions. This one is related with atomic oxygen. """

q_O2 = 0
""" The quantity measured in [1 / m3] represents the first set of six
species-dependent sets of coefficients or terms (i.e., sets of q_i, Q_i, u_i,
U_i, w_i and W_i), the corresponding members of all six of which are
simultaneously used in an empirical expression [eq (7)] for the vertical
transport term v_i / (D_i + K) in the vertical flux equation for the particular
gas species. The species-dependent values of all six sets have been selected for
this Standard to adjust number-density profiles of the related gas species to
particular boundary conditions at 150 and 450 [km], as well as at 97 [km] in hte
case of atomic oxygen. These boundary conditions all represent observed or
assumed average conditions. This one is related with atomic diatomic oxygen. """

q_Ar = 0
""" The quantity measured in [1 / m3] represents the first set of six
species-dependent sets of coefficients or terms (i.e., sets of q_i, Q_i, u_i,
U_i, w_i and W_i), the corresponding members of all six of which are
simultaneously used in an empirical expression [eq (7)] for the vertical
transport term v_i / (D_i + K) in the vertical flux equation for the particular
gas species. The species-dependent values of all six sets have been selected for
this Standard to adjust number-density profiles of the related gas species to
particular boundary conditions at 150 and 450 [km], as well as at 97 [km] in hte
case of atomic oxygen. These boundary conditions all represent observed or
assumed average conditions. This one is related with argon. """

q_He = 0
""" The quantity measured in [1 / m3] represents the first set of six
species-dependent sets of coefficients or terms (i.e., sets of q_i, Q_i, u_i,
U_i, w_i and W_i), the corresponding members of all six of which are
simultaneously used in an empirical expression [eq (7)] for the vertical
transport term v_i / (D_i + K) in the vertical flux equation for the particular
gas species. The species-dependent values of all six sets have been selected for
this Standard to adjust number-density profiles of the related gas species to
particular boundary conditions at 150 and 450 [km], as well as at 97 [km] in hte
case of atomic oxygen. These boundary conditions all represent observed or
assumed average conditions. This one is related with helium. """

Q_O = -5.809644e-13
""" The quantity measured in [1 / m3] represents the second of the six set of
constants described along with q_i above. This one is related with atomic
oxygen. """

Q_O2 = 1.366212e-13
""" The quantity measured in [1 / m3] represents the second of the six set of
constants described along with q_i above. This one is related with atomic
diatomic oxygen. """

Q_Ar = 9.434079e-14
""" The quantity measured in [1 / m3] represents the second of the six set of
constants described along with q_i above. This one is related with atomic
argon. """

Q_He = -2.457369e-13
""" The quantity measured in [1 / m3] represents the second of the six set of
constants described along with q_i above. This one is related with atomic
helium. """

T_9 = 240.0
""" The quantity measured in [K] represents the kinetic temperature at Z_9 = 110
[km]. This temperature has been adopted along with the gradient L_K9 = 12 [K /
km] to generate a linear segment of T(Z) represents a mean of observed
temperature-height data for the corresponding height region. """

T_inf = 1000
""" The quantity measured in [K] represents the exospheric temperature, i.e. the
asymptote which the exponential function representing T(Z) above 120 [km]
closely approaches at heights above about 500 [km], where the mean free path
exceeds the scale height. The value of T_inf adopted for this Standard is
assumed to represent mean solar conditions. """

u_H = 97e3
""" The quantity measured in [m] represents the third set of the six sets of
constants described along with q_i above. This one is related with atomic
oxygen. """

u_O2 = np.nan
""" The quantity measured in [m] represents the third set of the six sets of
constants described along with q_i above. This one is related with atomic
diatomic oxygen. """

u_Ar = np.nan
""" The quantity measured in [m] represents the third set of the six sets of
constants described along with q_i above. This one is related with argon. """

u_He = np.nan
""" The quantity measured in [m] represents the third set of the six sets of
constants described along with q_i above. This one is related with helium. """

U_O = 56.90311e3
""" The quantity measured in [m] represents the fourth set of the six sets of
constants described along with q_i above. This one is related with atomic
oxygen. """

U_O2 = 86.000e3
""" The quantity measured in [m] represents the fourth set of the six sets of
constants described along with q_i above. This one is related with diatomic
oxygen. """

U_Ar = 86.000e3
""" The quantity measured in [m] represents the fourth set of the six sets of
constants described along with q_i above. This one is related with argon. """

U_He = 86.000e3
""" The quantity measured in [m] represents the fourth set of the six sets of
constants described along with q_i above. This one is related with helium. """

w_O = 5.008765e-13
""" The quantity measured in [m] represents the fifth set of the six sets of
constants described along with q_i above. This one is related with atomic
oxygen. """

w_O2 = np.nan
""" The quantity measured in [m] represents the fifth set of the six sets of
constants described along with q_i above. This one is related with diatomic
oxygen. """

w_Ar = np.nan
""" The quantity measured in [m] represents the fifth set of the six sets of
constants described along with q_i above. This one is related with argon. """

w_He = np.nan
""" The quantity measured in [m] represents the fifth set of the six sets of
constants described along with q_i above. This one is related with helium. """

W_O = 2.706240e-14
""" The quantity measured in [m] represents the sixth set of the six sets of
constants described along with q_i above. This one is related with atomic
oxygen. """

W_O2 = 8.333333e-14
""" The quantity measured in [m] represents the sixth set of the six sets of
constants described along with q_i above. This one is related with diatomic
oxygen. """

W_Ar = 8.333333e-14
""" The quantity measured in [m] represents the sixth set of the six sets of
constants described along with q_i above. This one is related with argon. """

W_He = 6.666667e-13
""" The quantity measured in [m] represents the sixth set of the six sets of
constants described along with q_i above. This one is related with helium. """

Z_b = np.array([86, 91, 110, 120, 500, 1000]) * 1e3
""" The quantity Z_b represents a set of six values of Z for b equal to 7
through 12. The values Z_7, Z_8, Z_9, z_10 correspond successively to the base
of successive layers characterized by successive segments of the adopted
temperature height-function for this Standard. The fifth value, Z_11, is the
reference height for the atomic hydrogen calculation, while the sixth value,
Z_12, represents the top of the region for which the tabular values of the
Standard are given. These six values if Z_b, along with the designation of the
type of temperature-height function associated with the first four of these
values, plus the related value of L_Kb, for the two segments having a linear
temperature-height function, are listed in table 5. """

alpha_N2 = 0.00
""" This non-dimensional quantity represents a set of six adopted
species-dependent, thermal diffusion coefficients listed in Table 6. This one is
related with diatomic nitrogen. """

alpha_O = 0.00
""" This non-dimensional quantity represents a set of six adopted
species-dependent, thermal diffusion coefficients listed in Table 6. This one is
related with atomic oxygen. """

alpha_O2 = 0.00
""" This non-dimensional quantity represents a set of six adopted
species-dependent, thermal diffusion coefficients listed in Table 6. This one is
related with diatomic oxygen. """

alpha_Ar = 0.00
""" This non-dimensional quantity represents a set of six adopted
species-dependent, thermal diffusion coefficients listed in Table 6. This one is
related with argon. """

alpha_He = -0.40
""" This non-dimensional quantity represents a set of six adopted
species-dependent, thermal diffusion coefficients listed in Table 6. This one is
related with helium. """

alpha_H = -0.25
""" This non-dimensional quantity represents a set of six adopted
species-dependent, thermal diffusion coefficients listed in Table 6. This one is
related with hydrogen. """

phi = 7.2e11
""" The quantity measured in [1 / m2 / s] for the vertical flux is chosen as a
compromise between the classical Jeans escape flux for T_inf = 1000 [K], with
corrections to take into account deviations from a Maxwellian velocity
distribution at the critical level (Brinkman 1971), and the effects of charge
exchange with H+ and O+ in the plasmasphere (Tinley 1973). """

# ---------------- Derived constants and computed values ---------------------
T_Mb = np.array([288.15, 216.650, 216.650, 228.650, 270.65, 270.65, 214.650, 186.87])
""" Molecular temperature at the base of each layer. Values are given in [K]. """

T_b = np.array([186.87, 186.87, 240.00, 360.00, 999.24, 1000.00])
""" Kinetic temperature at the base of each layer. Values are given in [K]. """

P_b = np.array(
    [
        101325,
        22632.1,
        5474.89,
        868.019,
        110.906,
        66.9389,
        3.95642,
        0.37338,
    ]
)
""" Barometric pressure at the base of each layer. Values are given in [Pa]. """

M_M0_H_table_under_86km = np.array(
    [
        np.append(np.linspace(79000, 84500, 12), H_b[-1]),
        [
            1.000000,
            0.999996,
            0.999988,
            0.999969,
            0.999938,
            0.999904,
            0.999864,
            0.999822,
            0.999778,
            0.999731,
            0.999681,
            #0.999679,
            0.999624,
            0.999579,
        ],
    ]
)
""" Molecular-weight ratio as function of geopotential height in meters. This
values are hosted in table (8) from official report. """

M_M0_Z_table_under_86km = np.array(
    [
        np.linspace(80000, 86000, 13),
        [
            1.0000000,
            0.9999960,
            0.9999890,
            0.999971,
            0.9999410,
            0.9999090,
            0.9998700,
            0.999829,
            0.9997860,
            0.9997410,
            0.9996940,
            0.9996410,
            0.999579,
        ],
    ]
)
""" Molecular-weight ratio as function of geometric height in meters. This
values are hosted in table (8) from official report. """

M_0 = sum(M_i * F_i) / sum(F_i)
""" Mean molecular weight of air computed from official report table (3) by
making use of molecular weights and fractional volumes. This quantity is given
in [kg / kmol]. """
