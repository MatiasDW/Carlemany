import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Load the data
path = r"C:\Users\Matias Davila\OneDrive - DISTRIBUIDORA Y COMERCIALIZADORA OPEN\Documentos\Matias\Analisis multivariante\Labour.csv"
labour_data = pd.read_csv(path)

# Basic statistical summary
print(labour_data.describe())

# Pairplot of the Labour data
sns.pairplot(labour_data)
plt.title('Pairplot of Labour Data')
plt.show()

# Boxplot for each variable in Labour data
labour_data.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.suptitle('Boxplot of Each Variable in Labour Data')
plt.show()

# Heatmap of the correlation matrix
sns.heatmap(labour_data.corr(), annot=True, cmap="viridis")
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Simple linear regression (e.g., wage vs. capital)
X = labour_data[['capital']]  # Predictor variable
y = labour_data['wage']       # Response variable

# Using statsmodels
X = sm.add_constant(X)  # Adding a constant
model = sm.OLS(y, X).fit()
print(model.summary())

# Using sklearn for prediction
lin_reg = LinearRegression()
lin_reg.fit(X, y)

sns.regplot(x='capital', y='wage', data=labour_data)
plt.title('Scatter Plot with Regression Line: Wage vs Capital')
plt.show()

sns.pairplot(labour_data, hue='YourCategoricalVariable')
plt.show()
