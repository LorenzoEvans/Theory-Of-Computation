# import networkx as nx
# import matplotlib as mpl
# import matplotlib.pyplot
# %matplotlib inline
#
#
# fsm = nx.Graph()
#
# fsm.add_node("start")
#
# nx.draw(fsm)
# mpl.savefig() # save as png
# mpl.show() # display


import matplotlib as mpl
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import networkx as nx
%matplotlib inline 
df = pd.DataFrame({'from': ['FINISH'], 'to': ['START']})
G=nx.from_pandas_edgelist(df, 'from', 'to')
nx.draw(G, with_labels=True)
plt.show()