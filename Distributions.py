import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


# sakhte data ba dist normal dummy ba miangin (loc) 0 va enheraf meyare (scale) 1
#data_normal = stats.norm.rvs(size=100, loc=0, scale=1)

#rasme plot ba seaborn va kde baraye khate ruye nemoodare
#sb.displot(data_normal, bins=100, kde=True)

# sakhte data ba dist uniform ba miangin (loc) va enheraf meyar (scale)
#data_uniform = stats.uniform.rvs(size=100, loc=0, scale=10)

# rasme nemodar uniform
#sb.displot(data_uniform, bins=100)

# data haye bernoulli va rasm ba  p ehtemal movafaghiat
#data_bernoulli = stats.bernoulli.rvs(size=100, p=0.2)
#sb.displot(data_bernoulli, bins=100)

# data haye binom ba tekrare size dafe va ehtemal movafaghiat p dar tedade n nafar chand bar movafaghiat dare
#data_binom = stats.binom.rvs(size=1000, n=100, p=0.2)
# rasme figure plot haye bala
#sb.displot(data_binom, bins=100)

#data haye multinomial ba tedade n baraye har azmayesh va shanse movafaghiat baraye harkodoom va tekrare size dafe
icu = 0.2
surgery = 0.3
good = 0.5
#data_multinomial = np.random.multinomial(n=100, pvals=(icu, surgery, good), size=100)

# tozie poison ba tedade movafaghiat ya kharabi o ... tuye bazeye morede nazar
#data_poisson = np.random.poisson(lam=7, size=100)
#sb.displot(data_poisson,bins=10)

# tozie namaei ( explonential ) ba scale (betore mesal age 2min harf mizanan ya 2bar kharab mishe ) = 1/2e
# vali numpy tabdil mikone 2ro be 1/2 pas faghat numpy 2 mizarim va tedad moshtari ha ke tekrar shode
data_exponential = np.random.exponential(scale=2, size=1000)
sb.displot(data_exponential, bins=100)
plt.show()
