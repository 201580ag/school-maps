import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Load the data
data = pd.read_excel(".//전국초중등학교위치표준데이터-20231110.xlsx")

# Extract the relevant columns
school = data[['학교명', '학교급구분', '위도', '경도']]

# Create a base map
map = folium.Map(location=[36, 127], zoom_start=7)

# Add school markers to the map
for i in school.index:
    name = school.loc[i, '학교명']
    lat = school.loc[i, '위도']
    lon = school.loc[i, '경도']
    marker = folium.Marker([lat, lon], popup=name).add_to(map)

# Create a new map with school markers colored by '학교급구분'
map2 = folium.Map(location=[36, 127], zoom_start=7)
for i in school.index:
    name = school.loc[i, '학교명']
    lat = school.loc[i, '위도']
    lon = school.loc[i, '경도']
    if school['학교급구분'][i] == '초등학교':
        code_color = 'orange'
    elif school['학교급구분'][i] == '중학교':
        code_color = 'green'
    elif school['학교급구분'][i] == '고등학교':
        code_color = 'blue'
    else:
        code_color = 'black'
    marker = folium.Marker([lat, lon], popup=name, icon=folium.Icon(color=code_color)).add_to(map2)

# Create a new map with a marker cluster
map3 = folium.Map(location=[36, 127], zoom_start=7)
marker_cluster = MarkerCluster().add_to(map3)

for lat, long in zip(school.위도, school.경도):
    folium.Marker([lat, long]).add_to(marker_cluster)

# Save the maps as HTML files
map.save('map1.html')
map2.save('map2.html')
map3.save('map3.html')
