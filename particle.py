import numpy as np

class Particle:
    def __init__(self, x, y, z, vx, vy, vz, radius, color):
        self.x = x        # x-coordinate
        self.y = y        # y-coordinate
        self.z = z        # z-coordinate
        self.vx = vx      # velocity in x-direction
        self.vy = vy      # velocity in y-direction
        self.vz = vz      # velocity in z-direction
        self.radius = radius  # radius of the particle
        self.color = color  # color of the particle

    def move(self):
        """Update the position of the particle based on its velocity."""
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
