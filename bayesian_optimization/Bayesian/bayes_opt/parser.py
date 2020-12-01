import json

import matplotlib
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


def styblinski_tang(x, y):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """

    return 0.5*((x**4 - 16*x**2 + 5*x) + (y**4 - 16*y**2 + 5*y))


def parse(file_name):
    x_points = []
    y_points = []
    target = []
    with open(file_name, "r") as read_file:
        for line in read_file.readlines():
            data = json.loads(line)
            points = data['params']
            target.append(data['target'])
            x_points.append(points['x'])
            y_points.append(points['y'])
    # print(len(x_points), len(y_points), len(target))
    # print(x_points)
    # print(y_points)
    # print(target)
    return x_points, y_points, target

def plotting(x,y,z):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x_f = np.linspace(-5, 5, 100)
    y_f = np.linspace(-5, 5, 100)
    x_fm, y_fm = np.meshgrid(x_f, y_f)
    z_f = styblinski_tang(x_fm, y_fm)

    # for i in range(100):
    #     for j in range(100):
    #         z_f[i,j] = styblinski_tang(x_fm[i], y_fm[j])

    ax.plot_surface(x_fm, y_fm, z_f, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')

    for i in range(len(z)):
        z[i] = -z[i]

    # Data for three-dimensional scattered points
    ax.scatter3D(x, y, z, c=z, cmap='OrRd_r')
    plt.title('Styblinsky Tang function')
    plt.show()


def convergence(x, y, z):
    z_f = np.zeros(len(x))
    max_now = np.abs(np.argmax(z))
    for i in range(len(x)):
        if i == 0:
            z[i] = max_now
        temp = np.abs(z[i] - z[i-1])
        if max_now < temp:
            z_f[i] = max_now
        else:
            z_f[i] = temp
            max_now = temp

    x_f = np.linspace(0, len(x)-1, len(x))

    plt.plot(x_f, z_f)
    plt.show()


def convergence_to_actual(x, y, z):
    z_f = np.zeros(len(x))
    max_now = np.abs(np.argmax(z))
    for i in range(len(x)):
        if i == 0:
            z[i] = max_now
        temp = np.abs(z[i] - 78.33198)
        if max_now < temp:
            z_f[i] = max_now
        else:
            z_f[i] = temp
            max_now = temp

    x_f = np.linspace(0, len(x)-1, len(x))

    plt.plot(x_f, z_f)
    plt.show()


x,y,z = parse("./logs300.json")
convergence_to_actual(x,y,z)
