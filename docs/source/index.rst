.. illustris_elt documentation master file, created by
   sphinx-quickstart on Wed Nov  7 09:31:29 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

illustris_elt's documentation
=============================

The main goal of this project is to connect the Illustris cosmological
simulation database to the ELT/MICADO instrument simulator, in order to
determine the observational limits of the ELT/MICADO system with respect to
star formation before cosmic noon (z>2).

The ELT will have sensitivity similar to the next generation of space-based
telescopes, but with a resolution 50x better. This will enable the study of the
spatial characteristics of the earliest galaxies on scales of ~100pc. This in
turn will enable the scale and spatial extent of the star formation regions to
be understood, and should shed light on just how the first stars and galaxies
formed in the universe.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   background/1_project_scope_goals
   background/2_background
   background/3_package_architecture
   roadmap/roadmap
   code_design/ideas
   background/A_literature
   background/B_science_as_software_methodology


Goals of this study
-------------------
Target z>2, goal z>5

* Determine surface brightness observation limits for individual star forming
  regions in z>2 galaxies in all the major NIR filters
   * Calculate what star formation rate this translates to

* Determine whether the star formation mechanism (triggered vs jeans collapse)
  will be observable in z>2 galaxies by observing

* See whether this technique of "science as software" is a viable methodology
  for scientific research

