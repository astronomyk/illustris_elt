Roadmap for the Project
=======================

Get initial galaxy data
-----------------------
1. Choose 2 galaxies to follow their history
    * massive elliptical
    * beautiful spiral
2. Find their merger history
    * Get sub_halo_id number for each galaxy for each of the 135 snapshots
    * Assume that the merger history continues along the line of largest merger
      participant
3. Decide what data will be interesting
    * Star formation rate
    * Filter magnitudes
    * Particle positions
        * Particle sizes too (if available)
    * Mass of particle
        * Total mass
        * Dark matter mass
        * Gas mass
        * Star mass
4. Decide which particles in the sub-halo "belong" to the galaxy at the centre of the sub-halo
    * Do we decide on a star-mass density limit? Or combined star+gas mass density limit
    * Do we use a luminosity (density) limit?


Pull data from illustris database
---------------------------------
1. Write function to get the above mentioned data for a galaxy at a particular snapshot
2. Save the data somewhere in a coherent naming scheme
3. Decide, based on query/download speed whether to download data again every
    time the scripts are run, or whether to save the data in cache and load from
    disk (i.e. ``astropy.download_file(url=..., cache=True)``)


Make "ideal" mock 2D maps/images of galaxy
------------------------------------------
"Ideal" maps/images mean what the galaxy would look like before a telescope was
used to observe it. This could mean we display the stellar mass of the galaxy in
an image, or actually use the intensity of a galaxy in a given filter band
(UVIKgriz). We also want to be able to view the galaxy from any angle

1. Function to display an integrated 2D "column-density"-style map of the galaxy for any set of rotation angles
2. Function to automaticaly determine the semi-major and -minor axes of the sub-halo ellipsoid
3. Function to rotate particle positions to the following orientations:
    * Face on - view of largest and 2nd largest axes
    * Edge on - view of largest and smallest axes
    * End on - view of smallest and 2nd smallest axes

    This could be done with a `principle component analysis`_

.. _`principle component analysis`: https://en.wikipedia.org/wiki/Principal_component_analysis

4. Function to make maps of the following of each galaxy for each of the three main orientations:
    * Flux intensity in each of the UVRIgriz filters
    * Star formation rate
    * Stellar mass
    * Gas + stellar mass
    * Dark matter

5. Function to generate these maps on-the-fly and return a fits image at a giving spatial angular resolution, given a snapshot distance (i.e. lookback time)
    * See Ned Wright's `cosmological calculator`_ for angular distances vs redshift

.. _`cosmological calculator`: http://www.astro.ucla.edu/~wright/CosmoCalc.html

6. Combine this funtionality into a python package
    * Write the appropriate tests, and documentation

Time for the fun stuff:

7. Generate these maps for each of the snapshots of a galaxy
    * Create GIFs of the evolution of the galaxy over cosmic time
    * Create these maps for a fixed viewing angle
    * Create these maps oriented along one of the principle axes

8. Plot integrated parameters over the whole galaxies vs cosmic time (snapshot and lookback time)
    * Each of the parameters listed in 4.





