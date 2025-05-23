import folium
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Location
from blog.models import Post


def map_page(request):
    center = (13.133932434766733, 16.103938729508073)
    folium_map = folium.Map(location=center, zoom_start=2)
    locations = Location.objects.all()
    for location in locations:
        popup = f"""
        <a href="/map/{location.name}">{location.name}</a>
        """
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=popup
        ).add_to(folium_map)

    return HttpResponse(folium_map.get_root().render())


def post_list_by_location(request, name):
    location = Location.objects.get(name__iexact=name)

    folium_map = folium.Map(
        location=[location.latitude, location.longitude],
        zoom_start=4, width=400, height=300
    )
    folium.Marker(
            location=[location.latitude, location.longitude],
            popup=location.name
        ).add_to(folium_map)

    location_map = folium_map._repr_html_()

    posts = Post.objects.filter(
        location=location, published_date__lte=timezone.now()
    ).order_by('-published_date')

    return render(
        request, 'map/post_list_by_location.html',
        {"posts": posts, "location": location, "location_map": location_map}
    )
