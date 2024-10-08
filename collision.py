import numpy as np
from particle import Particle

def detect_collision(particles):
    """Detect collisions between particles."""
    collisions = []
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            dx = particles[i].x - particles[j].x
            dy = particles[i].y - particles[j].y
            dz = particles[i].z - particles[j].z
            distance = (dx**2 + dy**2 + dz**2)**0.5
            if distance < (particles[i].radius + particles[j].radius):
                collisions.append((i, j))
    return collisions

def handle_collisions(particles, collisions):
    """Handle particle collisions by updating velocities and creating new particles."""
    for i, j in collisions:
        # Calculate the midpoint for the new particle
        new_particle = Particle(
            (particles[i].x + particles[j].x) / 2,
            (particles[i].y + particles[j].y) / 2,
            (particles[i].z + particles[j].z) / 2,
            np.random.uniform(-0.05, 0.05),
            np.random.uniform(-0.05, 0.05),
            np.random.uniform(-0.05, 0.05),
            0.1,  # new particle radius
            'yellow'  # color of new particle
        )
        particles.append(new_particle)

        # Reverse velocities of the colliding particles
        particles[i].vx *= -1
        particles[i].vy *= -1
        particles[i].vz *= -1
        particles[j].vx *= -1
        particles[j].vy *= -1
        particles[j].vz *= -1
