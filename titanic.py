import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('titanic.csv', sep = ';')

#print(data.shape[0])
#print(len(data))
#print(data.describe())

#print(data.loc[data['classe']==3,:].mean())
print(data.groupby(['classe']).mean()['survie'])
print(data.dtypes)
print(data.loc[pandas.isna(data['tarif']),:])
print(len(data.loc[data['tarif']==0,:]))
# & data['tarif'] != ''
#print(data['survie'].mean())
#print(data.groupby(['sexe'])['survie'].mean())
#print(data.groupby(['classe','sexe'])['survie'].mean())
#data.hist(column = 'tarif', figsize = (9,6), bins = 10)
#plt.show()
