Scope and Outcomes
==================

Introduction
------------
Illustris is a large cosmological simulation suite that has simulated the
history of a "universe in a box" over a time frame of 13 Gyr. The primary
building block of the simulations is the "dark-matter particle", which has an
initial mass of 6 million solar masses (6x10^6 Msun) and an initial gas mass
of 1.3x10^6 Msun (http://www.illustris-project.org/data/ ). Each particle also
contains various sub-grid parameters, such as stellar mass, star formation rate,
number of black holes, etc.

.. todo:: Continue this explanation

As time progresses in the the simulation, particles group together, and galaxies
form in the dense centres of these groups (the so-called Sub-halos. Halos are
the larger overarching groups that surround galaxy clusters). The snapshots of
this universe-in-a-box allow us to view the evolution history of a certain
galaxy all the way back to its beginning.

Simulations are one thing, reality is often different. Hence out main goal of
this project is to determine whether the predictions made through this
cosmological simulation will actually be testable in real life - i.e. will the
next generation of telescopes be able to observe the phenomena seen in the
simulations.

The current generation of telescopes, through simple physics, will never be able
to resolve galaxies at distances larger than z>3, simply because the galaxies
are two small (D<1 kpc), the diffraction limit of an 8m class telescope (VLT)
is around 0.05" in K-band (lam/D), and the cosmological angular size scale is
~8kpc/" (0.125"/kpc) at 1<z<3 (http://www.astro.ucla.edu/~wright/CosmoCalc.html ).
Even the JWST, with its 6.5m mirror, will struggle to get any spatial
information from high-z galaxies.

The ELT however, with a 40m mirror and a corresponding diffraction limit of
0.007" in J (0.012" in K), will have a spatial resolution of ~60pc (100pc) in
J (K), and will thus be able to provide information on the spatial variations
of star formation in the very first galaxies. Unfortunately the ELT is a
ground-based telescope, and consequently suffers from a sensitivity limit due
to atmospheric extinction.

The main goals of this project revolve around the central theme::

    What will actually be bright enough for the ELT to observe?

Scope and Method
----------------
* We will concentrate on using 3D particle data form the illustris API
* We will generate realistic 2D on-sky projections of the particle data
  using the hyperion radiative transfer code
* We will create simulated observations of particle data using the SimCADO
  instrument data simulation software
* We will determine what star formation rates will be visible for a redshift
  and volume density








