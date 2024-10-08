import numpy as np
from particle import Particle
from collision import detect_collision, handle_collisions
from plot import plot_particles, create_gif

def main():
    # Create particles
    np.random.seed(42)  # For reproducibility
    num_particles = 20  # Increase the number of particles for more interactions
    particles = []

    for _ in range(num_particles):
        x = np.random.uniform(1, 9)
        y = np.random.uniform(1, 9)
        z = np.random.uniform(1, 9)
        vx = np.random.uniform(-0.1, 0.1)
        vy = np.random.uniform(-0.1, 0.1)
        vz = np.random.uniform(-0.1, 0.1)
        radius = 0.2
        color = np.random.choice(['red', 'blue', 'green', 'purple', 'orange'])  # Random color for each particle
        particles.append(Particle(x, y, z, vx, vy, vz, radius, color))

    # Store frame filenames for the GIF
    frame_filenames = []

    # Simulation loop
    for frame in range(100):
        # Move particles
        for particle in particles:
            particle.move()

        # Detect collisions
        collisions = detect_collision(particles)

        # Handle collisions
        handle_collisions(particles, collisions)

        # Plot particles and save the frame
        frame_filename = f'frame_{frame:03d}.png'
        plot_particles(particles, frame_filename)
        frame_filenames.append(frame_filename)

    # Create a GIF from the frames
    create_gif(frame_filenames, output_gif='particle_collision.gif', duration=0.1)

if __name__ == "__main__":
    main()
