# ***** LEGEND *****
# * States = {no lights blinking, left light blinking, right light blinking, both lights blinking}
# * State Keys(respectively) = {nlb, llb, rlb, blb}
# * Switches(appended to reciever vert to express input value) = {left-blinker, right-blinker, panic-button}
# * Switch Keys = {L-B, R-B, P-B}
#### Jupyter notebook cell start ####

%matplotlib inline
from jupyterthemes import jtplot
jtplot.style(context='talk', fscale=1, spines=False, gridlines='--')

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx
df = pd.DataFrame({'from':
                   ['start (nlb)', 'start (nlb)', 'start (nlb)', '<- (L-B) -> llb', '(P-B) -> blb' ],
                   'to': ['<- (L-B) -> llb', '(R-B) -> rlb ->', '(P-B) -> blb', '(R-B) -> rlb ->', 'start (nlb)']})
G=nx.from_pandas_edgelist(df, 'to', 'from')
nx.draw(G, with_labels=True, pos=nx.shell_layout(G), nodecolor='r', edge_color='b')
plt.show()
#### Jupyter notebook cell end ####