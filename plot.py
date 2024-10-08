import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
import os

def plot_particles(particles, filename):
    """Plot particles in 3D and save as a frame."""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    for particle in particles:
        ax.scatter(particle.x, particle.y, particle.z, s=particle.radius * 1000, color=particle.color, alpha=0.6)

    ax.set_title('3D Particle Collision Simulation')
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_zlabel('Z Position')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)

    plt.savefig(filename)
    plt.close()

def create_gif(frame_filenames, output_gif='particle_collision.gif', duration=0.1):
    """Create a GIF from a list of frame filenames."""
    with imageio.get_writer(output_gif, mode='I', duration=duration) as writer:
        for filename in frame_filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    # Remove the frame files after creating the GIF
    for filename in frame_filenames:
        os.remove(filename)
