# Seaborn-Plots-with-Data
Seaborn plots with randomly generated and imported data


## Overview
- A Seaborn display of plots using random genreated data and imported data. Seaborn is useful for producing visualy appealing plots, more than matplotlib. Plots can be genrated with a few lines of code.

## Methods
- Random generated data is produced with a different number of bins, and then plotted. We create some synthetic bimodal data by drawing from two separate normal/lognormal distributions and combine the two into two  bimodal data sets.  We do this by drawing from **random.normal( )** twice for  two normal distributions ($x_1,x_2$) and twice from **random.lognormal( )** for two lognormal distributions ($y_1,y_2$). When we plot our xdata as a histogram, we can see that we have a broadly bimodal distribution. We also plot the mean of the distribution as a red line. We can plot kernel density estimates using the **sns.kdeplot( )** function.



## Results

- 
What the code produces:
- Plots
- Simulations
- Key findings

## How to Run
1. Clone the repository
2. Install dependencies
3. Run the main script
