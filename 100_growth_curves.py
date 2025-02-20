import pandas as pd

def generate_growth_curves():
    data = []
    for i in range(100):
        population_curve = logistic_growth(K=1000, r=0.1, time=200, lag_factor=0.5, exp_factor=1.5)
        data.append(population_curve)
    df = pd.DataFrame(data)
    return df
  
