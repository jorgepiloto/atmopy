About
-----

Modeling the atmosphere is a complicated task since many variables play a role
on the different thermodynamic conditions: solar-fluxes, latitude and longitude
position, diffusion of the different gasses...

Since the early days of aviation and astronautics, scientists have tried to
develop different models which take into account all the previous parameters in
order to get the most accurate results. In particular, we care about density
since it is directly related to drag force and therefore with orbital decay
among time.

This package is not only a collection of atmospheric routines but also a tribute
to all those people who developed them during the early days of astronautics.


Documentation
-------------

If you want to know how to use this package, please refer to [official
documentation website](https://atmopy.readthedocs.io/en/latest/?badge=latest).
Although more information about package utilities and API reference is provided
in previous page, users will also find different examples and tutorials under
the gallery section.


How to contribute
-----------------

All contributors are welcome! As developer, you will need to clone the
repository in your local machine and install it in "dev" mode, so as soon as you
modify anything on the source code, your changes will show in the behavior of
the package. Please, follow these steps in order to achieve previous objective:

1. Clone this repository.
2. Run `flit install --symlink` so a symbolic link is created to the package.
3. Create a new branch, push changes and open a pull request to merge into
   master.


Coding guides
-------------

Every time you enter a new project, you enter a new world. Each project holds
its own coding rules and all your contributions need to agree with them.
Usually, coding rules are justified because of the nature of the project, as it
happens in this case:

1. All atmosphere models should hold original physical constants and quantities,
   no matter if they are outdated. The idea is to get a model as close to the
   original one.

2. Models should be implemented under the same sub-package making, if necessary,
   a separation between model constants and logical routines. 

Regarding coding line lengths, string definitions, imports order and so on, the
tool tox is provided for developers. By simply running `tox -e reformat` your
code will be properly adapted to the project standards.
