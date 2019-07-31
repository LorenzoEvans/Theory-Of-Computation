# import networkx as nx
# import matplotlib as mpl
# import matplotlib.pyplot
# %matplotlib inline
# fsm = nx.Graph()
# fsm.add_node("start")
# nx.draw(fsm)
# mpl.savefig() # save as png
# mpl.show() # display


# %matplotlib inline
# df = pd.DataFrame({'from': ['FINISH'], 'to': ['START']})
# G=nx.from_pandas_edgelist(df, 'from', 'to')
# nx.draw(G, with_labels=True)
# plt.show()

#### Jupyter notebook cell start ####

%matplotlib inline
from jupyterthemes import jtplot
jtplot.style(context='talk', fscale=1, spines=False, gridlines='--')
# CSS = """
# .output {
#     align-items: center;
#     border: 1px solid black;
# }
# """

# HTML('<style>{}</style>'.format(CSS))

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx
# %matplotlib inline
df = pd.DataFrame({'from':
                   ['start (nlb)', 'start (nlb)', 'start (nlb)', '<- (L-B) -> llb', '(P-B) -> blb' ],
                   'to': ['<- (L-B) -> llb', '(R-B) -> rlb ->', '(P-B) -> blb', '(R-B) -> rlb ->', 'start (nlb)']})
G=nx.from_pandas_edgelist(df, 'to', 'from')
nx.draw(G, with_labels=True, pos=nx.shell_layout(G), nodecolor='r', edge_color='b')
plt.show()
#### Jupyter notebook cell end ####