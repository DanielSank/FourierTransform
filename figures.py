import numpy as np
import matplotlib.pyplot as plt


def go():
    points = []
    for x in np.linspace(-10, 10, 21):
        for y in np.linspace(-10, 10, 21):
            points.append((x, y))
    points = np.array(points).T

    matrix = np.array(
            [
                [1, 0.5],
                [0.5, 1],
            ]
    )
    points_transformed = np.matmul(matrix, points)

    fig, ax = plt.subplots()
    ax.plot(
            points_transformed[0, :],
            points_transformed[1, :],
            linewidth=0,
            marker=".",
            markersize=4,
    )
    plt.show()

