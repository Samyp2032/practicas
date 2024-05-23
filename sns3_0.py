#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
tips_df = sns.load_dataset("tips");
print(tips_df)

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
tips_df = sns.load_dataset("tips");
print(tips_df)
sns.barplot(x='day', y='total_bill', data=tips_df);

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
tips_df = sns.load_dataset("tips");
print(tips_df)
sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df);

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
tips_df = sns.load_dataset("tips");
print(tips_df)
sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df);

#%%
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
tips_df = sns.load_dataset("tips");
# Chart title
plt.title("Daily Total Bill")
# Draw a nested boxplot to show bills by day and time
sns.boxplot(x=tips_df.day,y=tips_df.total_bill,hue=tips_df.smoker);

# %%
