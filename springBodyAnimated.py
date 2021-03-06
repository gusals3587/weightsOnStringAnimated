from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import unittest
import numpy as np

def main():
    fig, ax = plt.subplots()
    weight = Body(y = 1.0, v = 0.0, dt = 0.1, ax = ax)
    anim = FuncAnimation(fig, weight, init_func=weight.init)
    plt.show()

class Body():


    def __init__(self, y, v, dt, ax):
        # t is the x-axis, y is the y-axis
        self.y = [y]
        self.v = v
        self.a = -y
        self.t = [0.0]
        self.dt = dt
        self.ax = ax
        self.line, = ax.plot([], [])
        self.line.set_drawstyle('steps')
        self.ax.set_ylim(-1.2, 1.2)
        self.ax.set_xlim(0, 5)
        self.ax.spines['bottom'].set_position('center')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

    def init(self):
        self.line.set_data(self.t, self.y)
        return self.line,

    def __call__(self, i):
        if i == 0:
            self.v += (self.dt / 2) * self.a
        else:
            self.v += + self.dt * self.a
        if self.t[-1] >= self.ax.get_xlim()[1]:
            newXlim = self.ax.get_xlim()[1] * 2
            self.ax.set_xlim(right=newXlim)
        self.t += [self.t[-1] + self.dt]
        self.y += [self.y[-1] + (self.dt * self.v)]
        self.a = -self.y[-1]
        self.line.set_data(self.t, self.y)
        cos = self.ax.plot(self.t, np.cos(self.t), 'r')
        return self.line, cos

class TestSimulationMethods(unittest.TestCase):

    def setUp(self):
        self.fig, self.ax = plt.subplots()
        self.body = Body(y=1.0, v=0.0, dt=0.1, ax=self.ax)

    def test_bodyInit(self):
        testPlot = self.ax.plot(0.0, 1.0)[0]
        dataPoint = self.body.init()[0]
        self.assertEqual(testPlot.get_data(), dataPoint.get_data())

    def test_bodyCall(self):
        testPlot = self.ax.plot([0.0, 0.1], [1.0, 0.99])[0]
        dataPoint = self.body(1)[0]

        for i, j in zip(testPlot.get_data(), dataPoint.get_data()):
            self.assertEqual(i[0], j[0])
            self.assertEqual(i[1], j[1])

if __name__ == "__main__":
    main()