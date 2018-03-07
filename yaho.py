import pandas as pd
import numpy as np
import seaborn as sns
sns.set()




data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)#importer la base de donnée sous la bonne format

#renomer les deux colonnes pour une meilleur visualisation
#rajouter une nouvelle colonne pour la somme 
data.columns = ['West', 'East']
data['Total'] = data.eval('West + East')
#faire le bilan de la base de donnée en ignorant les NA
data.dropna().describe()


#visialuser la base de donnée en fonction des heures
data.plot()
plt.ylabel('Hourly Bicycle Count');

#visialuser la base de donnée en fonction des semaines
weekly = data.resample('W').sum()
weekly.plot(style=[':', '--', '-'])
plt.ylabel('Weekly bicycle count');


#regrouper en jour et faire un plot pour la somme sur tout les 30 jours


daily = data.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
plt.ylabel('mean hourly count');

#visusaliser la moyenne du trafic en fonction des heures de la journée



by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-']);

#visualiser la moyenne de trafic en moyenne des jours de la semaine

by_weekday = data.groupby(data.index.dayofweek).mean()
by_weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
by_weekday.plot(style=[':', '--', '-']);


#visualiser selon la semaine et le weekend

weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
by_time = data.groupby([weekend, data.index.time]).mean()

by_time.ix['Weekday'].plot(ax=ax[0], title='Weekdays',
                           xticks=hourly_ticks, style=[':', '--', '-'])
by_time.ix['Weekend'].plot(ax=ax[1], title='Weekends',
                           xticks=hourly_ticks, style=[':', '--', '-']);


























