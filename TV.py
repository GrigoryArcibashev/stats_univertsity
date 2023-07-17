import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


class DistributionAndDensity:
    def __init__(self, sample_average, mean_square_deviation):
        self._SA = sample_average
        self._MSD = mean_square_deviation

    def draw_distribution_and_density(self):
        # the three sigma rule
        x_vals = np.linspace(
                self._SA - 3 * self._MSD,
                self._SA + 3 * self._MSD,
                50)
        distribution_vals = [self._distribution(x) for x in x_vals]
        density_vals = [self._density(x) for x in x_vals]

        self._draw(
                distribution_vals,
                density_vals,
                x_vals)

    def _distribution(self, x):
        return scipy.stats.norm.cdf((x - self._SA) / self._MSD)

    def _density(self, x):
        return scipy.stats.norm.pdf((x - self._SA) / self._MSD)

    def _draw(
            self,
            distribution_vals,
            density_vals,
            x_vals):
        fig, ax = plt.subplots(1, 1)
        plt.xlabel("x")
        plt.ylabel("y")
        ax.plot(x_vals, distribution_vals, label="Распределение вероятностей")
        ax.plot(x_vals, density_vals, label="Плотность вероятности")
        self._draw_mark_of_SA(ax)
        ax.legend(loc="best", frameon=False)

    def _draw_mark_of_SA(self, ax):
        ax.plot(
                [self._SA, self._SA],
                [0, 0.95],
                color="black",
                linestyle="--",
                linewidth=0.8)


class Frequencies:
    def __init__(self, x_vals, empirical_frs, theoretical_frs):
        self._x_vals = x_vals
        self._empirical_frs = empirical_frs
        self._theoretical_frs = theoretical_frs

    def draw_empirical_and_theoretical_frequencies(self):
        fig, ax = plt.subplots(1, 1)
        plt.xlabel("x")
        plt.ylabel("n")
        ax.plot(
                self._x_vals,
                self._empirical_frs,
                label="Эмпирические частоты")
        ax.plot(
                self._x_vals,
                self._theoretical_frs,
                label="Теоретические частоты")
        self._draw_vertical_lines(ax)
        ax.legend(loc="best", frameon=False)

    def _draw_vertical_lines(self, ax):
        for x in self._x_vals:
            y_st = 0 if x < 90 else 5 if x < 96 else 2
            ax.plot(
                    [x, x],
                    [y_st, 30],
                    color="black",
                    linestyle="--",
                    linewidth=0.8)


def main():
    DistributionAndDensity(92.86, 2.83).draw_distribution_and_density()
    Frequencies(
            [x for x in range(86, 100, 2)],  # x_k values
            [1, 6, 16, 29, 21, 10, 10],
            [1.767, 6.231, 15.717, 24.552, 22.692, 15.345, 6.696]) \
        .draw_empirical_and_theoretical_frequencies()
    plt.show()


if __name__ == "__main__":
    main()
