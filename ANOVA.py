import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm

data = pd.read_csv('D:\Datasets\campaign\campain.csv')
print(data)

# miangin forooshe harkodoom az forooshandeharo hesab mikonim
print(data.groupby('Campain').mean())

# baraye barresi data az osl target sell hast va daste bandi ba campain
result = ols('Sell ~ Campain', data=data).fit()

# tozi f hesab mikonim ba stats model
print(sm.stats.anova_lm(result))
