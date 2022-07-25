from scipy import stats
import numpy as np
import pandas as pd



# betore mesal 5000 bimar dar rooz darim 0.2 bastari mishan mikhaim hesab konim beyne 0 ta 1000 bimar bastari mishan
# betore mesal az beyne 5000 morajee konande inke 1bastari ya 2 ya 3 ya .... ya 1000 ta bastari shan
c = 0
data = stats.binom(5000, 0.2)
#for i in range(0,1000):
#    c += data.pmf(i)
print(c)

# mikhaim befahmim hodoodan chanta takht bezarim ta 100% bimara betonan bastari shan age niaz bashe
#for i in range(0,1080):
#    c += data.pmf(i)
#print(c)

# cdf mohasebe mikone az baze 0 ta adade morede nazar cheghad ehtemalesh hast mesle pmf vali az baze 0 ta end
#print(data.cdf(1090))


# data haye poison baraye kharabi mahane server ha ya zang zadan haye sherkat
# betore mesal 160 nafar miangin harroz moshtari darim
data_poisson = stats.poisson(160)
# mikhaim bebinim cheghad ehtemal dare hadeaksar 150 nafar moshtari dashte bashim
#print(data_poisson.cdf(150))

# mikhaim bbinim cheghad ehtemal dare daghighan 200 nafar moshtari dashte bashim
#print(data_poisson.pmf(200))

# dadehaye peyvaste mesle normal baraye mesal daramade shahr ba miangin 2 va enheraf meyar 1
data_norm = stats.norm(2, 1)
# mohasebe daramad ha az 0 ta 2
print(data_norm.cdf(2))
# mohasebe daramad taghriban 2 chon data peyvaste hast daghighan 2 nadarim
print(data_norm.pdf(2))
# mohasebe data haei ke beyne 2.5 ta 3.5 mil daramad daran
print(data_norm.cdf(3.5) - data_norm.cdf(2.5))

