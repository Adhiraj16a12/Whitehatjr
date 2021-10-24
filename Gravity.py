import csv
import plotly.express as px

rows = []
with open('total_stars.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

print(headers)
headers[0] = "row_number"
print(star_data_rows[0])

#Gravity

star_gravity = []
star_masses = []
star_names = []
star_radius = []
star = []


for star_data in star_data_rows:
    star_masses.append(star_data[3])
    star_names.append(star_data[1])
    star_radius.append(star_data[4])

for index , name in enumerate(star_names):
    gravity = (float(star_masses[index])*5.972e+24) / (float(star_radius[index])*float(star_radius[index])*6371000*6371000) * 6.674e-11
    star_gravity.append(gravity)

#Gravity more than 150

low_gravity_star = []

for index , gravity in enumerate(star_gravity):
  if star > 150:
    low_gravity_star.append(star_data_rows[index])
  
print(len(low_gravity_star))


#Gravity less than 350

for index , gravity in enumerate(star_gravity):
  if star < 350:
    low_gravity_star.append(star_data_rows[index])

print(len(low_gravity_star))


#Define star name

star_name = []
star_name.append(star_data[1])

#Plotting Mass

for planet_data in low_gravity_star:
  star_masses.append(planet_data[3])


fig = px.scatter(x = star_name , y = star_masses)
fig.show()

#Plotting Radius

for planet_data in low_gravity_star:
  star_radius.append(star_data[5])


fig = px.scatter(x = star_name , y = star_radius)
fig.show()
