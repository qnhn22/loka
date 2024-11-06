import numpy as np
from rank_abc import RankInterface
class ParetoOptimization(RankInterface):
    def __init__(self,data):
        super().__init__(data)
        self.pareto_front = []

    def is_dominated(self, point, other_point):
        return (other_point[0] >= point[0] and  # distance (maximize)
                other_point[1] <= point[1] and  # price (minimize)
                other_point[2] >= point[2] and  # population (maximize)
                any([other_point[0] > point[0],
                     other_point[1] < point[1],
                     other_point[2] > point[2]]))

    def rank_data(self):
        self.pareto_front = []
        for i, point in enumerate(self.data):
            if not any(self.is_dominated(point, other_point) 
                       for other_point in self.data if not np.array_equal(point, other_point)):
                self.pareto_front.append(point)
        return np.array(self.pareto_front)


if __name__ == "__main__":
    np.random.seed(42)
    n_points = 100
    distance = np.random.uniform(50, 300, n_points)
    price = np.random.uniform(100, 1000, n_points)
    population = np.random.uniform(10000, 100000, n_points)
    data = np.column_stack((distance, price, population))
    parento_opt= ParetoOptimization(data)
    pareto_front = parento_opt.rank_data()
    print(pareto_front)
