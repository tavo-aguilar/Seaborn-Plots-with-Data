import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as random

import seaborn as sns

#Random Data

xdata1=random.normal(20,25,5000) # first x draw
xdata2=random.normal(100,25,5000) # second x draw
ydata1=random.lognormal(2,0.1,8000) # first y draw
ydata2=random.lognormal(3,0.1,2000) # second y draw
xdata=np.append(xdata1,xdata2) # combine the two x data sets
ydata=np.append(ydata1,ydata2) # combine the two y data sets


# make the histogram
plt.hist(xdata,bins=50);
# put on a heavy (linewidth=3) vertical red line at the mean of xdata
plt.axvline(np.mean(xdata),color='red',linewidth=3);   # axvline adds a vertical line to a Matplotlib plot

sns.kdeplot(xdata,fill=True,cut=0);  # cut determines how far the evaluation grid extends past the extreme datapoints. When set to 0, truncate the curve at the data limits.

sns.histplot(xdata, kde=True,stat="density", kde_kws=dict(cut=3),alpha=0.2,color='red');  # alpha: transparency level. 0: fully transparent. 1: fully opaque

sns.histplot(ydata, kde=True,stat="density", kde_kws=dict(cut=3),alpha=.2,color='blue');

plt.plot(xdata,ydata,'.')
plt.xlabel('x:length')
plt.ylabel('y:width')


df = pd.DataFrame({'x': xdata, 'y': ydata})
sns.jointplot(data=df,x="x", y="y",kind='scatter',color='blue');

sns.jointplot(data=df,x="x", y="y",kind='kde');

# Create the joint plot with kernel density estimate
g = sns.jointplot(data=df, x="x", y="y", kind='kde', joint_kws={'color':'red'})
# Add a scatter plot on top of the KDE plot
g.plot_joint(sns.scatterplot, color="lightgreen", s=20, edgecolor="black")


sns.jointplot(data=df,x="x", y="y",kind='hist');


sns.jointplot(df,x='x',y='y',kind='hex');

#With Data
MantleArray=pd.read_csv('/Users/gustavoaguilar/Downloads/Datasets for Python Earth/GeoRoc/MantleArray_OIB.csv')

sns.pairplot(MantleArray,\
             vars=['EPSILON_ND','SR87_SR86','PB206_PB204','EPSILON_HF'],\
             hue='LOCATION');

plt.show()