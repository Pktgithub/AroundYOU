from django.shortcuts import render,redirect,get_object_or_404
from .models import userLocation
import requests

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def save_locations(request) :
    if request.method == "POST" :
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        location = userLocation(latitude = float(lat), longitude=float(lon))
        location.save()
      

        return redirect('show_places',location_id= location.id,)
    return redirect('index')
    
# Geoapify API Key
GEOAPIFY_API_KEY = "use your own"
def show_places(request, location_id):
    # Get the saved user location from DB
    location = get_object_or_404(userLocation, id=location_id,)
    lat, lon = location.latitude, location.longitude
    radius = 5000  # in meters

    # Build Geoapify API request
    # if place_type == 'tourist' :
    url = (
            f"https://api.geoapify.com/v2/places"
            f"?categories=tourism.sights,tourism.attraction"
            f"&filter=circle:{lon},{lat},{radius}"
            f"&limit=20&apiKey={GEOAPIFY_API_KEY}"
        )
    

    response = requests.get(url)
    data = response.json()

    # Places are in features list
    places = data.get('features', [])

    return render(request, 'places.html', {
        'places': places,
        'lat': lat,
        'lon': lon,
    })