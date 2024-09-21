import pandas as pd
import numpy as np
from rank_abc import RankInterface

def normalize(series):
    return (series - series.min()) / (series.max() - series.min())
class WeightSumOptimization(RankInterface):
    def __init__(self,data,weights=None):
        super().__init__(data)
        if weights is None:
            weights = {
                'distance': 0.4,  # maximize distance
                'price': -0.3,    #  minimize price (negative weight)
                'population': 0.3 #  maximize population
            }
        self.weights = weights
    def rank_data(self):
        df = pd.DataFrame(self.data)
        for column in df.columns:
            df[f'{column}_normalized'] = normalize(df[column])
        
        df['score'] = (
            self.weights['distance'] * df['distance_normalized'] +
            self.weights['price'] * (1 - df['price_normalized']) +
            self.weights['population'] * df['population_normalized']
        ) 
        df_sorted = df.sort_values('score', ascending=False)
        return df_sorted[['distance', 'price', 'population']]
 
if __name__=="__main__":
    data = {
    'distance': [100, 200, 150, 300, 250],
    'price': [500, 400, 600, 300, 450],
    'population': [50000, 75000, 60000, 90000, 80000]
}
    weight_opt= WeightSumOptimization(data)
    weight_rank=weight_opt.rank_data()
    print(weight_rank )
