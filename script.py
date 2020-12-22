import numpy as np

def generate_random(size= 10):
    x = [np.random.randint() for _ in range(size)]
    return x