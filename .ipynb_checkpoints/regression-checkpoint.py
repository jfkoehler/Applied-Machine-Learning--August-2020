import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    import numpy as np
    def __init__(self, fit_intercept = False):
        self.coefs_ = None
        self.intercept_ = None
        self.fit_intercept = fit_intercept
        
    def fit(self, X, y):
        if self.fit_intercept:
            ones = np.ones((X.shape[0], 1))
            X = np.concatenate((ones, X), axis = 1)
        weights = np.linalg.inv(X.T@X)@X.T@y
        if self.fit_intercept:
            self.coefs_ = weights[1:]
            self.intercept_ = weights[0]
            return self
        self.coefs_ = weights
        
    def predict(self, X):
        if self.fit_intercept:
            return X@self.coefs_.T + self.intercept_
        return X@self.coefs_.T
    
class RegressionMetrics:
    import matplotlib.pyplot as plt
    def __init__(self, y_true, y_pred):
        self.y = y_true
        self.y_pred = y_pred
    
    def r_squared(self):
        ssr = np.sum((self.y - self.y_pred)**2)
#         ymean = np.mean(y_true)
        sst = np.sum((self.y - y.mean())**2)
        return 1 - ssr/sst
    
    def mse(self):
        self.mse_ = np.mean((self.y - self.y_pred)**2)
        return self.mse_
        
        
    def rmse(self):
        self.rmse_ = np.sqrt(self.mse_)
        return self.rmse_
        
        
    def plot(self):
        fig, ax = plt.subplots(1, 2, figsize = (15, 6))

        ax[0].plot(self.y - self.y_pred, 'ro', alpha = 0.2, markeredgecolor = 'black')
        ax[0].axhline(color = 'black')

        ax[1].hist(self.y- self.y_pred, bins = 50, color = 'grey', edgecolor = 'black');
        plt.suptitle(f'Evaluation Metrics for OLS fit:\n$r^2$={self.r_squared()}\nMSE:{self.mse()}\nRMSE:{self.rmse()}',
                    verticalalignment = 'bottom', horizontalalignment = 'left', fontsize = 20, x = 0)
        