
#----- Get Inputs -------------
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('frames')
parser.add_argument('labels')
args = parser.parse_args()
#-------------------------------



#----- Read Data ----------------

from tifffile import imread

frames = imread(args.frames)
labels = imread(args.labels)
#--------------------------------



#----- Analyze Data -------------

import numpy as np
import pandas as pd

traces = np.array([frames[:, labels==id].mean(1) for id in np.unique(labels)[1:]])
cell_activity = (
    pd.DataFrame(traces.T)
    .rename_axis(index='Frame')
    .melt(var_name='Cell', value_name='Mean', ignore_index=False)
    .reset_index()
)
cell_activity.Cell += 1

#-------------------------------



#----- View Analysis ------------
import matplotlib.pyplot as plt
import seaborn as sns

g = sns.FacetGrid(
    data=cell_activity, 
    col='Cell', 
    col_wrap=3, 
    sharey=False, 
    sharex=True,
)
g.map_dataframe(
    sns.lineplot, 
    x='Frame', 
    y='Mean'
);
plt.suptitle('Mean Cell Activity')
g.tight_layout();
g.savefig('results.png');
print('File Created: results.png')
#-----------------------------------
