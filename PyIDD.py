import pyidd
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('D:\Datasets\W-H\weight-height.csv')

# hameye tozi haro baraye data bedast miare va SSE khataye un data az tozi hast harchi kamtar bashe bishtar shabihe
p = pyidd.PyIDD(verbose=1)
p.fit(data['Height'])

# rasme plot baraye 15ta az nazdiktarin tozi ha be data
p.plot(top=15)
plt.show()
# tartib gozashtan baraye tozi ha az SSE kam be ziad
p.get_distributions()
