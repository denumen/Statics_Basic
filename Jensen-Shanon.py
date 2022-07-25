import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.stats import entropy
import seaborn as sb

#function jensen shannon
def js(p, q):
    p1 = p/np.linalg.norm(p, ord=1)
    q1 = q/np.linalg.norm(q, ord=1)
    m = 0.5*(p1+q1)
    r = 0.5*(entropy(p1, m)+entropy(q1, m))
    return r


wH_data = pd.read_csv('D:\Datasets\W-H\weight-height.csv')
# sakhte series az ghade mardan
m_height = wH_data[wH_data['Gender'] == 'Male']['Height']
# sakhte data normal ideal
i_height = np.random.normal(size=len(m_height), loc=m_height.mean(), scale=m_height.std())
# joda kardane data haye y o x bar asase hist ideal va data asli
m_count, m_division = np.histogram(m_height, bins=100)
i_count, i_division = np.histogram(i_height, bins=100)

# rasme plot 2data
#plt.hist(i_height)
#plt.hist(m_height)
#plt.show()

# mohasebe jensen shannon
#print(js(m_count, i_count))


#                     test ba ye data weather
ws_data = pd.read_csv('D:\Datasets\wind\wind_speed_laurel_nebraska.csv')
m_weather = ws_data['10 Min Sampled Avg']
i_weather = np.random.normal(size=len(m_weather), loc=m_weather.mean(), scale=m_weather.std())

mw_count, mw_division = np.histogram(m_weather, bins=100)
iw_count, iw_division = np.histogram(i_weather, bins=100)
#print(js(mw_count, iw_count))
#sb.displot(m_weather, bins=100, kde=True)
#sb.displot(i_weather, bins=100, kde=True)
#plt.show()

#          test ba data soccer
sc_data = pd.read_csv('D:\Datasets\soccer\soccer.csv')

# ezafe kardane sotoone total goals
sc_data['Total_scores'] = sc_data['home_score'] + sc_data['away_score']

t_score = sc_data['Total_scores']
i_score = np.random.normal(size=len(t_score), loc=t_score.mean(), scale=t_score.std())
ts_count, ts_division = np.histogram(t_score, bins=100)
is_count, is_division = np.histogram(i_score, bins=100)

# chon adad kheili ziade mishe fahmid ke az tozie normal peyravi nemikone
print(js(ts_count, is_count))
# barresi tozie poisson ba js baraye soccer scores
ip_score = np.random.poisson(size=len(t_score), lam=t_score.mean())
isp_count, isp_division = np.histogram(ip_score, bins=100)
print(js(ts_count, isp_count))

# mishe kamtarin js beyne tozi haye motefaveto peyda konim va bin haro taghir bedim ta be deghat behtari beresim
ts2_count, ts2_division = np.histogram(t_score, bins=10)
isp2_count, isp2_division = np.histogram(ip_score, bins=10)
print(js(ts2_count, isp2_count))
