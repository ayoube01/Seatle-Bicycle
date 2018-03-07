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


