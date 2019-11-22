import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def rotate3d(x, y, z, ang_xy=0, ang_xz=0, ang_yz=0):
    """ Rotate a data set (x,y,z) by an angle in each plane [x-y, x-z, y-z]

    Breaks down 3D rotation into 3x 2D rotations. Angles in [degrees]
    """
    x1, y1 = rotate2d(x, y, ang_xy)     # around the z-axis
    x2, z1 = rotate2d(x1, z, ang_xz)     # around the y-axis
    y2, z2 = rotate2d(y1, z1, ang_yz)     # around the y-axis

    return x2, y2, z2


def rotate2d(x, y, ang):
    """Rotate a data set (x,y,z) by an angle [deg] in each plane [xy, xz, yz]"""
    angr = np.deg2rad(ang)
    x1 = np.cos(angr) * x - np.sin(angr) * y
    y1 = np.sin(angr) * x + np.cos(angr) * y

    return x1, y1


def angle_from_pca2d(x, y):
    """
    Returns the rotation of the principle component relative to the 2D axis

    https://alyssaq.github.io/2015/computing-the-axes-or-orientation-of-a-blob/
    """
    cov = np.cov(np.vstack([x, y]))         # get the covariant matrix
    evals, evecs = np.linalg.eig(cov)       # find the eigenvalues/-vectors
    sort_indices = np.argsort(evals)[::-1]  # get the largest eigenvalue
    dx, dy = evecs[:, sort_indices[0]]      # the vector components
    angle = np.rad2deg(np.arctan2(dy, dx))  # make an angle relative to the axes

    return angle


def reorient_coords(x, y, z):
    """
    Re-orients a set of coordinated along the principle components

    Breaks a set of 3D rotations down into 3x 2D rotations
    """
    ang = angle_from_pca2d(x, y)
    x1, y1 = rotate2d(x, y, -ang)
    ang = angle_from_pca2d(x1, z)
    x2, z1 = rotate2d(x1, z, -ang)
    ang = angle_from_pca2d(y1, z1)
    y2, z2 = rotate2d(y1, z1, -ang)

    return x2, y2, z2


def plot_data_set(x, y, z, axes_limit=4):
    """ Scatter plot of the particles in all 3 planes: x-y , x-z, y-z """

    plt.figure(figsize=(18,12))
    for k, ai, aj, li, lj, title in [[1, x, y, "X", "Y", "Face-on"],
                                    [2, x, z, "X", "Z", "Edge-on"],
                                    [3, y, z, "Y", "Z", "End-on"]]:
        # scatter plots of the particles
        plt.subplot(2, 3, k)
        plt.scatter(ai, aj, s=1)
        plt.xlim(-axes_limit, axes_limit)
        plt.ylim(-axes_limit, axes_limit)
        plt.xlabel(li)
        plt.ylabel(lj)
        plt.title(title)

        # intensity maps of the particles
        plt.subplot(2, 3, k+3)
        bins = np.linspace(-axes_limit, axes_limit, 41)
        plt.hist2d(ai, aj, bins=bins, norm=LogNorm())

    plt.colorbar()


def make_data_set(dx=1, dy=0.3, dz=0.1, ang_xy=45, ang_xz=22, ang_yz=11, n=1000):
    """
    Makes a data set of points using a gaussian distribution along each axis

    Parameters
    ----------
    dx, dy, dz : float
        length along each axis
    ang_xy, ang_xz, ang_yz :
        [degree] rotation angle in the plane, i.e. ang_xy is the rotation angle
        around the z-axis
    n : int
        number of points in the data set

    Returns
    -------
    x, y, z : arrays of floats
        Coordinates of particles in the data set

    """
    # np.random.seed(9001)
    x = np.random.normal(loc=0, scale=dx, size=n)
    y = np.random.normal(loc=0, scale=dy, size=n)
    z = np.random.normal(loc=0, scale=dz, size=n)
    x, y, z = rotate3d(x, y, z, ang_xy, ang_xz, ang_yz)

    return x, y, z
