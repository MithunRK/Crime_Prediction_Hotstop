import folium
import os
m=folium.Map(location=[41.8781,-87.6298],zoom_start=12)
tooltip = 'click for more info'
data=r'C:\Users\rkmit\Desktop\Boundaries - Police Districts (current).geojson'
layout=data



import pandas as pd

# Make a data frame with dots to show on the map
data = pd.DataFrame({
   'lon':[-87.71034398494957,-87.65604480213752,-87.82525347058534,-87.64167850210183,-87.71721348193834,-87.69191938238211,-87.63379809489706,-87.58490775585948,-87.6647929389803,-87.8066412814894,-87.70624111986568,-87.62990629743399,-87.65168366381208,-87.70664109860438,-87.63060984943517,-87.57917050491052,-87.55338788852362,-87.59913850977236,-87.68587597495392,-87.61584971691116,-87.63034676468665,-87.60616881517161],
   'lat':[41.99490443749173, 41.99009486986016,41.98306864286755,41.967623257844245,41.93282842534008,41.93901200340937,41.72885314704923,41.718655913807865,42.022224691270125,42.01133369018264,41.822565687957166,41.92613798438551,41.89990852130757,41.898133344665915,41.788884248746285,41.791299116414805,41.76048653247689,41.74219948086281,41.86089004933658,41.88839074489003,41.838042017316134,41.83758189996618],
   'name':['17:albany park', '20:lincoln', '31', '19:town hall', '25:grand central', '14:shakesphere', '22:morgan park', '24:roger park','16:jeferson park','8:chicago lawn','18:near north','12:near west','15:austin','7:eaglewood','3:grand crossing','4:south chicago','6:grisham','10:ogden','1:central','9:deering','2:wentworth','23'],
   'value':[10, 12, 40, 70, 23, 43, 100, 43,10, 12, 40, 70, 23, 43, 100, 43,10, 12, 40, 70, 23, 43]
}, dtype=str)


for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
   ).add_to(m)
   
m.save('map1.html')