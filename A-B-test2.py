import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import statsmodels.api as smd

data = pd.read_csv('D:\Datasets\demy\Ab_data.csv')


# shenasai data ha - tedad satr o sotoon
#print(data.shape)

# head
#print(data.head())

# unique ha
#print(data.nunique())

# info
#print(data.info())

# hazfe data hai ke treatment hastan vali newpage naraftan
#print(data.query('group == "treatment" and landing_page != "new_page"'))

# shenasai data haye kharabe control ke old page naraftan
#print(data.query('group == "control" and landing_page != "old_page"'))

# joda mikonim data haye salem ro
data_treatment = data.query('group == "treatment" and landing_page == "new_page"')
data_control = data.query('group == "control" and landing_page == "old_page"')

# data haye salemo baham merge mikonim
data_merge = data_treatment.merge(data_control, how='outer')
#print(data_merge)

# data haro check mikonim dobare
#print(data_merge.nunique())

# hanoz yek data tekrari hast chon user_id = 290584 vali timestamp = 290584
# data hai ke  duplicate nistan joda mikonim
data_merge = data_merge[~data_merge.duplicated(subset=['user_id'], keep='first')]
#print(data_merge.info())


# chon miangine hardota nazdike behame mishe goft tasiri nadashte ruye afzayeshe moshtari vali chon morabia kamtar
# azyat shodan vali miangine old bishtar bude mikhaim bebinim vaghean kamtar bude moshtari ya random bude
data_control2 = data_merge.query('group == "control"')
data_treatment2 = data_merge.query('group == "treatment"')

# check mikonim miangine convert kodoom behtare
#print(data_treatment2.converted.mean())
#print(data_control2.converted.mean())
#print(data_merge.converted.mean())

# baraye har daste az data besoorate binom tekrar mikonim harchi size bozorgtar deghat bishtar
old_p_convert = np.random.binomial(len(data_control2), data_merge.converted.mean(), size=1000)/len(data_control2)
new_p_convert = np.random.binomial(len(data_treatment2), data_merge.converted.mean(), size=1000)/len(data_treatment2)
#print(new_p_convert)

# ekhtelafe data haye sakhte shodaro migirim baraye old va new
p_diff = new_p_convert - old_p_convert
# miangin migirim az ekhtelafeshon
#print(p_diff.mean())

# ekhtelafe miangine bakhshe convert data haye aslio hesab mikonimm
m_diff = data_treatment2['converted'].mean() - data_control2['converted'].mean()
#print(m_diff)

# age ekhtelafe data haye sakhte shode bishtar az ekhtelafe data haye vaghei bashe yani shansi nabude be un ehtemal
#print((p_diff > m_diff).mean())
#print((p_diff < m_diff).mean())

# rasm mikonim data haye sakhte shodaro ekhtelafeshono
plt.hist(p_diff, bins=50)
low = m_diff
high = p_diff.mean()
plt.axvline(x=low, color='g')
plt.axvline(x=high, color='r')
#plt.show()

# ba stats models hamin karaye balaro mikonim
# tedade unai ke tabdil  be moshtari shodan az old o new
converted_old = len(data_control2[data_control2['converted'] == 1])
converted_new = len(data_treatment2[data_treatment2['converted'] == 1])
# tedade kole unai ke new budan ya old
n_old = len(data_control2)
n_new = len(data_treatment2)

# ehtemale inke farze aslimon in bashe ke bozorgtare va farze alt kochiktar budan bashe
#print(smd.stats.proportions_ztest([converted_old, converted_new], [n_old, n_new], alternative='smaller'))
# ehtemale inke farze aslimon in bashe ke ko chiktare va farze alt bozorgtar budan bashe
#print(smd.stats.proportions_ztest([converted_old, converted_new], [n_old, n_new], alternative='larger'))


print(converted_new)
print(converted_old)
print(n_new)
print(n_old)
