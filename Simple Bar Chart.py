import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dt = pd.DataFrame({
    'Year': [2022, 2023, 2024, 2025],
    'Cost': [100000, 80000, 140000, 150000]
})

base_cost = dt['Cost'].loc[0]
dt['%Increase'] = ((dt['Cost'] - base_cost) / base_cost) * 100
dt['%Increase'] = dt['%Increase'].round(2)

plt.plot(figsize=(100, 100))
# plt.plot(dt['Year'], dt['Cost'], marker='o', label='Cost')
# plt.plot(dt['Year'], dt['%Increase'], marker='x', label='% Increase')
plt.bar(dt['Year'], dt['Cost'], color='skyblue')
plt.grid = (True)
plt.xlabel = ('Year')
plt.ylabel = ('Cost')
plt.show()
