# folium-geocoder-own-locations
Geocoder search plugin for folium with own places.

## how to use
   ```
   from geocoder_custom import Geocoder as Geocoder_custom

    suggestions = [
        {
            "name": 'Im manually added',
            "center": [50.27, 19.03]
        },
        {
           "name": 'RandomPosition78',
            "center": [50.10, 18.4]
        }
    ]
  
   Geocoder_custom(collapsed=True, add_marker=True, suggestions = suggestions).add_to(m)
   ```
## Results

![image](https://github.com/JohnyCarrot/folium-geocoder-own-locations/assets/107358703/3684826d-0363-4867-8fe0-5ac75766c57e)

![image](https://github.com/JohnyCarrot/folium-geocoder-own-locations/assets/107358703/d7c5b219-2bad-48a5-a90b-0adeb36b1a9d)


![image](https://github.com/JohnyCarrot/folium-geocoder-own-locations/assets/107358703/ed4a6b04-9b2f-4d27-a438-5c77d4ee44c3)

![image](https://github.com/JohnyCarrot/folium-geocoder-own-locations/assets/107358703/ce4c112a-66a7-43e5-a134-a9b9bdf56766)


