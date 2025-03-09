import folium
from django.shortcuts import render


def map_page(request):
    center = (13.133932434766733, 16.103938729508073)
    folium_map = folium.Map(location=center, zoom_start=2)
    folium_map.save("map/templates/map/map.html")
    return render(request, "map/map.html")
