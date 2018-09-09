#http://markthegraph.blogspot.com/2015/05/using-python-statsmodels-for-ols-#linear.html

import numpy as np

x = np.random.randn(100)

y = x + np.random.randn(100) + 10

x=[4843, 6192, 7520, 8802, 8802]
y=[3.478, 3.716, 4.167, 4.506, 4.596]
print(x)
print()
print(y)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))

ax.scatter(x, y, alpha=0.5, color='orchid')
fig.suptitle('Example Scatter Plot')
fig.tight_layout(pad=2); 
ax.grid(True)
fig.savefig('filename1.png', dpi=125)

import statsmodels.api as sm

x = sm.add_constant(x) # constant intercept term

# Model: y ~ x + c

model = sm.OLS(y, x)

fitted = model.fit()

x_pred = np.linspace(x.min(), x.max(), 50)

x_pred2 = sm.add_constant(x_pred)

y_pred = fitted.predict(x_pred2)

ax.plot(x_pred, y_pred, '-', color='darkorchid', linewidth=2)

fig.savefig('filename2.png', dpi=125)

print(fitted.params)     # the estimated parameters for the regression line
print(fitted.summary())  # summary statistics for the regression

y_hat = fitted.predict(x) # x is an array from line 12 above

y_err = y - y_hat

mean_x = x.T[1].mean()

n = len(x)

dof = n - fitted.df_model - 1

from scipy import stats

t = stats.t.ppf(1-0.025, df=dof)

s_err = np.sum(np.power(y_err, 2))

conf = t * np.sqrt((s_err/(n-2))*(1.0/n + (np.power((x_pred-mean_x),2) / 
         ((np.sum(np.power(x_pred,2))) - n*(np.power(mean_x,2))))))

upper = y_pred + abs(conf)

lower = y_pred - abs(conf)

ax.fill_between(x_pred, lower, upper, color='#888888', alpha=0.4)

fig.savefig('filename3.png', dpi=125)
