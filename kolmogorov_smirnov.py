from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import kstest

data = pd.read_csv('D:\Datasets\W-H\weight-height.csv')
m_data = data[data['Gender'] == 'Male']['Height']
f_data = data[data['Gender'] == 'Female']['Height']

m_count, m_division = np.histogram(m_data, bins=100)
f_count, f_division = np.histogram(f_data, bins=100)

# age ks test pvalue kamtar az 0.05 bashe yani az tozi haye motefaveti peyravi mikonan hatman
print(kstest(m_count, f_count))

#rasme nemodar ha besoorate cmf ya cumolative
#plt.plot(np.cumsum(m_count))
#plt.plot(np.cumsum(f_count))
#plt.show()

# rasme nemodare data haye sort shode besorate histogram
#plt.hist(m_data.sort_values())
#plt.hist(f_data.sort_values())
plt.show()

# rasme data ha
#plt.plot(m_data.sort_values(), bins=100)
#plt.plot(f_data.sort_values(), bins=100)
plt.show()

# reset kardane index data baraye rasm
#plt.plot((m_data.sort_values().reset_index)(drop=True))
#plt.plot((f_data.sort_values().reset_index)(drop=True))
plt.show()

# momkene data haye normal bashan hardo vali chon mianagin va std motefavete adad khob nabashe baraye hamin
# miaim har data ro mianginesho kam mikonim ta az 0 rasm beshan hardo
m_data = m_data - m_data.mean()
f_data = f_data - f_data.mean()
#plt.hist(m_data.sort_values(), bins=100)
#plt.hist(f_data.sort_values(), bins=100)
plt.show()
# ks test two way hast chon az 2 data nazari tashkil shode yeki sample va yeki vaghei nist
print(kstest(m_data, f_data))
# ks test one way chon yeki random sakhte shode yeki vaghei
ideal_m = norm.rvs(size=5000, loc=m_data.mean(), scale=m_data.std())
print(kstest(m_data, ideal_m))

