from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# function mohasebe kullback
def kul(p, q):
    # epsilon baraye inke 0 warning nade mizarim
    epsilon = 0.00000001
    p = p + epsilon
    q = q + epsilon
    # tebghe formule kullback jaigozari mikonim
    result = np.sum(p*np.log(p/q))
    return result


# sakhte data az -10 ta 10 ba fasele 0.001
x = np.arange(-10, 10, 0.001)
len(x)
# sakhte data normal ba  tozie pdf shode yani pdf data ba miangin va std dade shode
p = norm.pdf(x, 0, 2)
q = norm.pdf(x, 2, 3)

# rasme nemodar ha baraye moghayese
plt.plot(x, p, c='blue')
plt.plot(x, q, c='red')
#plt.show()


# data haye ghad o vazn
data = pd.read_csv('D:\Datasets\W-H\weight-height.csv')

# baraye mohasebe data haye vaghei ghad o vazn kullback ro hesab mikonim

# sakhte series az ghade mardan
m_height = data[data['Gender'] == 'Male']['Height']
# rasme hist baraye data haye ghad mardan
m_height.hist(bins=100)
# sakhte yek data random tebghe tozie normal baraye moghayese data haye asli ba data ideal normal
i_height = norm.rvs(size=5000, loc=m_height.mean(), scale=m_height.std())
# joda kardane data haye histogram yani mehvare y(tedade har data az baze haye x) = count
# ,mehvare x(baze haye data ha from to end) = division baraye estekhraje data
m_count, m_division = np.histogram(m_height, bins=100)
i_count, i_division = np.histogram(i_height, bins=100)
# rasme nemodare histogram ba data haye normal ideal
plt.hist(i_height)

# baraye inke ehtemale p va q hesab konim ta rahat tar baraye har data befahmim adade bedast umade monasebe taghsim be
# tedad mikonim har data ro ta ehtemale har data bedast biad
m_count = m_count/5000
i_count = i_count/5000
# moshahede adade kullback harchi kamtar bashe natije behtari mide
print(kul(m_count, i_count))
