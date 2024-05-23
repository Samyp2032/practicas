
#%%
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.figure(figsize=(12, 6))
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00FFFF'
sns.set_style("darkgrid")
fmt = 's-b'
plt.plot(years, apples, fmt);
plt.plot(years, oranges, 'o--r');
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
