#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


data = {
    't': [2003.2, 2004.1, 2004.2, 2005.1, 2005.2, 2006.1, 2006.2, 2007.1, 2007.2, 2008.1, 2008.2, 2009.1, 2009.2],
    'Yt': [13.09, 17.62, 20.05, 12.76, 18.64, 15.95, 21.32, 30.61, 30.86, 25.8, 30.74, 29.66, 33.67]
}

df = pd.DataFrame(data)
print(df)


# In[6]:


import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


data = {
    't': [2003.2, 2004.1, 2004.2, 2005.1, 2005.2, 2006.1, 2006.2, 2007.1, 2007.2, 2008.1, 2008.2, 2009.1, 2009.2],
    'Yt': [13.09, 17.62, 20.05, 12.76, 18.64, 15.95, 21.32, 30.61, 30.86, 25.8, 30.74, 29.66, 33.67]
}

df = pd.DataFrame(data)

# AEH con alfa=0.3, gamma=0.6
model1 = ExponentialSmoothing(np.asarray(df['Yt'][:-3]), seasonal_periods=2, trend='add', seasonal='add')
model1 = model1.fit(smoothing_level=0.3, smoothing_slope=0.6)

# AEH con alfa=0.7, gamma=0.4
model2 = ExponentialSmoothing(np.asarray(df['Yt'][:-3]), seasonal_periods=2, trend='add', seasonal='add')
model2 = model2.fit(smoothing_level=0.7, smoothing_slope=0.4)

df['AEH_0.3_0.6'] = np.append(model1.fittedvalues, model1.forecast(3))
df['AEH_0.7_0.4'] = np.append(model2.fittedvalues, model2.forecast(3))

# Evaluamos cuál modelo es mejor
mse1 = mean_squared_error(df['Yt'][:-3], df['AEH_0.3_0.6'][:-3])
mse2 = mean_squared_error(df['Yt'][:-3], df['AEH_0.7_0.4'][:-3])

print(f'MSE AEH(0.3, 0.6): {mse1}')
print(f'MSE AEH(0.7, 0.4): {mse2}')


# In[7]:


import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


data = {
    't': [2003.2, 2004.1, 2004.2, 2005.1, 2005.2, 2006.1, 2006.2, 2007.1, 2007.2, 2008.1, 2008.2, 2009.1, 2009.2],
    'Yt': [13.09, 17.62, 20.05, 12.76, 18.64, 15.95, 21.32, 30.61, 30.86, 25.8, 30.74, 29.66, 33.67]
}

df = pd.DataFrame(data)

# Doble media móvil con k=4
df['SMA_4'] = df['Yt'].rolling(window=4).mean()

# Doble media móvil con k=2
df['SMA_2'] = df['Yt'].rolling(window=2).mean()

# Evaluamos cuál método es mejor
mse3 = mean_squared_error(df['Yt'][3:-3], df['SMA_4'][3:-3])
mse4 = mean_squared_error(df['Yt'][1:-3], df['SMA_2'][1:-3])

print(f'MSESMA(4): {mse3}')
print(f'MSE SMA(2): {mse4}')


# In[8]:


import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error


data = {
    't': [2003.2, 2004.1, 2004.2, 2005.1, 2005.2, 2006.1, 2006.2, 2007.1, 2007.2, 2008.1, 2008.2, 2009.1, 2009.2],
    'Yt': [13.09, 17.62, 20.05, 12.76, 18.64, 15.95, 21.32, 30.61, 30.86, 25.8, 30.74, 29.66, 33.67]
}

df = pd.DataFrame(data)

# Ajustar una línea a los datos
z = np.polyfit(df['t'][:-3], df['Yt'][:-3], 1)
p = np.poly1d(z)

df['trend_line'] = p(df['t'])

# Evaluar la precisión
mse5 = mean_squared_error(df['Yt'][:-3], df['trend_line'][:-3])

print(f'MSE Trend Line: {mse5}')


# In[9]:


plt.figure(figsize=(12, 8))
plt.plot(df['t'], df['Yt'], marker='o', label='Yt')
plt.plot(df['t'], df['AEH_0.3_0.6'], marker='o', label='AEH(0.3, 0.6)')
plt.plot(df['t'], df['AEH_0.7_0.4'], marker='o', label='AEH(0.7, 0.4)')
plt.plot(df['t'], df['SMA_4'], marker='o', label='SMA(4)')
plt.plot(df['t'], df['SMA_2'], marker='o', label='SMA(2)')
plt.plot(df['t'], df['trend_line'], marker='o', label='Trend Line')
plt.legend()
plt.show()


# In[ ]:




