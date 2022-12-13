import matplotlib.pyplot as plt


class Renderer:
    def render(self, X, Y):
        a = type(X[3])
        plt.plot(X, Y)
        plt.show()
