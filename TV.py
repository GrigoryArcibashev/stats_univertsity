import scipy.stats
import numpy as np
import matplotlib.pyplot as plt


class DistributionAndDensity:
    def __init__(self, SA, MSD):
        self._SA = SA
        self._MSD = MSD

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
        fig1, ax1 = plt.subplots(1, 1)
        plt.xlabel("x")
        plt.ylabel("y")
        ax1.plot(x_vals, distribution_vals, label="Распределение вероятностей")
        ax1.plot(x_vals, density_vals, label="Плотность вероятности")
        self._draw_mark_of_SA(ax1)
        ax1.legend(loc="best", frameon=False)

    def _draw_mark_of_SA(self, ax1):
        ax1.plot(
                [self._SA, self._SA],
                [0, 0.95],
                color="black",
                linestyle="--",
                linewidth=0.8)


class Frequencies:
    def __init__(self):
        self._x_vals = [x for x in range(86, 100, 2)]
        self._empirical_frs = [1, 6, 16, 29, 21, 10, 10]
        self._theoretical_frs = \
            [1.767, 6.231, 15.717, 24.552, 22.692, 15.345, 6.696]

    def draw_empirical_and_theoretical_frequencies(self):
        fig2, ax2 = plt.subplots(1, 1)
        plt.xlabel("x")
        plt.ylabel("n")
        ax2.plot(
                self._x_vals,
                self._empirical_frs,
                label="Эмпирические частоты")
        ax2.plot(
                self._x_vals,
                self._theoretical_frs,
                label="Теоретические частоты")
        self._draw_vertical_lines(ax2)
        ax2.legend(loc="best", frameon=False)

    def _draw_vertical_lines(self, ax2):
        for x in self._x_vals:
            y_st = 0 if x < 90 else 5 if x < 96 else 2
            ax2.plot(
                    [x, x],
                    [y_st, 30],
                    color="black",
                    linestyle="--",
                    linewidth=0.8)


def main():
    SA = 92.86  # sample_average
    MSD = 2.83  # mean square deviation
    DistributionAndDensity(SA, MSD).draw_distribution_and_density()
    Frequencies().draw_empirical_and_theoretical_frequencies()
    plt.show()


if __name__ == "__main__":
    main()
