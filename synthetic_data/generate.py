# generate.py

from math import pi
import numpy as np

def sine_data(
    min_x=0,
    max_x=2*pi,
    n=1000,
    amplitude=1,
    error_mean=0,
    error_std_dev=1,
    seed=123
):
    """
    Returns a tuple (X, y)

    Note that X and y are both 1-D numpy arrays of length n, where X is a
    uniform random sample of n items between min_x and max_x (inclusive),
    and y is the value of amplitude * sin(x) for each x in X plus some error
    pulled from a normal distribution with mean `error_mean` and standard
    deviation error_std_dev`.
    """

    # set a seed for repeatable results
    np.random.seed(seed)

    # generate the x-values
    X = np.random.uniform(
        low=min_x,
        high=max_x,
        size=n
    )

    # generate the errors
    error_noise = np.random.normal(
        loc=error_mean,
        scale=error_std_dev,
        size=n
    )

    # generate the y-values
    y = amplitude * np.sin(X) + error_noise
    # y = amplitude + error_noise

    return X, y

if __name__ == '__main__':
    # simple test of function outputs on execution of script
    X, y = sine_data(n=5)
    print(X)
    print()
    print(y)
