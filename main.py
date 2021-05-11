import folium
from pathlib import Path

m = folium.Map(location=[32.55801995200005,
                         54.305910263000044], zoom_start=5.5)
with open("countries_edge.json", 'r', encoding='utf-8-sig') as f:
    countries_edge = f.read()

folium.GeoJson(countries_edge, name='‌Borders of countries').add_to(m)
feature_group = folium.FeatureGroup(name="Waterfalls Locations")

path = Path("waterfalls.txt")
waterfalls = path.read_text()
waterfalls = waterfalls.split("\n")

for waterfall in waterfalls[1:]:
    height = int(waterfall.split(',')[2])
    fillcolor = ''
    if height < 20:
        fillcolor = 'green'
    elif height < 50:
        fillcolor = 'orange'
    else:
        fillcolor = 'red'
    
    feature_group.add_child(folium.Marker([float(waterfall.split(',')[3]), float(waterfall.split(',')[4])], tooltip="Name= {} Location= {} Heght= {}Meters Latitude= {}\nLongitude= {}".format(waterfall.split(
        ',')[0].upper(), waterfall.split(',')[1], height, waterfall.split(',')[3], waterfall.split(',')[4]), icon=folium.Icon(color=fillcolor)))
m.add_child(feature_group)
folium.LayerControl().add_to(m)
m.save('index.html')
