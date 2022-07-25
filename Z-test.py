from numpy import sqrt, abs,round
import pandas as pd
from scipy.stats import norm
import statsmodels.api as smd
import numpy as np


data = pd.read_csv('D:\Datasets\corona\Corona_Updated.csv')

# mikhaim bebinim dama rabti be bimaran dare ya na
# function 1 khati mizanim ke dama balatar az ye hadi tuye temp cat 1 ya 0 gharar begire
data['Temp_cat'] = data['Temprature'].apply(lambda x: 0 if x < 24 else 1)
#print(data['Temp_cat'].describe())

# daata haye damaye a va b ro joda mikonim az hamdige va tedade confirmed ro joda mikonim
data_a = data[data['Temp_cat'] == 1]['Confirmed']
data_b = data[data['Temp_cat'] == 0]['Confirmed']

# miangine har do dataro joda mikonim
mean_a = data_a.mean()
mean_b = data_b.mean()

# enheraf meyare hardo dataro joda mikonim
std_a = data_a.std()
std_b = data_b.std()

# tedade har do dataro joda mikonim
n_a = len(data_a)
n_b = len(data_b)

# tebghe formoole z test makhraj = d va soorat = n mizarim
d = sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
n = mean_a - mean_b

# formole z barabare n/d
z = n/d

# mohasebe p value tebghe formool
p_value = 2 * (1-norm.cdf(abs(z)))
print(p_value)



# baraye data haye A-B test ba z test mohasebe kardam
an = np.array([23, 21, 19, 24, 35, 17, 18, 24, 33, 27, 21, 23])
bn = np.array([31, 28, 19, 24, 32, 27, 16, 41, 23, 32, 29, 33])
mean_an = an.mean()
mean_bn = bn.mean()
std_an = an.std()
std_bn = bn.std()
n_an = len(an)
n_bn = len(bn)
dn = sqrt((std_an**2 / n_an) + (std_bn**2 / n_bn))
nn = mean_an - mean_bn
zn = nn/dn
pn_value = 2 * (1-norm.cdf(abs(zn)))
print(pn_value)


