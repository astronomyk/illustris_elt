import numpy as np
import matplotlib.pyplot as plt

from . import reorient_galaxies as rg


def test_make_a_galaxy_dataset_and_reorient_it_with_plots():
    # make the data set
    x, y, z = rg.make_data_set(dx=1, dy=0.3, dz=0.1,
                               ang_xy=np.random.rand()*360,
                               ang_xz=np.random.rand()*360,
                               ang_yz=np.random.rand()*360,
                               n=10000)
    rg.plot_data_set(x, y, z)
    plt.show()

    # find the principle axis and reorient it
    x1, y1, z1 = rg.reorient_coords(x, y, z)
    rg.plot_data_set(x1, y1, z1)
    plt.show()

