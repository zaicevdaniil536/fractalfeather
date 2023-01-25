import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_feathers():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    feathers = f.generate()
    # Add noise to the fractal shape to make it look more like feathers
    noise = np.random.normal(0, 0.05, feathers.shape)
    feathers = feathers + noise
    feathers = np.clip(feathers, 0, 1)
    # Apply a feathers-like color map to the fractal shape
    feathers = plt.cm.Reds(feathers)
    # Return the fractal feathers
    return feathers

# Generate 10 fractal feathers images
for i in range(10):
    feathers = generate_fractal_feathers()
    plt.imsave("fractal_feathers_{}.png".format(i), feathers)
