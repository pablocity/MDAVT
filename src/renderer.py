import matplotlib.pyplot as plt


class Renderer:
    def render(self, X, Y):
        X = [x for x in X if x < 95]
        Y = [y for y in Y if y < 95]
        plt.scatter(X, Y)
        plt.show()
