import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995]).T
df.head()
stats = df.describe(percentiles=[0.025, 0.975]).T
stats['err'] = stats.apply(lambda row: 1.96*row['std']/math.sqrt(row['count']), axis=1)
stats
fig = plt.figure()
ax = fig.add_subplot(111)

index = range(len(stats.index))
bars = plt.bar(index, stats['mean'], width=0.85, alpha=0.9, color='grey',
               yerr=stats['err'], error_kw={'capsize': 5, 'elinewidth': 2, 'alpha':0.7})
plt.xticks(index, stats.index)

plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='on', labelbottom='on')
for spine in ax.spines.values():
    spine.set_visible(False)