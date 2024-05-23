#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
print(flights_df)
# %%

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
print(flights_df)
plt.title("Número de pasajeros (1000s)")
sns.heatmap(flights_df);
# %%

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
flights_df = sns.load_dataset("flights").pivot(index="month", columns="year", values="passengers")
plt.title("Número de pasajeros (1000s)")
sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues');
# %%

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Flores')
sns.kdeplot(x=flowers_df.sepal_length,
y=flowers_df.sepal_width,
shade=True,
shade_lowest=False);

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
plt.figure(figsize=(12, 6))
plt.title('Flores')
setosa = flowers_df[flowers_df.species ==
'setosa']
virginica = flowers_df[flowers_df.species ==
'virginica']
plt.title("Flowers (Setosa & Virginica)")
sns.kdeplot(x=setosa.sepal_length,
y=setosa.sepal_width,
shade=True, cmap='Reds',
shade_lowest=False)

sns.kdeplot(x=virginica.sepal_length,
y=virginica.sepal_width,
shade=True, cmap='Blues',
shade_lowest=False);
# %%
