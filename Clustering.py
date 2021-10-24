import csv
import pandas as pd 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Reading data

df = pd.read_csv("total_stars.csv")

X = []
star_masses = []
star_radius = []
wcss = []


for index , star_mass in enumerate(star_masses):
  temp_list = [star_radius[index],star_mass]
  X.append(temp_list)

for i in range(1,11):
 kmeans = KMeans(n_clusters = i , init = 'k-means++',random_state = 24)
 wcss.append(kmeans)

plt.figure(figsize = (10,5))
plt.plot(range (1,11) , str(wcss ,marker = 'o',color = 'blue')
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Wcss')
plt.show()