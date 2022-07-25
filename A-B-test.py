import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# betore mesal array forooshe mahane ma dar 1sal baraye 2design mokhtalef
a = np.array([23, 21, 19, 24, 35, 17, 18, 24, 33, 27, 21, 23])
b = np.array([31, 28, 19, 24, 32, 27, 16, 41, 23, 32, 29, 33])

# ekhtelafe miangin haye 2data ro hesab mikonim
d = b.mean() - a.mean()

# 2 array beham michasboonim be tedade majmooe 2 array data
np.append(np.zeros(len(a)), np.ones(len(b)))

# data haro be array 0 o 1 michasbonim
sales_data = np.array([
    np.append(np.zeros(len(a)), np.ones(len(b))),
    np.append(a,b)
])
# transpose mikonim ke 2sotoon va jame a o b satr beshe
sales_data_t = sales_data.T
#print(sales_data_t)

# besoorate random 0 o 1 be tedade jame a ,b misazim
experiment_label = np.random.randint(0, 2, len(sales_data_t))

# data haye experiment random be 0 o 1 pakhsh mikonim
experiment_data = np.array([
    experiment_label,
    sales_data_t[:, 1]
])
# transpose mikonim data jadido ke 2sotoon va a + b  satr beshe
experiment_data_t = experiment_data.T
# az sotoone aval data haye marboot be 0 joda mikonim va az sotoone 2shoon miangin migirim
a2 = experiment_data_t[experiment_data_t[:, 0] == 0][:, 1].mean()
# data hai ke sotoone aval marboot be 1 hast joda mikonim va az sotoone 1 miangin migirim
b2 = experiment_data_t[experiment_data_t[:, 0] == 1][:, 1].mean()

# ekhteklafe miangine data haye random pakhsh shode
d2 = b2 - a2


# function minvisim baraye inke be tedade n bar betoonim amaliate balaro tekrar konim
def sh_exp(n):
    # data haye ekhtelafe miangino tuye ye dataframe ba N satr va 1 sotoon mirizim
    experiment_diff_mean = np.empty([n, 1])
    for times in np.arange(n):
        experiment_label2 = np.random.randint(0, 2, len(sales_data_t))
        experiment_data2 = np.array([
            experiment_label2,
            sales_data_t[:, 1]
        ]).T
        a3 = experiment_data2[experiment_data2[:, 0] == 0][:, 1].mean()
        b3 = experiment_data2[experiment_data2[:, 0] == 1][:, 1].mean()
        experiment_diff_mean[times] = b3 - a3
    return experiment_diff_mean

# sakhte 5000 data random shode dar function
el = sh_exp(5000)
# data haye random shodei ke ekhtelafeshon bishtar az data valias
m = len(el[el >= d])
# miangine tedade ekhtelaf miangin haye random shodei ke az ekhtelaf miangin data avalie bishtar shode
print(m/5000)

# age bishtar az 0.05 bashe yani data ehtemale ghavi random bude va shansi roshdesh
# age kamtar az 0.05 bashe yani data shansi tolid nashode roshdesh

# nemodare data haro rasm mikonim ke skahte shode
plt.hist(el, bins=100)
#plt.show()