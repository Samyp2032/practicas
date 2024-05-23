#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimension de Sepalo')
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100);
# %%

#%%
import matplotlib.pyplot as plt
import seaborn as sns
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width);
# %%

#%%
import matplotlib.pyplot as plt
import seaborn as sns
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=3);

#%%
import matplotlib.pyplot as plt
import seaborn as sns
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5]);
# %%

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
plt.hist(virginica_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
# %%

#%%
import matplotlib.pyplot as plt
import seaborn as sns
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Dimensiones de Sepalo')
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],

bins=np.arange(2, 5, 0.25),
stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']);

# %%

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
plt.figure(figsize=(12, 6))
matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
sns.set_style("darkgrid")
plt.bar(years, oranges);
plt.bar(years, oranges, bottom=apples);
plt.xlabel('Año')
plt.ylabel('Rendimiento (toneladas por hectárea)');
plt.title("Rendimiento de los campos en Baja California")
plt.legend(['Manzanas', 'Naranjas'])
# %%
