import numpy as np

def calculate_volatility(stock_data):
    returns = np.log(stock_data / stock_data.shift(1))
    return np.std(returns)

# Portfolio optimization logic...
