import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


def main():
    X = np.random.rand(100, 10)
    y = X[:, 0] * 5 + X[:, 4] * 2 + np.random.rand(100) * 4
    
    plt.scatter(X[:, 0], y)
    plt.show()


if __name__ == "__main__":
    main()
