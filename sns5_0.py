#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
img = Image.open('chart.jpeg')
img_array = np.array(img)
plt.imshow(img);
# %%
