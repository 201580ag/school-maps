import pandas as pd
import folium

# 데이터를 불러옵니다.
data = pd.read_excel(".//전국초중등학교위치표준데이터-20231110.xlsx")

school = data[['학교명', '학교급구분', '위도', '경도']]

# 기본 지도를 생성합니다.
map = folium.Map(location=[36, 127], zoom_start=7)

# 학교 위,경도 데이터로 지도위에 학교 위치를 표시합니다.
for i in school.index:
    name = school.loc[i, '학교명']
    lat = school.loc[i, '위도']
    lon = school.loc[i, '경도']
    marker = folium.Marker([lat, lon], popup=name).add_to(map)

# 학교급구분 코드를 활용하여 학교별 마커에 색상을 부여합니다.
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

# Save the maps as HTML files
map.save('map1.html')
map2.save('map2.html')
