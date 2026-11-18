"""
 Please merge the functions and classes from this file with the same file from the previous
 homework assignment
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import io as scio

import me570_geometry


class SphereWorld:
    """
    Class for loading and plotting a 2-D sphereworld.
    """

    def __init__(self):
        """
        Load the sphere world from the provided file sphereworld.mat, and sets the
    following attributes:
     -  world: a  nb_spheres list of  Sphere objects defining all the spherical obstacles in the
    sphere world.
     -  x_start, a [2 x nb_start] array of initial starting locations (one for each column).
     -  x_goal, a [2 x nb_goal] vector containing the coordinates of different goal locations (one
    for each column).
        """
        data = scio.loadmat('sphereworld.mat')

        self.world = []
        for sphere_args in np.reshape(data['world'], (-1, )):
            sphere_args[1] = sphere_args[1].item()
            sphere_args[2] = sphere_args[2].item()
            self.world.append(me570_geometry.Sphere(*sphere_args))

        self.x_goal = data['xGoal']
        self.x_start = data['xStart']
        self.theta_start = data['thetaStart']

    def plot(self, axes=None):
        """
        Uses Sphere.plot to draw the spherical obstacles together with a  * marker at the goal
        location.
        """

        if axes is None:
            axes = plt.gca()

        for sphere in self.world:
            sphere.plot('r')

        plt.scatter(self.x_goal[0, :], self.x_goal[1, :], c='g', marker='*')

        plt.xlim([-11, 11])
        plt.ylim([-11, 11])
        plt.axis('equal')

    def is_collision(self, x_sample):
        """
        Checks if the points with coordinates   x is inside any of the spheres
        in   world. This is done by iterating over all spheres, using the
        function Sphere.distance from Homework 3 on each one of them, and then
        combining the results.
        """
        pass  # Substitute with your code
        return flag

    def sample(self):
        """
        Generate samples using the specified distribution, until
        Sphereworld.is_collision returns   false for a sample, or a maximum
        number of trials   nb_trials is reached.
        """
        pass  # Substitute with your code
        return x_sample
