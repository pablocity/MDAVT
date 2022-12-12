import matplotlib.pyplot as plt


class Renderer:
    def render(self, X, Y):
        for y in Y:
            plt.plot(X, y)
        plt.show()
