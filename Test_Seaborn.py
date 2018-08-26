import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

# ts = pd.read_excel('demo_1.xlsx','Sheet1',index_col=None,na_values=['NA'])
# ts = ts.cumsum()
# ts.plot()
# plt.show()