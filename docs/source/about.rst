About atmopy library
====================

Why atmospheric modelling
-------------------------

Air drag plays a big role when it comes to aircraft performance or spacecraft
orbital decay. Since this force is proportional to air density, several models
have tried all along history to model the Earth's atmosphere to achieve high
accurate results. They might consider the air to be static, different solar
conditions such us day and night and many other variables.

But atmospheric modelling does not only play a big role in our planet. It is
possible to find other celestial bodies in the Solar System such us Venus, who
has a very dense and hot atmosphere, or Jupiter moons. Those models, although
more difficult to generate because of lack of data compared to Earth one, are
important when it comes to spacecraft landing or any other maneuver in which
drag is not negligible.


Old models: software archaeology
--------------------------------

It is quite difficult to understand latest atmospheric mathematical models
without having a look at all previous developed models. You should be aware that
atmospheric modelling started together with the development of the first
rockets and missiles. Data registers from sensors located in those machines,
enable to generate different mathematical approaches.

Therefore, the reasons behind old models implemented within **atmopy** are not
because they are useful, but for historical reasons. One of the objectives is
also to create some kind of software atmospheric library, not only hosting
source code but also original papers.

Finally, having a collection of models implemented in Python improves
readability a lot. Some of them were initially implemented in Fortran or C/C++,
programming languages which can be a little bit confusing for amateur users.
