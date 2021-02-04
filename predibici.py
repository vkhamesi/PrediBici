## importation des librairies nécessaires
import os
import numpy as np
import matplotlib.pyplot as plt
import math as m
import seaborn as sn
import pandas as pd
from sklearn.svm import SVR
plt.style.use('Solarize_Light2')

## choix du dossier principal
os.chdir('/Users/victorkhamesi/Desktop/WEEX')
df = pd.read_csv('2019-07.csv', delimiter=',')
del df['Fecha_Arribo']
del df['Bici']

station = 1
jour = '01/07/2019'
capamax = 26 # paramètre trouvé en faisant plusieurs analyses sur les échantillons tracés

df.columns = ['Genre', 'Age', 'Station_dep', 'Jour', 'Heure_dep', 'Station_arr', 'Heure_arr']
#del df['Genre']
#del df['Age']

df.set_index('Jour')
df = df[['Jour', 'Station_dep', 'Heure_dep', 'Station_arr', 'Heure_arr']]

## construction DataFrame intermédiaires
df_dep = df.loc[df['Station_dep'] == station]
df_arr = df.loc[df['Station_arr'] == station]
del df_dep['Station_arr']
del df_dep['Heure_arr']
del df_dep['Station_dep']
del df_arr['Station_dep']
del df_arr['Heure_dep']
del df_arr['Station_arr']
df_dep = df_dep.loc[df_dep['Jour'] == jour]
df_arr = df_arr.loc[df_arr['Jour'] == jour]
del df_dep['Jour']
del df_arr['Jour']
df_dep.columns = ['date']
df_arr.columns = ['date']

## idée : conserver une seule station (la station 1) dans un quartier similaire à celui dans lequel on travaille et réaliser des prédictions sur le remplissage de la station
## à partir des données brutes, estimer comme dans l'exemple le remplissage de la station

df_dep['retrait'] = -1
df_arr['ajout'] = +1

## DataFrame total avec tous les ajouts et retraits de la journée
DataFrame = pd.merge(df_dep, df_arr, on='date', how='outer', sort=True)
DataFrame = DataFrame.fillna(0)

DataFrame['quantity'] = 0
DataFrame['quantity'][0] = capamax
for i in range(1,len(DataFrame)) :
    DataFrame['quantity'][i] = DataFrame['quantity'][i-1] + DataFrame['retrait'][i] + DataFrame['ajout'][i]

## affichage des résultats
DataFrame['quantity'].plot()
plt.show()
#(DataFrame['quantity'] + 0.2*DataFrame['quantity']).plot()
#(DataFrame['quantity'] - 0.2*DataFrame['quantity']).plot()
#plt.show()

## Holt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, Holt, ExponentialSmoothing
model = ExponentialSmoothing(np.asarray(DataFrame.quantity))
fit1 = ExponentialSmoothing(np.asarray(DataFrame.quantity),seasonal_periods=144, trend='add', seasonal='add').fit(optimized=True)
pred1 = fit1.forecast(30)
fit2 = ExponentialSmoothing(np.asarray(DataFrame.quantity),seasonal_periods=144, trend='add', seasonal='add',damped=True).fit(optimized=True)
pred2 = fit2.forecast(30)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(DataFrame.quantity)
for p, f, c in zip((pred1, pred2),(fit1, fit2),('#ff7823','#3c763d')):
    ax.plot(f.fittedvalues[150:], color=c)
    ax.plot(p, label="alpha="+str(f.params['smoothing_level'])[:4]+", beta="+str(f.params['smoothing_slope'])[:4]+",phi"+str(f.params['damping_slope'])[:4]+",gamma"+str(f.params['smoothing_seasonal'])[:4], color=c)
plt.title("Holt-Wineter's Exponential Smoothing")
plt.legend()