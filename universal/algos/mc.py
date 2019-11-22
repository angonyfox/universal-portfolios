from ..algo import Algo
from .. import tools
import numpy as np
from random import randint


class MC(Algo):
    """ Monte Carlo Simulation (random walk)
    """

    def __init__(self, b=None):
        """
        :params b: Constant rebalanced portfolio weights. Default is uniform.
        """
        super(MC, self).__init__()
        self.b = b


    def step(self, x, last_b):
        # init b to default if necessary
        self.b = np.zeros(len(x))
        r = randint(0,len(x)-1)
        self.b[r] = 1
        return self.b

if __name__ == '__main__':
    result = tools.quickrun(MC())
    print(result.information)