import folium
from django.shortcuts import render
from .models import Location


def map_page(request):
    center = (13.133932434766733, 16.103938729508073)
    folium_map = folium.Map(location=center, zoom_start=2)
    locations = Location.objects.all()
    for location in locations:
        popup = f"""
        {location.name} <br>
        """
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=popup
        ).add_to(folium_map)
    folium_map.save("map/templates/map/map.html")
    return render(request, "map/map.html")
